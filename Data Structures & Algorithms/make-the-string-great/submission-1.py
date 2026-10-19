class Solution:
    def makeGood(self, s: str) -> str:
        st = []

        for ch in s:
            if st and (abs(ord(st[-1]) - ord(ch)) == 32):
                st.pop()
            else:
                st.append(ch)
        return "".join(st)

