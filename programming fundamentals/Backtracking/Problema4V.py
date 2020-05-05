'''
Created on 13 Feb 2019

@author: Teuodor
'''
def solution(l):
    for i in range(0,len(l)-1):
        if l[i]>=l[i+1]:
            return False
    return True
def consistent(l):
    if len(l)>0:
        return True
    return False
def bckt(l):
    def rec(l,nr = []):
        if solution(nr):
            return [nr]
        else:
            sol = []
            