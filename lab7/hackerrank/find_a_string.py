def count_substring(string, sub_string):
    n = len(string)
    m = len(sub_string)
    count = 0
    for i in range(n-m+1):
        if string[i:m+i]==sub_string:
            count +=1
    return count