def fibonacci(n):            # slow! repeatedly computation for every sub-problem
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_no_rec(n):
    f = [0, 1, 1]
    if n > 2:
        for i in range(n-2):
            num = f[-1] + f[-2]
            f.append(num)
    return f[n]

print(fibonacci_no_rec(100))