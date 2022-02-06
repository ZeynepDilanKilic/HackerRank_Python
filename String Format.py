def print_formatted(number):
    nl = len(bin(number)[2:])
   
    for i in range(1,number+1):
        print(str(i).rjust(nl,' '),end=" ")
        print(oct(i)[2:].rjust(nl,' '),end=" ")
        print(((hex(i)[2:]).upper()).rjust(nl,' '),end=" ")
        print(bin(i)[2:].rjust(nl,' '),end=" ")
        print("")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)