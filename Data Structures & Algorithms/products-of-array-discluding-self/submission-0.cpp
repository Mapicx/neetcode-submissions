class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        if (nums.empty())
            return {}; // ✅ Edge case: Empty input

        int n = nums.size();
        vector<int> res(n, 1); // ✅ Ensure proper vector size

        long long prefix = 1, postfix = 1; // ✅ Prevent overflow

        for (int i = 0; i < n; i++) {
            res[i] = prefix;
            prefix *= nums[i];
        }

        for (int i = n - 1; i >= 0; i--) {
            res[i] *= postfix;
            postfix *= nums[i];
        }

        return res;
    }
};
