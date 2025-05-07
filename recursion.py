# 1. Recursive multiplication using addition
def recursive_multiply(a, b):
    if b == 0:
        return 0
    if b < 0:
        return -recursive_multiply(a, -b)
    return a + recursive_multiply(a, b - 1)

# 2. Recursive exponentiation
def recursive_power(base, exponent):
    if exponent == 0:
        return 1
    return base * recursive_power(base, exponent - 1)

# 3. Countdown from n to 0
def countdown(n):
    if n < 0:
        return
    print(n)
    countdown(n - 1)

# 4. Count up from 0 to n
def countup(n, current=0):
    if current > n:
        return
    print(current)
    countup(n, current + 1)

# 5. Reverse a string recursively
def reverse_string(s):
    if s == "":
        return ""
    return reverse_string(s[1:]) + s[0]

# 6. Check if a number is prime recursively
def is_prime(n, divisor=None):
    if n <= 1:
        return False
    if divisor is None:
        divisor = n - 1
    if divisor == 1:
        return True
    if n % divisor == 0:
        return False
    return is_prime(n, divisor - 1)

# 7. Fibonacci sequence (recursive)
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Sample calls
# if __name__ == "__main__":
#     print("1. Multiply 4 * -3:", recursive_multiply(4, -3))
#     print("2. Power 2^5:", recursive_power(2, 5))
#     print("3. Countdown from 5:")
#     countdown(5)
#     print("4. Count up to 5:")
#     countup(5)
#     print("5. Reverse 'hello':", reverse_string("hello"))
#     print("6. Is 13 prime?:", is_prime(13))
#     print("7. Fibonacci(6):", fibonacci(6))

#Tower of Hanoi
def TowerOfHanoi(n, source, destination_rod, auxiliary_rod):
    if n == 1:
        print("Move disk 1 from source ", source, " to destination ", destination_rod)
        return
    TowerOfHanoi(n - 1, source, auxiliary_rod, destination_rod)
    print("Move disk ", n, " from source ", source, " to destination ", destination_rod)
    TowerOfHanoi(n - 1, auxiliary_rod, destination_rod, source)

n = 4
TowerOfHanoi(n, 'A', 'B', 'C')
