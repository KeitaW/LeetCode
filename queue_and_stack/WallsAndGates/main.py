from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """You are given a m x n 2D grid initialized with these three possible values.

        -1 - A wall or an obstacle.
        0 - A gate.
        INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
        Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.
        Do not return anything, modify rooms in-place instead.
        """
        if len(rooms) == 0:
            return rooms
        height, width = len(rooms), len(rooms[0])

