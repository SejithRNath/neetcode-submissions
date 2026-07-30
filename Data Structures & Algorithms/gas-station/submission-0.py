class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            tank = 0
            flag = 1
            j=0
            if cost[i] > gas[i]:
                continue
            tank += gas[i]-cost[i]
            if tank <0:
                continue
            j = (i+1)%len(gas)
            while j!=i:
                tank += gas[j]-cost[j]
                if tank <0:
                    flag =0
                    break
                j = (j+1)%len(gas)
            if flag:
                return j
        return -1
           

        