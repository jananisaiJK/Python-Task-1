def longest_common_substring(str1, str2):
    m = len(str1)
    k = len(str2)
    
    # Create a matrix to store lengths of longest common suffixes of substrings
    lcs_suffix = [[0] * (k + 1) for i in range(m + 1)]
    
    longest_length = 0
    end_index = 0
    
    # Building the matrix in bottom-up fashion
    for i in range(1, m + 1):
        for j in range(1, k + 1):
            if str1[i - 1] == str2[j - 1]:
                lcs_suffix[i][j] = lcs_suffix[i - 1][j - 1] + 1
                if lcs_suffix[i][j] > longest_length:
                    longest_length = lcs_suffix[i][j]
                    end_index = i - 1
            else:
                lcs_suffix[i][j] = 0
    
    # The longest common substring
    longest_common_substr = str1[end_index - longest_length + 1: end_index + 1]
    
    return longest_common_substr

# Example usage
str1 = "abcdef"
str2 = "zabdf"
print("Longest Common Substring:", longest_common_substring(str1, str2))
