class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        d = {}
        for i in cpdomains:
            count = int(i.split(' ')[0])
            domain = i.split(' ')[1]
            for i in range(len(domain.split('.'))):
                sub_domain = domain.split('.',i)
                if sub_domain[i] not in d:
                    d[sub_domain[i]] = count
                else:
                    d[sub_domain[i]] += count
        l = []
        for k,v in d.items():
            temp = str(v) + ' ' + str(k)
            l.append(temp)
        return l
            
            