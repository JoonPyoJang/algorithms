input = "abcba"


def is_palindrome(string):
    if len(string) <=1:
        return True
    if string[0] != string[-1]:
        return False
    print(string)
    return is_palindrome(string[1:-1])


print(is_palindrome(input))