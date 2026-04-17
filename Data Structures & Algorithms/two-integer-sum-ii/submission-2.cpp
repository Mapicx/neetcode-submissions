class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0;
        int right = 1;
        vector<int> res;
        while(left < numbers.size())
        {
            while(right < numbers.size())
            {
                if((numbers[left] + numbers[right]) == target){
                    res.push_back(left + 1);
                    res.push_back(right + 1);
                    return res;
                }
                right++;
            }
            left++;
            right = left + 1;
        }
        return res;
    }
};
