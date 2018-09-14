class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d = {}
        d1 = {}
        set_l2 = set(list2)
        for i in range(len(list1)):
            if list1[i] in set_l2:
                temp = list2.index(list1[i]) + i
                d[i] = temp
                d1[i] = list1[i]
        key_min = min(d, key = d.get)
        return [d1[k] for k,v in d.items() if v == d[key_min]]
            

                    