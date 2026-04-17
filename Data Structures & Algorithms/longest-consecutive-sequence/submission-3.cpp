class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
       if (nums.empty()) return 0;

        sort(nums.begin(), nums.end());
        
        int longest_seq = 1;  
        int seq = 1;  

        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] == nums[i - 1]) continue; 
            
            if (nums[i] == nums[i - 1] + 1) {
                seq++;  
            } else {
                longest_seq = max(longest_seq, seq);  
                seq = 1;  
            }
        }

        return max(longest_seq, seq);  
    }
};
