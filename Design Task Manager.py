# 3408. Design Task Manager

# There is a task management system that allows users to manage their tasks, each associated with a priority. The system should efficiently handle adding, modifying, executing, and removing tasks.

# Implement the TaskManager class:

# TaskManager(vector<vector<int>>& tasks) initializes the task manager with a list of user-task-priority triples. Each element in the input list is of the form [userId, taskId, priority], which adds a task to the specified user with the given priority.

# void add(int userId, int taskId, int priority) adds a task with the specified taskId and priority to the user with userId. It is guaranteed that taskId does not exist in the system.

# void edit(int taskId, int newPriority) updates the priority of the existing taskId to newPriority. It is guaranteed that taskId exists in the system.

# void rmv(int taskId) removes the task identified by taskId from the system. It is guaranteed that taskId exists in the system.

# int execTop() executes the task with the highest priority across all users. If there are multiple tasks with the same highest priority, execute the one with the highest taskId. After executing, the taskId is removed from the system. Return the userId associated with the executed task. If no tasks are available, return -1.

# Note that a user may be assigned multiple tasks.

 

# Example 1:

# Input:
# ["TaskManager", "add", "edit", "execTop", "rmv", "add", "execTop"]
# [[[[1, 101, 10], [2, 102, 20], [3, 103, 15]]], [4, 104, 5], [102, 8], [], [101], [5, 105, 15], []]

# Output:
# [null, null, null, 3, null, null, 5]

# Explanation

# TaskManager taskManager = new TaskManager([[1, 101, 10], [2, 102, 20], [3, 103, 15]]); // Initializes with three tasks for Users 1, 2, and 3.
# taskManager.add(4, 104, 5); // Adds task 104 with priority 5 for User 4.
# taskManager.edit(102, 8); // Updates priority of task 102 to 8.
# taskManager.execTop(); // return 3. Executes task 103 for User 3.
# taskManager.rmv(101); // Removes task 101 from the system.
# taskManager.add(5, 105, 15); // Adds task 105 with priority 15 for User 5.
# taskManager.execTop(); // return 5. Executes task 105 for User 5.
 

# Constraints:

# 1 <= tasks.length <= 105
# 0 <= userId <= 105
# 0 <= taskId <= 105
# 0 <= priority <= 109
# 0 <= newPriority <= 109
# At most 2 * 105 calls will be made in total to add, edit, rmv, and execTop methods.
# The input is generated such that taskId will be valid.

# Code: Python3
import heapq
from typing import List

class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        """
        tasks: list of [userId, taskId, priority]
        """
        # task_map: taskId -> (userId, priority)
        self.task_map = {}
        # heap holds tuples (-priority, -taskId, taskId)
        # using negative values to simulate max-heap; tie-breaker: higher taskId first
        self.heap = []
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        """
        Add a new task. It's guaranteed taskId does not already exist.
        """
        self.task_map[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        """
        Update priority of an existing task. It's guaranteed taskId exists.
        We update the authoritative map and push the new entry onto the heap.
        Old heap entries become stale and will be skipped when popped.
        """
        userId, _ = self.task_map[taskId]
        self.task_map[taskId] = (userId, newPriority)
        heapq.heappush(self.heap, (-newPriority, -taskId, taskId))

    def rmv(self, taskId: int) -> None:
        """
        Remove an existing task. It's guaranteed taskId exists.
        We remove it from the map; its heap entries are lazily ignored later.
        """
        if taskId in self.task_map:
            del self.task_map[taskId]

    def execTop(self) -> int:
        """
        Execute (remove and return) the userId of the highest-priority task.
        If tie in priority, return the task with larger taskId.
        Return -1 if no tasks remain.
        """
        while self.heap:
            neg_prio, neg_tid, tid = self.heap[0]
            # Check if tid is still valid and matches the priority in map
            if tid not in self.task_map:
                heapq.heappop(self.heap)  # stale (removed)
                continue
            userId, cur_prio = self.task_map[tid]
            if -neg_prio != cur_prio:
                heapq.heappop(self.heap)  # stale (outdated priority)
                continue
            # Found the valid top task
            heapq.heappop(self.heap)
            del self.task_map[tid]
            return userId
        return -1