
def test_primeNumber():
    n =15
    # prime numbers are greater than 1
    if n > 1:
        # check for factors
        for i in range(2, n):
            if (n % i) == 0:
                print(n, "is not a prime number")
                break

        else:
            print(n, "is a prime number")

    # if input number is less than or equal to 1, it is not prime
    else:
        print(n, "is not a prime number")


def test_ArmstrongNumber():
    n = 153
    origin = n
    nstr = str(n)

    sum = 0

    for i in range(len(nstr)):
        productsum = (int(nstr[i]) * int(nstr[i]) * int(nstr[i]))
        sum = sum + productsum

    if sum == origin:
        print(n,"Given Number is Amstrong")

    else:
        print(n,"Given Number is Not Amstrong")


def test_palindromeNumber():
    a = "121"
    b = a[::-1]
    if a == b:
        print(a,"Is palindrome")

    else:
        print(a,"Is Not a Palindrome")

