import collections

beginWord = "hit" 
endWord = "cog" 
wordList = ["hot","dot","dog","lot","log","cog"]
wordList=set(wordList)

visited=set()

def check(w1,w2):
    diff=0
    for a , b in zip(w1,w2):
        if a!=b :
            diff+=1
        if diff>1:
            return False
    return True


def bfs(begin):
    q=collections.deque()
    q.append([begin])
    visited.add(begin)
    
    while q:
        path=q.popleft()
        curr=path[-1]
        
        if curr==endWord:
            return path

        for word in wordList:
            if word not in visited and check(word,curr):
                q.append(path+[word])
                visited.add(word)
    return []
res=bfs(beginWord)
print(res)