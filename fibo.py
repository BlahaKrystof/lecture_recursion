def recursive_nth_fibo(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_nth_fibo(n - 1) + recursive_nth_fibo(n - 2)




def main():
    n = int(input("Zadej pořadí prvku fibonacciho posloupnosti: "))
    print(recursive_nth_fibo(n))
    fib_list = []
    for m in range(n + 1):
        fib_list.append(recursive_nth_fibo(m))

    print(fib_list)

if __name__ == "__main__":
    main()
