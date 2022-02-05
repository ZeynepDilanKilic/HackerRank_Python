def alphaNumeric(s):
    for i in range(len(s)):
        if(s[i].isalnum()):
            return True;
            break;
    return False;
        
def alphabetical(s):
    for i in range(len(s)):
        if(s[i].isalpha()):
            return True;
            break;
    return False;

def digits(s):
    for i in range(len(s)):
        if(s[i].isdigit()):
            return True;
            break;
    return False;

def lowerCase(s):
    for i in range(len(s)):
        if(s[i].islower()):
            return True;
            break;
    return False; 
     
def upperCase(s):
    for i in range(len(s)):
        if(s[i].isupper()):
            return True;
            break;
    return False;

if __name__ == '__main__':
    s = input()
    
    print(alphaNumeric(s))
    print(alphabetical(s))
    print(digits(s))
    print(lowerCase(s))
    print(upperCase(s))