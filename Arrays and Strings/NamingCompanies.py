from collections import defaultdict


class Solution:
    def distinctNames(self, ideas: list[str]) -> int:
        words = defaultdict(set)
        for w in ideas:
            words[w[0]].add(w[1:])

        res = 0
        for c1 in words:
            for c2 in words:
                if c1==c2: continue

                same = len(words[c1].intersection(words[c2]))

                d1 = len(words[c1]) - same
                d2 = len(words[c2]) - same

                res += d1 * d2
        return res