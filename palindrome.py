def is_palindrome(num):
    copy = num
    rev = 0

    while num > 0:
        ld = num % 10
        rev = rev * 10 + ld
        num = num//10

    return rev==copy

num = int(input("Enter a number: "))
print(is_palindrome(num))