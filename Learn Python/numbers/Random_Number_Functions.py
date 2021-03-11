# -*- coding: utf-8 -*-
#Random Number Functions
#choice(seq)
'''A random item from a list, tuple, or string. '''
import random
print ("returns a random number from range(100) : ",random.choice(range(100)))
print ("returns random element from list [1, 2, 3, 5, 9]) : ", random.choice([1, 2, 3, 5, 9]))
print ("returns random character from string 'Hello World' : ", random.choice('Hello World'))
#randrange ([start,] stop [,step]) 
'''
A randomly selected element from range(start, stop, step). '''
# randomly select an odd number between 1-100  
print ("randrange(1,100, 2) : ", random.randrange(1, 100, 2)) 
# randomly select a number between 0-99  
print ("randrange(100) : ", random.randrange(100)) 
#random()
'''A random float r, such that 0 is less than or equal to r and r is less than 1.'''
# First random number 
print ("random() : ", random.random()) 
# Second random number 
print ("random() : ", random.random())
#seed([x])
'''Sets the integer starting value used in generating random numbers.
 Call this function before calling any other random module function.
 Returns None. '''
random.seed()
print ("random number with default seed", random.random()) 
random.seed(10) 
print ("random number with int seed", random.random()) 
random.seed("hello",2) 
print ("random number with string seed", random.random()) 
random.seed() 
print ("random number with default seed", random.random()) 
random.seed(10)
print ("random number with int seed", random.random()) 
random.seed("hello",2) 
print ("random number with string seed", random.random()) 
 #shuffle(lst)
'''Randomizes the items of a list in place. Returns None.'''
list = [20, 16, 10, 5]; 
print('Initial List: ',list)
random.shuffle(list) 
print ("Reshuffled list : ",  list) 
random.shuffle(list) 
print ("Reshuffled list : ",  list) 
random.shuffle(list)
print('Shuffled List: ',list)
#uniform(x,y)
'''A random float r, such that x is less than or equal to r and r is less than y. '''
print ("Random Float uniform(5, 10) : ",  random.uniform(5, 10)) 
print ("Random Float uniform(7, 14) : ",  random.uniform(7, 14))
