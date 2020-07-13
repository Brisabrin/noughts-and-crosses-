#first time loading the program press 1 
from random import randint
import time
import json
#create a user menu 
menu="""
********************
        MENU
********************
1. Choose board of size 
2. View best time 
3. View previous games 
4. View average win time 
5. View specific user 
6. Quit

"""
all_users={}
array=[]
state=""
result=""
#for username + time

try:
  string_data = open("store.json", "r").read()
  
except FileNotFoundError:
  write_file=json.dumps(all_users)
  f = open("store.json", "w")
  f.write(write_file)
  f.close()
#file with time record only 
try:
  with open('time.json', 'r') as filehandle:  
    basicList = json.load(filehandle)
    
except FileNotFoundError:
  with open('time.json', 'w') as filehandle:  
    json.dump(array,filehandle)

def check_win(state):
    
  global result
  if state=="x":
    if player=="X":
      result="player"
    else:
      result="computer"
    return True

  elif state=="o":
    if player=="O":
      result="player"
    else:
      result="computer"
    return True
def board_design():
  board_design_index=0
  while board_design_index<=board_index:
      
    if (board_design_index+1)%size_input==0 and board_design_index!=0 and board_design_index!=board_index:
      print(" {} \n".format(board[board_design_index]),end='')
      print("-----"*(size_input))
    elif board_design_index==board_index:
      print("{}".format(board[board_index]))
    else:
      print(" {}  |".format(board[board_design_index]),end='')
    board_design_index+=1
def game_player():
    
  player_track=True
  while player_track:
    try:
      user_input=int(input("type a number from 1-{}\n".format(board_index+1)))
      if user_input in range(1,board_index+2) and board[user_input-1]==" ":
        board[user_input-1]=player
        player_track=False
      else:
        print("The number you entered {} is already taken".format(user_input))
    except ValueError:
      print("invalid number")
  board_design()
  print("\n")
def game_computer():
  computer_track=True
  while computer_track:
    random_num=randint(0,board_index)
    if board[random_num]==" ":
      board[random_num] = computer
      computer_track=False
  board_design()
  print("\n") 

board = []

def record_time(user):
    
  string_data = open("store.json", "r").read()
  ex_file1=json.loads(string_data)
  if user not in ex_file1:
    ex_file1[user] = []
  ex_file1[user].append(total)
  record_file= json.dumps(ex_file1)
  
  f=open("store.json","w")
  f.write(record_file)
  f.close()
  
  with open('time.json', 'r') as filehandle:
      
    e_file1 = json.load(filehandle)
  e_file1.append(total)
  with open('time.json', 'w') as filehandle:
      
    json.dump(e_file1,filehandle)
  
print(menu)
menu_input=input()
if menu_input=="1":
  sizeinput=True
  while sizeinput:
    try: 
      size_input=int(input("Enter a size board the minimum is 3"))
      if size_input>=3:
        sizeinput=False
      else:
        print("number out of range")
    except ValueError:
      print("Enter a number")
  board_add_item=0
  board_index=(size_input**2)-1
  while board_add_item<=(board_index):
    board.append(" ")
    board_add_item+=1
  gameturn_count=0
  game_track=True

  username_input=input("Type in your username")
 
  yesno=True
  while yesno:
    user_input=input("Do you like to go first")
    if user_input.lower().strip()=="yes":
      player="X"
      computer="O"
      board_design()
      yesno=False
    elif user_input.lower().strip()=="no":
      player="O"
      computer="X"
      yesno=False
    else:
      print("type yes or no")
    
  print("\nPlays noughts and crosses by getting three in a row, column or diagonal")
  t0 = time.time()
  while game_track:
      
    if player=="X":
        
      if gameturn_count%2==0:
        game_player()
      else:
        game_computer()
        
    elif player=="O":
        
      if gameturn_count%2!=0:
        game_player()
        
      else:
        game_computer()
    #check row
    for y in range(0, size_input**2, size_input):
        
      if all([board[x]=="X" for x in range(y, y+size_input)]):
        state="x"
        
      elif all([board[x]=="O" for x in range(y, y+size_input)]):
          
        state="o"
    
    #check column 
    a=(size_input**2-size_input)+1
    for y in range(0,size_input):
        
      if all([board[x]=="X" for x in range(y,y+a,size_input)]):
        state="x"
        
      elif all([board[x]=="O" for x in range(y,y+a,size_input)]):
        state="o"
        
    if all([board[x]=="X" for x in range(0,board_index+1,size_input+1)]):
      state = "x"
      
    elif all([board[x]=="O" for x in range(0,board_index+1,size_input+1)]):
      state = "o"
      
    if all([board[x]=="X" for x in range(size_input-1,board_index-(size_input-1)+1,size_input-1)]):
      state="x"
      
    elif all([board[x]=="O" for x in range(size_input-1,board_index-(size_input-1)+1,size_input-1)]):
      state="o"
      
    if check_win(state):
      game_track=False
      
    if board.count(" ")==0:
        
      if check_win(state):
        game_track=False
        
      else:
        print("This round is a draw")
        game_track=False
        
    gameturn_count+=1

  t1 = time.time()
  total = t1-t0
  if result=="player":
    record_time(username_input)
  print("{} won!".format(result))

else:
  string_data = open("store.json", "r").read()
  
  load = json.loads(string_data)
  with open('time.json', 'r') as filehandle:  
    time_array = json.load(filehandle)
    
  if menu_input=="2":
    print(min(time_array))
    #view previous games
    
  elif menu_input=="3":
    for i in time_array:
      for j in load:
        for b in load[j]:
          if b==i:
            print("{}:{}\n".format(j,round(i,2)))
  #view average time
  elif menu_input=="4":
    print(sum(time_array)/len(time_array) )
    
      #view specific user
  elif menu_input=="5":
    specific=input("Type in the username:")
    
    if specific in load:
      print("{}: {}".format(specific,load[specific]))
    else:
      print("username not found")
  else:
    print("the end")


