import threading

results = [0, 0, 0, 0]

def sum_of_squares(start, end, index):
    total = 0
    for i in range(start, end + 1):
        total += i * i
    results[index] = total

n = 100
num_threads = 4
threads = []

step = n // num_threads

for i in range(num_threads):
    start = i * step + 1
    end = (i + 1) * step if i != num_threads - 1 else n
    thread = threading.Thread(target=sum_of_squares, args=(start, end, i))
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()

total_sum_of_squares = sum(results)
print("Sum of squares from 1 to 100 is:", total_sum_of_squares)
