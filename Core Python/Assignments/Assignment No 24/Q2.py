import threading

# Shared resources
n = 10
condition = threading.Condition()
turn = "odd"  # Start with odd numbers

def print_odd():
    global turn
    for i in range(1, n + 1, 2):  # 1, 3, 5, 7, 9
        with condition:
            while turn != "odd":
                condition.wait()  # Wait until it's odd's turn
            print(i, end=" ")
            turn = "even"  # Next turn is even
            condition.notify()  # Wake up the even thread

def print_even():
    global turn
    for i in range(2, n + 1, 2):  # 2, 4, 6, 8, 10
        with condition:
            while turn != "even":
                condition.wait()  # Wait until it's even's turn
            print(i, end=" ")
            turn = "odd"  # Next turn is odd
            condition.notify()  # Wake up the odd thread

# Create threads
t1 = threading.Thread(target=print_odd)
t2 = threading.Thread(target=print_even)

# Start threads
t1.start()
t2.start()

# Wait for threads to finish
t1.join()
t2.join()
