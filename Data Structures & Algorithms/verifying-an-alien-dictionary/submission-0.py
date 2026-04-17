class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # we have to check if the second word is prefix of first word and if yes then return False
        # we need to find the differentiation character in the word pair

        order_index = {c : i for i,c in enumerate(order)}

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            for j in range(len(w1)):
                if j == len(w2):
                    return False
                
                if w1[j] != w2[j]:
                    if order_index[w1[j]] > order_index[w2[j]]:
                        return False
                    break
        
        return True