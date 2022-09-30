import sys

'''
Tic-tac-toe Game
Katherine Cendana
'''

print('\nWelcome to Tic-tac-toe Game')
print('-'*30)

instruction = """
This is the sample Gameboard:

+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
1. Enter a number 1-9 to put your sign("X", "O").
2. Player one will take the first turn.
"""

num_list = []
for i in range(9):
  num_list.append(i+1)

def print_GameBoard():
  board = f"""
   +---+---+---+
   | {num_list[0]} | {num_list[1]} | {num_list[2]} |
   +---+---+---+
   | {num_list[3]} | {num_list[4]} | {num_list[5]} |
   +---+---+---+
   | {num_list[6]} | {num_list[7]} | {num_list[8]} |
   +---+---+---+
  """
  print(board)

index_list = []
def take_input(player_name):
    X = int(input(f'{player_name}, Please enter a number(1-9): '))
    while X >= 10 or X <= 0:
      print('\nThe number you entered is out of range.')
      X = int(input(f'{player_name}, Please enter a number(1-9): '))

    if X < 10 and X > 0:
      if X in index_list:
        print('The number you entered has already been taken.')
        X = int(input(f'{player_name}, Please enter a number(1-9): '))
      else: 
        index_list.append(X)
        return X
   
      

def check_Winner(player_One, player_Two):
  if (num_list[0] == num_list[1] == num_list[2] == "X" or
  num_list[3] == num_list[4] == num_list[5] == "X" or
  num_list[6] == num_list[7] == num_list[8] == "X" or
  num_list[0] == num_list[3] == num_list[6] == "X" or
  num_list[1] == num_list[4] == num_list[7] == "X" or
  num_list[2] == num_list[5] == num_list[8] == "X" or
  num_list[0] == num_list[4] == num_list[8] == "X" or
  num_list[2] == num_list[4] == num_list[6] == "X" ):
    print(f'Congratulations, {player_One}. You won!')
    sys.exit()

  elif (num_list[0] == num_list[1] == num_list[2] == "O" or
  num_list[3] == num_list[4] == num_list[5] == "O" or
  num_list[6] == num_list[7] == num_list[8] == "O" or
  num_list[0] == num_list[3] == num_list[6] == "O" or
  num_list[1] == num_list[4] == num_list[7] == "O" or
  num_list[2] == num_list[5] == num_list[8] == "O" or
  num_list[0] == num_list[4] == num_list[8] == "O" or
  num_list[2] == num_list[4] == num_list[6] == "O" ):
    print(f'Congratulations, {player_Two}. You won!')
    sys.exit()


def main():
  play_Again = 'y'
  while play_Again == "y":
    player_One = input('\nPlease enter the name of player one: ').capitalize()
    player_Two = input('Please enter the name of player two: ').capitalize()
    print(f'\nWelcome to Tic-tac-toe Game, {player_One} and {player_Two}. ')

    print(instruction)
    print(f"\n{player_One} is 'X'")
    print(f"{player_Two} is 'O'")
    input('Enter any key to start the game: ')

    print_GameBoard()

    for i in range(9):
      if i % 2 == 0:
        index = take_input(player_One)
        num_list[index - 1] = 'X'
      else:
        index = take_input(player_Two)
        num_list[index - 1] = 'O'
      
      print_GameBoard()
      check_Winner(player_One, player_Two)

    print("It's a draw.")
    play_Again = input('Enter [Y] to play again: ').lower()

main()