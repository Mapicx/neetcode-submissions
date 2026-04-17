class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded_str;
        string str_to_find_len;
        for(auto itr = strs.begin();itr < strs.end() ; itr++)
        {
            int len_of_word = 0;
            str_to_find_len = *itr;
            len_of_word = str_to_find_len.length();
            encoded_str += to_string(len_of_word) + "#" + *itr;
        }
        return encoded_str;
    }

    vector<string> decode(string s) 
    {
        vector<string> decoded_strs;
        int i = 0;
        while (i < s.length()) {
            int hash_pos = s.find('#', i);
            int length = stoi(s.substr(i, hash_pos - i));
            string word = s.substr(hash_pos + 1, length);
            decoded_strs.push_back(word);
            i = hash_pos + 1 + length;
        }

        return decoded_strs;
    }

};
