class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res = []
        c = -1
        curr=[]
        for i,word in enumerate(words):
            c += 1 + len(word)
            if c<=maxWidth:
                curr.append(word)
            else:
                res.append(curr)
                c = len(word)
                curr = [word]
        if curr:
            res.append(curr)

        for i,line in enumerate(res):

            if i == len(res)-1:
                res[i] = " ".join(line).ljust(maxWidth)
                continue

            words = len(line)
            if words == 1:
                res[i] = line[0].ljust(maxWidth)
                continue

            chars = sum([len(word) for word in line])
            spaces = maxWidth-chars
            
            gaps = [0 for _ in range(words)]
            k = 0
            while spaces:
                gaps[k]+=1
                k = (k+1)%(words-1)
                spaces-=1
            
            s = ""
            for k,word in enumerate(line):
                s+=word
                s+=" "*gaps[k]

            res[i]=s
        return res