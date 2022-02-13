def print_rangoli(size):
    w =  size*4-3
    chr_array = ''
    for i in range(1,size+1):
        for j in range(i):
            chr_array += chr(96+size-j)
            if len(chr_array) < w:
                chr_array +='-'
        for k in range(i-1,0,-1):
            chr_array += chr(97+size-k)
            if len(chr_array) < w:
              chr_array +='-'
        print(chr_array.center(w,'-'))
        chr_array =''      
    for i in range(size-1,0,-1):
        for j in range(0,i):
            chr_array += chr(96+size-j)
            if len(chr_array) < w :
                chr_array += '-'
        for k in range(i-1,0,-1):
            chr_array += chr(97+size-k)
            if len(chr_array) < w :
                chr_array += '-'
        print(chr_array.center(w,'-'))
        chr_array = ''
     


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)