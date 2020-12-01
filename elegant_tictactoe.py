def check_winar(p):
    for i in range(0,3):
        if p[i][0]==p[i][1]==p[i][2]=="x" or p[0][i]==p[1][i]==p[2][i]=="x" or p[i][0]==p[i][1]==p[i][2]=="o" or p[0][i]==p[1][i]==p[2][i]=="o":
            return 1
    if  p[0][0]==p[1][1]==p[2][2]=="x" or p[0][2]==p[1][1]==p[2][0]=="x" or p[0][0]==p[1][1]==p[2][2]=="o" or p[0][2]==p[1][1]==p[2][0]=="o":
        return 1
    else:
        return 0

def play(p,ch):
    statement=1
    while statement==1:
        try:
            q = int(input("Enter row: "))
            r = int(input("Enter column: "))
        except:
            print("Only numbers can be accepted as input")
            continue
        if q not in range(0,3) or r not in range(0,3) or p[q][r]!=' ':
            print("Choose another position")
        else:
            statement=0
    if ch=='x':
        p[q][r]="x"
    elif ch=='o':
        p[q][r] = "o"
    return p

p=[[" "," "," "],[" "," "," "],[" "," "," "]]
print("\n",p[0],"\n",p[1],"\n",p[2])
print("Player 1 is 'x' and player 2 is 'o'\nRows and Columns are both numbered from 0 to 2")
while ' ' in p[0] or ' ' in p[1] or ' ' in p[2]:
    p=play(p,"x")
    print("\n",p[0],"\n",p[1],"\n",p[2])
    if check_winar(p)==1:
        print("Player 1 wins!!!")
        break
    if ' ' in p[0] or ' ' in p[1] or ' ' in p[2]:
        p=play(p,"o")
        print("\n",p[0],"\n",p[1],"\n",p[2])
    if check_winar(p)==1:
        print("Player 2 wins!!!")
        break
print("Game over!")