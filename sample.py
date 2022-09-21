

x = 3
possibleNum = []
num_list = []
for i in range(x*x):
    possibleNum.append(i+1)
print(possibleNum)

for num in range(0, x*x, x):
    num_list.append(possibleNum[num:num+x])
print(num_list)

def printGameBoard():
  for a in range(x):
    print("\n","-----|"*(x))
    print("|", end="")
    for y in range(x):
      print("", num_list[a][y]," "*(2-len(str(num_list[a][y]))), end=" |")
  print("\n","------"*(x))

printGameBoard()
print('change 7 to x')
for k in range(len(possibleNum)):
    if possibleNum[k] == 7:
       possibleNum[k] = "X"
