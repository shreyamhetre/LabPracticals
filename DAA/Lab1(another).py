# Recursive approach
def recursive_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


# Non-recursive approach
def non_recursive_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[n]


user_input = input("Enter a positive integer n: ")
n = int(user_input)
fib_series = [non_recursive_fibonacci(i) for i in range(n + 1)]
print(f"Fibonacci series up to the {n}th number: {fib_series}")
recursive_result = recursive_fibonacci(n)
non_recursive_result = non_recursive_fibonacci(n)
print(f"Recursive Fibonacci({n}) = {recursive_result}")
print(f"Non-Recursive Fibonacci({n}) = {non_recursive_result}")
