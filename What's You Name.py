def print_full_name(first, last):
    # Write your code here
    str1 ="Hello "
    str2 = "You just delved into python."
    print(str1 + first +" " + last +"! "+str2)

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)