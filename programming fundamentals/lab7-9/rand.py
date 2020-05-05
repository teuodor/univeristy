'''
Created on 24 Mar 2019

@author: Teuodor
'''
if "a" in ["a","b"]:
    assert True
else:
    assert False

l=[1,"a","catelus",3.14]
l.append("Dragos")
l += ["Mihai",3.16]
print(l)