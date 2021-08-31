def checkingDiagonally(total_play):
    set_a=set()
    for i in range(3):
        for j in range(3):
            if i==j:
                set_a.add(total_play[i][j])
    if len(set_a)==1:
            if "X" in set_a:
                return "Anjali Wins";
            else:
                return "Abhinav Wins"
    else:
        set_a=set()
        set_a.add(total_play[0][2])
        set_a.add(total_play[1][1])
        set_a.add(total_play[2][0])
        if len(set_a)==1:
            if "X" in set_a:
                return "Anjali Wins";
            else:
                return "Abhinav Wins"

#while checking columns im transposing the matrix and again calling checking rows function
def checkingColumns(total_play):
    new_matrix=[]
    for i in range(3):
        sub_matrix=[]
        for j in range(3):
            sub_matrix.append(total_play[j][i])
        new_matrix.append(sub_matrix)
    return checkRows(new_matrix)


def checkRows(total_play):
    for sub_list in total_play:
        set_a=set(sub_list)
        if len(set_a)==1:
            if "X" in set_a:
                return "Anjali Wins";
            else:
                return "Abhinav Wins"
                
total_play=[]
for i in range(3):
    input1=input().split()
    total_play.append(input1)
total_play2=total_play


#Checking rows 
checkingRows=checkRows(total_play);

if checkingRows:
    print(checkingRows)
else:
    checkingColumns=checkingColumns(total_play);
    if checkingColumns:
        print(checkingColumns);
    else:
        checkingDiagonal=checkingDiagonally(total_play)
        if checkingDiagonal:
            print(checkingDiagonal)
        else:
            print("Tie")