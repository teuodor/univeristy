'''
Created on 22 Nov 2018

@author: Teuodor
'''
import random,string,time
def cmp(x,y):
    if x<y:
        return -1
    elif x==y:
        return 0
    return 1
def rand_int():
    '''
    Returns a random number between 6 and 200
    '''
    return random.randint(6,200)
def rand_string(length):
    '''
    Returns a random string
    '''
    letters=string.ascii_letters
    return random.choice(string.ascii_uppercase)+''.join(random.choice(letters) for letter in range(length))
def compare_hours(hour1,hour2):
    '''
    Returns if hour1>hour2
    '''
    t1 = time.strptime(hour1,'%H:%M')
    t2 = time.strptime(hour2,'%H:%M')
    if t1>t2:
        return True
    
def insertion_sort(list,*,key = lambda x:x, reverse = False,cmp = cmp):
    '''
    Function to implement insertion sort
    '''
    
    for i in range(1,len(list)):
        pivot = list[i]
        j = i-1
        
        while j>=0 and cmp(key(pivot), key(list[j])) < 0:
            list[j+1] = list[j]
            j -= 1
            
        list[j+1] = pivot
    
    if reverse == False:
        return list
    elif reverse == True:
        return list[::-1]
    
def getNextGap(gap):
    gap = (gap*10)//13
    if gap < 1:
        return 1
    return gap

def comb_sort(list,*,key = lambda x:x,reverse = False,cmp = cmp):
    '''
    Function to implement comb sort
    '''
    n = len(list)
    gap = n
    
    swapped = True
    
    while gap != 1 or swapped == True:
        gap = getNextGap(gap)
        swapped = False
        for i in range(0,n-gap):
            if cmp(key(list[i]),key(list[i+gap]))>0:
                list[i],list[i+gap] = list[i+gap],list[i]
                swapped = True
                
    if reverse == False:
        return list
    elif reverse == True:
        return list[::-1]




