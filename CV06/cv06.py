def faktorial(*args):
    def fakt(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n*fakt(n-1)
    for num in args:
        if num < 0:
            print("Nejde")
        else:
            print(f"faktorial cisla {num} je {fakt(num)}")

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2)+fib(n-1)

print(fib(10))
faktorial(1,5,8,15,-5)