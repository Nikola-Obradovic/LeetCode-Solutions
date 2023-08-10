class Solution:




    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        total_cost = 0
        current_gas = 0
        start = 0
        
        for x in range(len(gas)):
            total_gas += gas[x]
            total_cost += cost[x]
            current_gas += gas[x] - cost[x]
            
            if current_gas < 0:
                current_gas = 0
                start = x + 1
                
        if total_gas < total_cost:
            return -1
        else:
            return start

        
