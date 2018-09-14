class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        flag = 0
        leng = min(len(a),len(b))
        m_leng = max(len(a),len(b))
        
        s = ""
        for _ in range(m_leng-leng): s += "0"
        if len(a)<len(b):
            s += a
            a = s
        else: 
            s += b
            b = s
        
        l = ""
        for i in range(m_leng-1,-1,-1):
            l += str((int(a[i]) + int(b[i]) + flag) % 2)
            if int(a[i])+int(b[i])+flag >= 2:
                flag = 1
            else:
                flag = 0
        if flag == 1: l += "1"
            
        return l[::-1]
        