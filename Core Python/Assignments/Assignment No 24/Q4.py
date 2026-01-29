import threading
import queue
import random
import time

BUFFER_SIZE = 5
q = queue.Queue(BUFFER_SIZE)

def producer(name):
    for _ in range(10):
        item = random.randint(1, 100)
        q.put(item)  # Waits if buffer is full
        print(f"Producer {name} produced {item}")
        time.sleep(random.random())

def consumer(name):
    for _ in range(10):
        item = q.get()  # Waits if buffer is empty
        print(f"Consumer {name} consumed {item}")
        time.sleep(random.random())

# Create threads
producers = [threading.Thread(target=producer, args=(i,)) for i in range(1, 3)]
consumers = [threading.Thread(target=consumer, args=(i,)) for i in range(1, 3)]

# Start threads
for t in producers + consumers:
    t.start()
for t in producers + consumers:
    t.join()
