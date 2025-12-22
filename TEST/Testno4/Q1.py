def print_factors(n):
    
    if n <= 0:
        print("Please give a positive integer.")
        return []
    factors = []
    
    for i in range(1, n//2 + 1):
        if n % i == 0:
            factors.append(i)
    factors.append(n)         
    print("Factors of", n, ":", ", ".join(map(str, factors)))
    return factors

print_factors(15)