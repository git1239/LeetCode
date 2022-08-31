class Solution:
    def isHeightBalanced(self, root):
        if root:
            left_height, left_balanced = self.isHeightBalanced(root.left)
            right_height, right_balanced = self.isHeightBalanced(root.right)

            return (
                max(left_height, right_height) + 1,
                (
                    left_balanced
                    and right_balanced
                    and (abs(right_height - left_height) <= 1)
                ),
            )

        return (0, True)

    def isBalanced(self, root):
        _, is_balanced = self.isHeightBalanced(root)
        return is_balanced
