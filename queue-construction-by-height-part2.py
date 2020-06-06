class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        new_arr = []
        people = sorted(people, key= lambda x:(-x[0],x[1]))
        for var in people:
            new_arr.insert(var[1],var)
        return new_arr