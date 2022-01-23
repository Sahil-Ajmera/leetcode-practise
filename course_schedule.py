"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

 

Constraints:

    1 <= numCourses <= 105
    0 <= prerequisites.length <= 5000
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    All the pairs prerequisites[i] are unique.
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited: typing.Set = set()
        course_completed: typing.Set = set()
            
        dependency_map = defaultdict(list)
        
        def course_can_be_completed(current_course):
            
            visited.add(current_course)
            
            if current_course not in dependency_map:
                course_completed.add(current_course)
                return True
            
            can_be_completed = True
            for dependency in dependency_map[current_course]:
                if dependency in visited:
                    can_be_completed &= dependency in course_completed
                elif dependency not in course_completed:
                    can_be_completed &= course_can_be_completed(dependency)
            
            if can_be_completed:
                course_completed.add(current_course)
            return can_be_completed

        for prerequisite in prerequisites:
            dependency_map[prerequisite[0]].append(prerequisite[1])
            
        for i in range(numCourses):
            if i not in dependency_map:
                course_completed.add(i)

        for i in range(numCourses):
            if i not in course_completed and i not in visited:
                course_can_be_completed(i)
        
        if len(course_completed) == numCourses:
            return True
        else:
            return False
                
        
        
