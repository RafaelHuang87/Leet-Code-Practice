# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors



class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        from queue import Queue
        oldToNew = {}
        oldToNew[node] = Node(node.val, [])
        q = Queue()
        q.put(node)
        while not q.empty():
            cur = q.get()
            cur_copy = oldToNew[cur]
            nes_list = []
            for ne in cur.neighbors:
                if ne not in oldToNew.keys():
                    ne_copy = Node(ne.val, [])
                    q.put(ne)
                    oldToNew[ne] = ne_copy
                nes_list.append(oldToNew[ne])
            cur_copy.neighbors = nes_list
        return oldToNew[node]
