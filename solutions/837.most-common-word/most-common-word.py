from collections import Counter
import string
class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        for char in "!?',;.": paragraph = paragraph.replace(char,'')

        counts = Counter(paragraph.lower().split())
        most_freq = counts.most_common()
        print(most_freq)
        for word,count in most_freq:
            if word in banned:
                continue
            else:
                return word