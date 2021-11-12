# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
                3  
            1       4
         3    

Base conditions:
Base condition: node being null, return

Check:
node having no previousSaveD to compare,save this node value as previousSaved, add to result, traverse left and right
node having greater or equal to than previosSaveD, add to result,  save this node value as previousSaved
node not having greater, traverse left and right, save this node value as previousSaved
result = [3, 4]
"""
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def traverseNodeWithPath(node: TreeNode, path: List[TreeNode]):
            if node == None:
                return
            else:
                save: bool = True
                for idx in range(0, len(path)):
                    if node.val < path[idx].val:
                        save = False
                if save:
                    result.append(node.val)
                    path.append(node)
                    traverseNodeWithPath(node.left, path)
                    traverseNodeWithPath(node.right, path)
                    path.pop()
                else:
                    path.append(node)
                    traverseNodeWithPath(node.left, path)
                    traverseNodeWithPath(node.right, path)
                    path.pop()
        result = []
        traverseNodeWithPath(root, [])
        return len(result)
