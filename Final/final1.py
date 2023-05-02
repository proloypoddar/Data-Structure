def check_diff_property(s):
    s = s.lower()
    n = len(s)
    for i in range(n // 2):
        if abs(ord(s[i]) - ord(s[n - i - 1])) != (2 * i + 1):
            return False
    return True
print(check_diff_property("a5fKge3B")) # True
print(check_diff_property("5py83xn6")) # False
