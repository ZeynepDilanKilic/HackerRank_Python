def solve(s):
    string_arr = s.split(' ')
    l =  len(string_arr)

    string =""
    for i in range(l):
        if string_arr [i] != '':
            string_arr[i] =string_arr[i].replace(string_arr[i][0],string_arr[i][0].upper(),1)
            string += string_arr[i] + ' '
        else:
            string += ' '
    return string

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()