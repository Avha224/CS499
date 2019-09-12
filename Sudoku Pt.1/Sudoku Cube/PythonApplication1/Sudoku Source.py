import numpy as np
import random


top   = [['9^', '7^', '1^'],['2^', '4^', '8^'],['5^', '3^', '6^']] #Starting position
left  = [['3<', '8<', '7<'],['2<', '1<', '9<'],['5<', '6<', '4<']]
front = [['1-', '5-', '2-'],['4-', '6-', '3-'],['7-', '8-' ,'9-']]
right = [['3>', '9>', '7>'],['6>', '1>', '5>'],['8>', '2>', '4>']]
bot   = [['1.', '4.', '2.'],['8.', '7.', '3.'],['6.', '9.', '5.']]
back  = [['4,', '3,', '6,'],['7,', '5,', '1,'],['9,', '2,', '8,']]

print('This is the correct key for the puzzle cube')

uper = np.array(top)
print(" \t\t" +str(uper).replace('\n','\n\t\t')) #Print out top array

middle1 = np.array(left)
middle2 = np.array(front)
middle3 = np.array(right)
mid = np.concatenate((middle1,middle2,middle3),1) #Print middle of array (3 block section)

print(" " +str(mid).replace('\n','\n '))

lower = np.array(bot)
print(" \t\t" +str(lower).replace('\n','\n\t\t')) #Print lower array

backface = np.array(back)
print(" \t\t" +str(backface).replace('\n','\n\t\t')) #Print back face array
print('\n')




def pick_side (): #Pick which side will be considered the front

    list = ['top', 'left', 'front', 'right', 'bot', 'back']
    x = random.choice(list)

    return x

def clockwise(starting_face): #Clockwise turn
    print('clk')
    
    if starting_face =='top':
         return 'top'
    elif starting_face =='left':
         return 'left'
    elif starting_face =='front':
         return 'front'
    elif starting_face =='right':
         return 'right'
    elif starting_face =='bot':
         return 'bot'
    else:  
        return 'back'

def counter_clk(starting_face): #Counter clockwise turn
    print('c_clk')
    

    if starting_face =='top':
        return 'top'
    elif starting_face =='left':
         return 'left'
    elif starting_face =='front':
         return 'front'
    elif starting_face =='right':
         return 'right'
    elif starting_face =='bot':
         return 'bot'
    else:  
        return 'back'

def turn(starting_face, which_way): #Decide if clockwise or counter clockwise turn

    if which_way =='clockwise':
        move = clockwise(starting_face)
        return move
    else:
        move = counter_clk(starting_face)
        return move

def rotate_clk(times, nfront, nleft, nright, ntop, nbot, nback): #Rotate the main face 90 degrees and adjust the top row of each effected face for each time the action is performed
    upper = np.array(ntop)
    middle1 = np.array(nleft)
    middle2 = np.array(nfront)
    middle3 = np.array(nright)
    lower = np.array(nbot)
    backface = np.array(nback)
    

     # Run the randomizer for x turns
    for i in range(0, times):        
        
           middle2 = np.rot90(middle2,1,(1,0))    
           hold1 = middle3[0,0]
           hold2 = middle3[0,1]
           hold3 = middle3[0,2]
               
           middle3[0,0] = upper[0,0]
           middle3[0,1] = upper[0,1]
           middle3[0,2] = upper[0,2]
           upper[0,0] = middle1[0,0]
           upper[0,1] = middle1[0,1]
           upper[0,2] = middle1[0,2]
           middle1[0,0] = lower[0,0]
           middle1[0,1] = lower[0,1]
           middle1[0,2] = lower[0,2]
           lower[0,0] = hold1
           lower[0,1] = hold2
           lower[0,2] = hold3
   
           print(" \t\t" +str(upper).replace('\n','\n\t\t')) #Print out top array

        
           mid = np.concatenate((middle1,middle2,middle3),1) #Print middle of array (3 block section)

           print(" " +str(mid).replace('\n','\n '))

       
           print(" \t\t" +str(lower).replace('\n','\n\t\t')) #Print lower array

           print(" \t\t" +str(backface).replace('\n','\n\t\t')) #Print back face array
           print('\n')
      
           
       


    return(upper, middle1, middle2, middle3, lower, backface)

