class Solution:
    def largestValues(self, root) -> list[int]:
        ans = []
        queue = [root]

        while any(queue):
            
            ans.append(max([i.val for i in queue if i]))
            new = []
            for i in queue:
                if i.left!=None: new.append(i.left)
                if i.right!=None: new.append(i.right)
            queue = new
        
        return ans