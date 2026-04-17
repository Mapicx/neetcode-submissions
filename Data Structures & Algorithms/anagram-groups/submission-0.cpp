class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> anagramGroups;
        
        for (const string& word : strs) {
            string sortedWord = word;
            sort(sortedWord.begin(), sortedWord.end()); // Sort each word to create a unique key
            anagramGroups[sortedWord].push_back(word);
        }

        // Collect results
        vector<vector<string>> output;
        for (const auto& group : anagramGroups) {
            output.push_back(group.second);
        }

        return output;
    }
};
//act cat hat pots stop tops
