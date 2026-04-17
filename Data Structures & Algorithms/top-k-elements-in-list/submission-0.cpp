class Solution {
public:
    static bool comp(pair<int, int> p1, pair<int, int> p2)
    {
        return p1.second > p2.second;  // Sort by frequency in descending order
    }

    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> mpp;
        for (int num : nums) {
            mpp[num]++;
        }

        vector<pair<int, int>> freqVec;
        for (auto& entry : mpp) {
            freqVec.push_back(entry);
        }

        // Pass the static comparator function directly
        sort(freqVec.begin(), freqVec.end(), comp);

        vector<int> result;
        for (int i = 0; i < k; i++) {
            result.push_back(freqVec[i].first);
        }

        return result;
    }
};
