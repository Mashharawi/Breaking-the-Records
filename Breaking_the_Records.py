#Record break for high points
def highRecordBrk(b):
    count = 0;
    highScore = runs[0]
    for i in range(0, b):
        if runs[i]>highScore:
            count += 1
            highScore = runs[i]
    return count

#Record break for low points
def lowRecordBrk(b):
    count = 0;
    lowScore = runs[0]
    for j in range(0, b):
        if runs[j] < lowScore:
            count +=  1
            lowScore = runs[j]
    return count

#Generating Score Card
runs = [ ]          #Empty list to update the runs scored
print("Enter the number of games per series")
games = input()
print('Enter runs in each games')
for i in range(0,games):
    a = input()
    runs.append(int(a))

print('Runs scored so far')
print(runs)
print(highRecordBrk(games))
print(lowRecordBrk(games))
