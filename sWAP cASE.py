def swap_case(s):
    str1 = ""
    for ch in s:
        if ch.isupper():
            str1 += ch.lower()
        elif ch.islower():
            str1 += ch.upper()
        else:
            str1 += ch
    return str1

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)