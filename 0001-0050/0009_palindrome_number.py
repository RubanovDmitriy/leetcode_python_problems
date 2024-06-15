# Brute force

def isPalindrome(x: int) -> bool:
    a = str(x)[::-1]
    try:
        y = int(a)
    except ValueError:
        return False
    return x == y

    

