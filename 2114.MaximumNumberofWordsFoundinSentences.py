class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count=0
        for i in sentences:
            x=i.count(' ')+1
            if x>count:
                count=x
        return count
