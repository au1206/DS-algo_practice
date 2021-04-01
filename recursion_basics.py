

# write a recursive function to print nth fibonachi number
def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n-1)+fib(n-2)


# write a recursive function to calculate n!
def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)


# write a recursive function to print string in reverse order
def str_rev(str):
    if len(str)==0:
        return
    temp = str[0]
    str_rev(str[1:])
    print(temp, end='')


if __name__ == '__main__':
    n = 5
    print("Fibonachi Sequence")
    for elem in range(n+1):
        print(fib(elem))

    print("\nFactorial")
    for elem in range(n+1):
        print(fact(elem))

    print("\n String Reverse")
    str_rev("Akshay is awesome")



