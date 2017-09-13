import math, string, itertools, fractions, heapq, collections, re, array, bisect


class GreaterGameDiv2:
    def calc(self, snuke, sothe):
        score = 0
        for i in range(len(snuke)):
            if snuke[i] > sothe[i]:
                score+=1
        return score
        print(score)
obj=GreaterGameDiv2
obj.calc({1,3},{4,2},{1.3})