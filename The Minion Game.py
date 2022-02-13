def minion_game(string):
    kevin_score = 0
    stuart_score = 0
    l =  len(string)
    for i in range(l):
        if string[i] in 'AEIOU':
            kevin_score += l - i
        else:
            stuart_score += l - i
    if kevin_score > stuart_score:
        print('Kevin', kevin_score)
    elif stuart_score>kevin_score :
        print('Stuart', stuart_score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)