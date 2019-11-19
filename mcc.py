# The function accepts STRING s as parameter, and returns an INTEGER
#
 
def maxLCS(s):
    distels = []
    for x in s:#creating a list of all the distinct elements of 
        if x in distels:
            continue
        distels.append(x)
    #print(distels)this part is correct
    #now, need to make a list with all the possible s1, s2 combos. Max num to split string is len(s) -1
    combos = []
    for x in range(1, len(s)):
        s1 = s[0:x]
        s2 = s[x:len(s)]
        combos.append([s1,s2])#each element of combos contains two strings. Element 0 of each combo element is s1, element 1 of each combo element is s2
    #print(combos) correctly getting list of all the substrings
    
 
 
    cuts = []
    for x in combos:#now, need to calculate cut commonality for each set of substrings
        common = 0
        for dis in distels:#iterating through distinct elements to count number of elements in common
            if (dis in x[0]) and (dis in x[1]):#now, should count number of times the distinct element is in each string. If number of times isn't equal, just add the minimum of those two counts
                c1 = x[0].count(dis)
                c2 = x[1].count(dis)
                common+=min(c1,c2)
        cuts.append(common)
    #have now created a list with indices corresponding to list of combos
    #print(cuts)
    #maxcutind = cuts.index(max(cuts))
    return max(cuts)
