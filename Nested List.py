def sortFuncScore(e):
  return e[1]

def sortFuncName(e):
    try:
        return int(e[1].split(' ')[0])
    except:
        return sorted(e)
        
list_students = []


if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list_students.append([name,score])

list_students.sort(key=sortFuncScore)
min_score =  float(list_students[0][1])
min_score_2 = 0
list_name = []
flag = True
for i in range(len(list_students)):
    score = float(list_students[i][1])
    if(score>min_score and flag):
        min_score_2 = score;
        flag =  False
        list_name.append(list_students[i][0])
    elif(score == min_score_2):
        list_name.append(list_students[i][0])



list_name.sort(key=sortFuncName)

for i in range(len(list_name)):
    print(list_name[i])
