"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
"""

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

Time Complexity: O(N^2) (?)
Space Complexity: O(N^2) (?)
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
      
 

"""
Solution storing the max at every node

Time Complexity : O(N)
Space complexity: O(N) call stack is as high as height of the tree
"""

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
	
        def dfs(node, max_so_far):
            nonlocal num_good_nodes
            if max_so_far <= node.val:
                num_good_nodes += 1
            if node.right:
                dfs(node.right, max(node.val, max_so_far))
            if node.left:
                dfs(node.left, max(node.val, max_so_far))
        
        num_good_nodes = 0
        dfs(root, float("-inf"))
        return num_good_nodes

"""
Iterative solution O(N) time complexity O(N) space complexity
that can use any variant of pre order traversal since the path from root to a node is unique
"""

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, float("-inf"))]
        num_good_nodes = 0
        while stack:
            node, max_so_far = stack.pop()
            if max_so_far <= node.val:
                num_good_nodes += 1
            if node.left:
                stack.append((node.left, max(node.val, max_so_far)))
            if node.right:
                stack.append((node.right, max(node.val, max_so_far)))
        
        return num_good_nodes

"""
BFS 

Time Complexity: O(N)

Space Complexity: O(N) because from one level to another all nodes in the next level will be populated which in the leaf nodes are N/2 of all nodes in the tree.
"""

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        num_good_nodes = 0
        
        # Use collections.deque for efficient popping
        queue = deque([(root, float("-inf"))])
        while queue:
            node, max_so_far = queue.popleft()
            if max_so_far <= node.val:
                num_good_nodes += 1
            if node.right:
                queue.append((node.right, max(node.val, max_so_far)))
            if node.left:
                queue.append((node.left, max(node.val, max_so_far)))
        
        return num_good_nodes
