class Solution(object):
    """
    find the longest unique character substring in the string s. time complexity: O(n)
    maintain a sliding range from i to j. Assume a longest substring from s[i]..s[j].
    Store each character as a key in a dict, with
    its respective value being its index in the string.
    For s[j+1], two outcomes are possible:
        1. The character is unique and not in the dict. increment j
        2. the character is in the dict. take the max(i, dict[s[j+1]]) to find the correct i
        Take the max of the maxLen value max(max, j-i+1)
        store char in dict: dict[s[j+1]] = j+1
    """

    @classmethod
    def length_of_longest_substring(cls, given_str):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        start = 0
        letters = {}
        for j, char in enumerate(given_str):
            if given_str[j] in letters:
                if start < letters[given_str[j]]:
                    start = letters[given_str[j]]
            if max_len < j - start + 1:
                max_len = j - start + 1
            letters[given_str[j]] = j + 1
        return max_len

if __name__ == '__main__':
    SAMPLE = "pwwkew"
    print(Solution.length_of_longest_substring(SAMPLE))
