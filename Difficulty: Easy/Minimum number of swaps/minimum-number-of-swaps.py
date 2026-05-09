class Solution:
    def minSwaps(self, s1, s2):
        # code here 
        count_A = 0
        count_b = 0
        for i in range(len(s1)):
            if (s1[i] == '0') and (s2[i] == '1'):
                count_A +=1
            if (s1[i] == '1') and (s2[i] == '0'):
                count_b +=1
                
        ans = count_A//2 + count_b // 2
        if (count_A%2 == 0) and (count_b%2==0):
            return ans
        elif (count_A + count_b)%2 ==0 :
            return ans+2
        return -1