class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        # create a table for visited node and set all to false
        visited: list[list[bool]] = [[False for _ in i] for i in grid]
        numIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                coordinate = (i, j)
                if visited[i][j] == False and grid[i][j] != "0":
                    self.bfs(grid, visited, coordinate)
                    numIslands += 1

        return numIslands

    def bfs(self, grid: list[list[str]], visited: list[tuple[int]], start: tuple[int]):
        queue: list[tuple[int]] = [start]

        checkLocation = [(0, -1), (-1, 0), (0, 1), (1, 0)]

        while queue:
            coordinate = queue.pop(0)
            visited[coordinate[0]][coordinate[1]] = True
            for next in checkLocation:
                i = coordinate[0] + next[0]
                j = coordinate[1] + next[1]
                locationToCheck = (i, j)

                # check if the next location to check is out of bounds
                # is already in the queue
                # or have been visited
                # or is the sea
                # if it is any of those it will skip
                if (
                    (i >= len(grid) or i < 0)
                    or (j >= len(grid[i]) or j < 0)
                    or locationToCheck in queue
                    or visited[i][j] == True
                    or grid[i][j] == "0"
                ):
                    continue

                queue.append(locationToCheck)
