def palindrome():
    n = 1
    while True:
        if str(n) == str(n)[::-1]:
            yield n
        n += 1

p = palindrome()
for _ in range(10):
    print(next(p))