
def same_necklace(str1, str2):
    if len(str1) != len(str2):
        return False
    for num in range(len(str1)):
        temp = str1[num:] + str1[:num]
        # print(temp)
        if temp == str2:
            return True
    if (str1 == "") and (str2 == ""):
        return True
    return False


def repeats(string):
    count = 1
    for num in range(1, len(string)):
        temp = string[num:] + string[:num]
        # print(temp)
        if temp == string:
            count += 1
    return count


print("same_necklace function: ")
print(same_necklace("nicole", "icolen"))  # => true
print(same_necklace("nicole", "lenico"))  # => true
print(same_necklace("nicole", "coneli"))  # => false
print(same_necklace("aabaaaaabaab", "aabaabaabaaa"))  # => true
print(same_necklace("abc", "cba"))  # => false
print(same_necklace("xxyyy", "xxxyy"))  # => false
print(same_necklace("xyxxz", "xxyxz"))  # => false
print(same_necklace("x", "x"))  # => true
print(same_necklace("x", "xx"))  # => false
print(same_necklace("x", ""))  # => false
print(same_necklace("", ""))  # => true

print("repeats function: ")
print(repeats("abc"))  # => 1
print(repeats("abcabcabc"))  # => 3
print(repeats("abcabcabcx"))  # => 1
print(repeats("aaaaaa"))  # => 6
print(repeats("a"))  # => 1
print(repeats(""))  # => 1
