'''
Created on 4 Feb 2019

@author: Teuodor
'''
import random
def random_tv_show(dict):
    '''
    A function which return the key of a random tv_show
    :input: dict - a dictionary of tv shows
    :return: a key of a random tv show
    '''
    a = random.randint(6,200)
    a = a%(len(dict))
    ind = 0
    for i in dict.keys():
        if a == ind:
            return i
        ind = ind + 1
        