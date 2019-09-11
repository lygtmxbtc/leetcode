haystack = 'BBC ABCDAB ABCDABCDABDE'
needle = 'ABCDABD'

'''
Prefix means except last character all combination for str
Suffix means except first charcter all combination for str
Partial match value is the length of the longest common element of prefix and suffix
'''
def get_partial_match_table(str):
    table_dict = {}
    str_length = len(str)
    for i in range(1,str_length+1):
        match_str = str[:i]
        prefix = [match_str[:p] for p in range(1,i)]
        suffix = [match_str[s:] for s in range(-1,-i,-1)]
        tmp_index = 0
        max_match_element_length = 0
        while tmp_index < i - 1:
            if prefix[tmp_index] == suffix[tmp_index]:
                max_match_element_length = len(prefix[tmp_index])
            tmp_index += 1
        table_dict[i] = max_match_element_length
    return table_dict

def kmp(haystack,needle):
    haystack_length = len(haystack)
    needle_length = len(needle)
    partial_match_table = get_partial_match_table(needle)
    i = 0
    matched_length = 0
    while i < haystack_length:
        if haystack[i] == needle[matched_length]:
            matched_length += 1
        elif matched_length in [0,1]:
            matched_length = 0
        else:
            # needle shift nums = matched nums - matched value
            # then after shift, the matched_length change to matched value
            matched_length = partial_match_table[matched_length]
            continue

        if matched_length == needle_length:
            return i - (matched_length - 1)

        i += 1
    return -1

print(kmp(haystack,needle))






