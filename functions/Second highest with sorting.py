# Finding the second runner up score for N players.
N = int(input("enter the number of players:"))
score=[]
for i in range(N):
    s = int(input("enter the score:"))
    score.append(s)
score.sort(reverse = True)


for i in range(len(score)-1):
    if score[i]>score[i+1]:
        print(f'the second runner up socre is {score[i+1]}')
        break

    if i >= len(score)-1:
        print(f' all scores are equal')
    
    

if len(score)==1:
    print(f'only one player and score is {score[0]}')









