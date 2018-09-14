"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        d_impo = {}
        d_sub = {}
        for i in employees:
            # print(i.importance)
            d_impo[i.id] = i.importance
            d_sub[i.id] = i.subordinates
        s = set()
        # for i in employees:
        s.add(id)
        _sum = 0
        # print(d_impo)
        while len(s):
            temp = s.pop()
            _sum += d_impo[temp]
            for i in d_sub[temp]:
                s.add(i)
        return _sum
                
                
            
        