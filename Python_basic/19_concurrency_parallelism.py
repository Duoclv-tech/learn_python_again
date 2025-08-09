"""
PHẦN 19: CONCURRENCY VÀ PARALLELISM TRONG PYTHON
================================================

Bài tập về Threading, Multiprocessing, Asyncio, Concurrent.futures và GIL.
"""

# CÂU HỎI 1: Threading module
# a) Tạo 3 thread in ra thông điệp kèm tên thread
# b) Dùng Lock để bảo vệ biến đếm dùng chung khi tăng 100_000 lần
# c) Dùng Queue để giao tiếp giữa các thread (producer/consumer)

# Code của bạn ở đây:



# CÂU HỎI 2: Multiprocessing module
# a) Tạo 2 process, mỗi process tính tổng 1..n cho n khác nhau
# b) Dùng Pool để map một hàm tính bình phương lên list số lớn
# c) Dùng Manager (hoặc Value/Array) để chia sẻ trạng thái giữa các process

# Code của bạn ở đây:



# CÂU HỎI 3: Asyncio và async/await
# a) Viết 3 coroutine giả lập I/O (asyncio.sleep) và chạy đồng thời
# b) Dùng asyncio.gather để gom kết quả
# c) Dùng asyncio.create_task để tạo task và hủy một task giữa chừng

# Code của bạn ở đây:



# CÂU HỎI 4: concurrent.futures
# a) Dùng ThreadPoolExecutor để tải giả lập 10 công việc I/O
# b) Dùng ProcessPoolExecutor để tính toán CPU-bound (ví dụ: đếm số nguyên tố)
# c) So sánh thời gian chạy giữa ThreadPool và ProcessPool cho bài toán phù hợp

# Code của bạn ở đây:



# CÂU HỎI 5: GIL (Global Interpreter Lock)
# a) Viết đoạn mô tả ngắn về GIL và tác động của nó đến multi-thread CPU-bound
# b) Thiết kế thí nghiệm nhỏ chứng minh: CPU-bound dùng threads không tăng tốc, còn multiprocessing thì có
# c) Kết luận khi nào nên dùng Threading vs Multiprocessing vs Asyncio

# Trả lời của bạn ở đây:



"""
ĐÁP ÁN THAM KHẢO (hãy tự làm trước khi xem)

# CÂU HỎI 1: Threading
import threading
import time
from queue import Queue

def worker_print(name):
    print(f"[Thread] Xin chào từ {name}")

threads = [threading.Thread(target=worker_print, args=(f"T{i}",)) for i in range(3)]
for t in threads: t.start()
for t in threads: t.join()

# b) Bảo vệ biến đếm
counter = 0
lock = threading.Lock()

def increment(n):
    global counter
    for _ in range(n):
        with lock:
            counter += 1

ts = [threading.Thread(target=increment, args=(100_000,)) for _ in range(2)]
for t in ts: t.start()
for t in ts: t.join()
print("Counter =", counter)  # kỳ vọng 200_000

# c) Producer/Consumer với Queue
q = Queue()

def producer(q: Queue, n=5):
    for i in range(n):
        item = f"item-{i}"
        print("Produce:", item)
        q.put(item)
    q.put(None)  # tín hiệu kết thúc

def consumer(q: Queue):
    while True:
        item = q.get()
        if item is None:
            break
        print("Consume:", item)

tp = threading.Thread(target=producer, args=(q,))
tc = threading.Thread(target=consumer, args=(q,))
tp.start(); tc.start(); tp.join(); tc.join()


# CÂU HỎI 2: Multiprocessing
import multiprocessing as mp

def sum_to(n: int) -> int:
    return n * (n + 1) // 2

if __name__ == "__main__":
    p1 = mp.Process(target=lambda: print("sum(1..10^6)=", sum_to(1_000_000)))
    p2 = mp.Process(target=lambda: print("sum(1..10^7)=", sum_to(10_000_000)))
    p1.start(); p2.start(); p1.join(); p2.join()

    # Pool map
    with mp.Pool(processes=mp.cpu_count()) as pool:
        nums = list(range(10))
        squares = pool.map(lambda x: x*x, nums)
        print("Squares:", squares)

    # Manager list
    with mp.Manager() as manager:
        shared = manager.list()
        def add_values(n):
            for i in range(n):
                shared.append(i)
        ps = [mp.Process(target=add_values, args=(100,)) for _ in range(2)]
        [p.start() for p in ps]; [p.join() for p in ps]
        print("Shared length:", len(shared))


# CÂU HỎI 3: Asyncio
import asyncio

async def fake_io(name, delay):
    await asyncio.sleep(delay)
    return f"{name} done in {delay}s"

async def main_async():
    # gather
    results = await asyncio.gather(
        fake_io("A", 0.5), fake_io("B", 0.3), fake_io("C", 0.1)
    )
    print("gather:", results)

    # create_task + cancel
    t1 = asyncio.create_task(fake_io("Task-1", 1.0))
    t2 = asyncio.create_task(fake_io("Task-2", 2.0))
    await asyncio.sleep(0.6)
    t2.cancel()
    try:
        r1 = await t1
        r2 = await t2
    except asyncio.CancelledError:
        r2 = "Task-2 cancelled"
    print("tasks:", r1, r2)

# asyncio.run(main_async())


# CÂU HỎI 4: concurrent.futures
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

def io_task(i):
    time.sleep(0.05)
    return i

def is_prime(n: int) -> bool:
    if n < 2: return False
    if n % 2 == 0 and n != 2: return False
    r = int(n ** 0.5)
    for x in range(3, r+1, 2):
        if n % x == 0:
            return False
    return True

def demo_executors():
    # ThreadPool cho I/O
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = [ex.submit(io_task, i) for i in range(50)]
        done = [f.result() for f in as_completed(futs)]
        print("ThreadPool I/O results:", len(done))

    # ProcessPool cho CPU-bound
    nums = list(range(100_00, 101_00))
    with ProcessPoolExecutor() as ex:
        primes = list(ex.map(is_prime, nums))
    print("Có", sum(primes), "số nguyên tố trong dải", len(nums))

# demo_executors()


# CÂU HỎI 5: GIL
gil_note = """
GIL (Global Interpreter Lock) là cơ chế khóa toàn cục của CPython đảm bảo chỉ có một thread Python
thực thi bytecode tại một thời điểm. Hệ quả:
- Tác vụ CPU-bound dùng nhiều thread thường không tăng tốc đáng kể do bị tuần tự hóa bởi GIL.
- Tác vụ I/O-bound vẫn hưởng lợi từ threading do thread được nhường khi I/O chờ.
Khuyến nghị:
- CPU-bound: dùng multiprocessing hoặc chuyển sang C/NumPy/Cython.
- I/O-bound: dùng threading hoặc asyncio.
"""
print(gil_note)
