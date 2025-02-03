import collections

beginWord = "hit" 
endWord = "cog" 
wordList = ["hot","dot","dog","lot","log","cog"]
wordList=set(wordList)

visited=set()

def check(word1,word2):
    if len(word1)!= len(word2):
        return False
    diff=0
    for c1,c2 in zip(word1,word2):
        if c1!= c2:
            diff+=1
        if diff>1:
            return False
    return True

count=0

def wordshit(beginWord,endWord,wordList,count):
    q=collections.deque()
    q.append([beginWord])
    visited.add(beginWord)
    
    while q:
        path=q.popleft()
        current_word=path[-1]
        
        if current_word==endWord:
            return path
        
        for word in wordList:
            if word not in visited and check(current_word,word):
                q.append(path+[word])
                visited.add(word)
    return []

print(wordshit(beginWord,endWord,wordList,count))