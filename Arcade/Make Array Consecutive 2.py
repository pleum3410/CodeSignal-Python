"""
statues = 6,2,3,8
8-2=6
6-4=2
2+1=3
statues > func > sizes of statues
func = ((max(statues)-min(statues))-len(statues))+1

"""

def solution(statues):
    return ((max(statues)-min(statues))-len(statues))+1
