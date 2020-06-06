class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        new_arr = []
        people = sorted(people, key= lambda x:(-x[0],x[1]))
        for var in people:
            if len(new_arr) == 0:
                new_arr.append(var)
            elif (len(new_arr) == var[1]):
                new_arr.append(var)
            elif (len(new_arr) > var[1]):
                if new_arr[var[1]][0] > var[0]:
                    new_arr.insert(var[1],var)
                else:
                    new_arr.insert(var[1]+1,var)
            else:
                new_arr.insert(var[1],var)
        return new_arr