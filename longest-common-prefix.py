def longestCommonPrefix(strs):
    if strs == [" "] or strs == [""]:
        return ""
    shortest = min(strs, key=len)
    if shortest == "":
        return ""
    for i in strs:
        p = shortest
        k = 1
        if i[0] != p[0]:
            return ""
        while i[:k] == p[:k] and k < len(p):
            k += 1
        if i[k-1] != p[k-1]:
            k -= 1
        shortest = shortest[:k]
    return shortest