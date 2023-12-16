prime_count = 0
start = 2
end = 10

for n in range(start, end):
    for x in range(2, n):
        if n % x == 0:
            print(n, "is equal to", x, "*", n // x)
            break
    else:
        # loop fell through without finding a factor
        print(n, "is a prime number")
        prime_count += 1
print(f"There are {prime_count} prime numbers between {start} and {end - 1}")
