# Brute force

def isPalindrome(x: int) -> bool:
    a = str(x)[::-1]
    try:
        y = int(a)
    except ValueError:
        return False
    return x == y


# no strings
def is_alindrome(x: int) -> bool:
    if x < 0:
        return False

    rev = 0
    xsave = x

    

