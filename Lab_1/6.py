def fibonacci_ser(n):
    fib_ser = [0, 1]
    for _ in range(2, n):
        fib_ser.append(fib_ser[-1] + fib_ser[-2])
    return fib_ser[:n]

num = int(input("Enter the number of terms: "))
print("Fibonacci series:", fibonacci_ser(num))