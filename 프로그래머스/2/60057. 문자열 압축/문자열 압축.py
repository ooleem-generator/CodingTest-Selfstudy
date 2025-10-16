def solution(s):
    zipped = ""
    zipped_list = []
    #snippet = []
    for i in range(1,len(s)+1):
        zipped = ""
        snippet = []
        for j in range(0, len(s), i):
            if j+i < len(s):
                if not snippet:
                    snippet.append([1, s[j:j+i]])
                else:
                    if snippet[-1][1] == s[j:j+i]:
                        snippet[-1][0] += 1
                    else:
                        snippet.append([1, s[j:j+i]])
            else:
                if not snippet:
                    snippet.append([1, s[j:]])
                else:
                    if snippet[-1][1] == s[j:]:
                        snippet[-1][0] += 1
                    else:
                        snippet.append([1, s[j:]])
        #print(snippet)
        
        for num, val in snippet:
            if num != 1:
                zipped += str(num)
            zipped += val
        zipped_list.append(zipped)
        
        
        
        
    return min(list(map(len, zipped_list)))