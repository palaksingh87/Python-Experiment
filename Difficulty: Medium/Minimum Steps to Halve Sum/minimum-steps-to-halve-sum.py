class Solution:
    def minOperations(self, arr):
        import heapq
        tmp=[-x for x in arr]
        heapq.heapify(tmp)
        cur=ini=sum(arr)
        cnt=0
        while cur>ini/2:
            cnt+=1
            cur+=tmp[0]/2
            heapq.heapreplace(tmp,tmp[0]/2)
        return cnt


