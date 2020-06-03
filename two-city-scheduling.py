class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs = sorted(costs, key= lambda x:x[0]-x[1])
        cost=0
        for var in range(int(len(costs)/2)):
            cost+=costs[var][0]
        for var in range(int(len(costs)/2),len(costs)):
            cost+=costs[var][1]
        return cost