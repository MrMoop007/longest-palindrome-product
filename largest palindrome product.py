def is_palindrome(n):
    num = str(n)
    length = len(num)
    if length%2 == 1:
        return False
    return num[:length//2] == num[length//2:][::-1]

best_palindrome = 0
for i in range(100, 999):
    for j in range(100, 999):
        product = i*j
        if is_palindrome(product):
            if product > best_palindrome:
                best_palindrome = product

print(best_palindrome)