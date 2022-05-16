class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0;
        l = 1 + self.maxDepth(root.left)
        r = 1 + self.maxDepth(root.right)
        return max(l,r);