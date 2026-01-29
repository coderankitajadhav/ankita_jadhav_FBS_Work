import threading

condition = threading.Condition()
turn = "lower"  # Start with lowercase

def print_lowercase():
    global turn
    for c in range(ord('a'), ord('z') + 1):
        with condition:
            while turn != "lower":
                condition.wait()
            print(chr(c), end="")
            turn = "upper"
            condition.notify()

def print_uppercase():
    global turn
    for c in range(ord('A'), ord('Z') + 1):
        with condition:
            while turn != "upper":
                condition.wait()
            print(chr(c), end=" ")
            turn = "lower"
            condition.notify()

# Create threads
t1 = threading.Thread(target=print_lowercase)
t2 = threading.Thread(target=print_uppercase)

# Start threads
t1.start()
t2.start()

# Wait for threads
t1.join()
t2.join()
