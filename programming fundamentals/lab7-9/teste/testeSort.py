'''
Created on 20 Dec 2018

@author: Teuodor
'''
from utils.helper import comb_sort, insertion_sort, rand_int
class TestSort:
    def test(self,list):
        list2 = comb_sort(list)
        list3 = insertion_sort(list)
        assert list2 == sorted(list)
        assert list3 == sorted(list)
    def test100(self):
        for i in range(100):
            nr=rand_int()
            list=[]
            for j in range(nr):
                list.append(rand_int())
            
            assert comb_sort(list) == sorted(list)
            assert insertion_sort(list) == sorted(list)
    
test = TestSort()
test.test([13,18,2,5,9])
test.test([502,0,304,22])
test.test([4,2012,45,32])
test.test([23,45,42,32])
test.test([1,2,3,4,5,0])
test.test100()