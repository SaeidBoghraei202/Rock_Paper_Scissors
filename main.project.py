import random

user_win = 0
computer_win = 0
options = ['r', 'p', 's']

while True:

    user_input = input('Type R / P / S or Q to quit : ').lower()

    if (user_input == 'q'): break

    if (user_input not in options): continue
    

    random_no = random.randint(0, 2)

    computer_pick = options[random_no]


    if(user_input == 'r' and computer_pick == 's') or (user_input == 'p' and computer_pick == 'r') or (user_input == 's' and computer_pick == 'p') :
      
       print('You Won')

       user_win += 1


        

    elif(computer_pick == 'r' and user_input == 's') or (computer_pick== 'p' and user_input == 'r') or (computer_pick == 's' and user_input == 'p') :
        
        print('Computer Won')

        computer_win += 1
    
    elif(user_input == computer_pick):
       print('Both are the same!')

print('You :' , user_win)
print('Computer :' , computer_win)

