# Name = Vipan Kumar
# GitHub user name = @VipanKumar01

""" 
That have some Error I can't find Out. So Please Help me for solve this Questions
Samples =>

For a = [1, 2, 3] and b = [1, 2, 3], the output should be
solution(a, b) = true.

The arrays are equal, no need to swap any elements.

For a = [1, 2, 3] and b = [2, 1, 3], the output should be
solution(a, b) = true.

We can obtain b from a by swapping 2 and 1 in b.

For a = [1, 2, 2] and b = [2, 1, 1], the output should be
solution(a, b) = false.

Any swap of any two elements either in a or in b won't make a and b equal.

"""

def solution(a, b):
    a.sort()
    b.sort()

    temp1 = set(a)
    temp2 = set(b)
    
    if a!=b or temp1!=temp2 :
        return False
    elif a == b or temp1 == temp2:
        return True
            
        
# --HappyCode--
