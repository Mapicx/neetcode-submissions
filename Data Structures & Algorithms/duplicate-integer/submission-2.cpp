class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> st;
        for(auto it = nums.begin();it != nums.end();it++)
        {
            st.emplace(*it);
        }
        if(st.size() < nums.size())
            return true;
        return false;    
    }
};