def rotate_counter(times, nfront, nleft, nright, ntop, nbot, nback):
    upper = np.array(ntop)
    middle1 = np.array(nleft)
    middle2 = np.array(nfront)
    middle3 = np.array(nright)
    lower = np.array(nbot)
    backface = np.array(nback)

    
    for i in range(0, times):

            middle2 = np.rot90(middle2,1,(0,1))
            hold1 = upper[0,0]
            hold2 = upper[0,1]
            hold3 = upper[0,2]

            upper[0,0] = middle3[0,0]
            upper[0,1] = middle3[0,1]
            upper[0,2] = middle3[0,2]
            middle3[0,0] = lower[0,0]
            middle3[0,1] = lower[0,1]
            middle3[0,2] = lower[0,2]
            lower[0,0] = middle1[0,0]
            lower[0,1] = middle1[0,1]
            lower[0,2] = middle1[0,2]
            middle1[0,0] = hold1
            middle1[0,1] = hold2
            middle1[0,2] = hold3



            print(" \t\t" +str(upper).replace('\n','\n\t\t')) #Print out top array

        
            mid = np.concatenate((middle1,middle2,middle3),1) #Print middle of array (3 block section)

            print(" " +str(mid).replace('\n','\n '))

       
            print(" \t\t" +str(lower).replace('\n','\n\t\t')) #Print lower array

            print(" \t\t" +str(backface).replace('\n','\n\t\t')) #Print back face array
            print('\n')





    return(upper, middle1, middle2, middle3, lower, backface)

print('\nHow many times would you like to turn the cube?')
print('Please enter a number')
turns = int(input())
print(turns)

for i in range (0,turns):
       starting_face = pick_side() #Initiate a starting face
       way = ['clockwise','counter_clk']
       which_way = random.choice(way)
       print(which_way)
       
       x = turn(starting_face,which_way) #Find which way it will turn
       print(x)

       times = random.randint(1,3)
       print(times)


       upper = top
       middle1 = left
       middle2 = front
       middle3 = right
       lower = bot
       backface = back


       if starting_face == 'front':    #Adjust starting point based on starting face selected
            if which_way == 'clockwise':
               upper, middle1, middle2, middle3, lower, backface = rotate_clk(times, front, left, right, top, bot, back) 
            else:
                upper, middle1, middle2, middle3, lower, backface = rotate_counter(times, front, left, right, top, bot, back)
       elif starting_face == 'left':
            if which_way == 'clockwise':
                upper, middle1, middle2, middle3, lower, backface = rotate_clk(times, left, back, front, top, bot, right) 
            else:
                 upper, middle1, middle2, middle3, lower, backface = rotate_counter(times, left, back, front, top, bot, right)
       elif starting_face == 'right':
            if which_way == 'clockwise':
                 upper, middle1, middle2, middle3, lower, backface = rotate_clk(times, right, front, back, top, bot, left) 
            else:
                upper, middle1, middle2, middle3, lower, backface = rotate_counter(times, right, front, back, top, bot, left)
       elif starting_face == 'top':
            if which_way == 'clockwise':
                 upper, middle1, middle2, middle3, lower, backface = rotate_clk(times, top, left, right, back, front, bot) 
            else:
               upper, middle1, middle2, middle3, lower, backface = rotate_counter(times, top, left, right, back, front, bot) 
       elif starting_face == 'bot':
            if which_way == 'clockwise':
                 upper, middle1, middle2, middle3, lower, backface= rotate_clk(times, bot, left, right, front, back, top) 
            else:
                upper, middle1, middle2, middle3, lower, backface = rotate_counter(times, bot, left, right, front, back, top)
       elif starting_face == 'back':
            if which_way == 'clockwise':
                upper, middle1, middle2, middle3, lower, backface = rotate_clk(times, back, right, left, top, bot, front) 
            else:
                 upper, middle1, middle2, middle3, lower, backface = rotate_counter(times, back, right, left, top, bot, front)

       
       



     
    

