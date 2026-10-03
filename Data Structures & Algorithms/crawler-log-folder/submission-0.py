class Solution:
    def minOperations(self, logs: List[str]) -> int:
        st = []
        for op in logs:
            if op == "../":
                if st:
                    st.pop()
            elif op == "./":
                continue
            else:
                st.append(op)
        
        return len(st)