class LockingTree(object):
    
    class Node(object):
        def __init__(self, val, parent):
            self.val = val
            self.lock = False
            self.lockUser = -1
            self.parent = parent
            self.children = list()
    
    def __init__(self, parent):
        """
        :type parent: List[int]
        """
        self.nodes = []
        for i in range(len(parent)):
            self.nodes.append(self.Node(i, parent[i]))
        
        for i in range(len(parent)):
            if parent[i] != -1:
                self.nodes[parent[i]].children.append(i)

    def lock(self, num, user):
        """
        :type num: int
        :type user: int
        :rtype: bool
        """
        if self.nodes[num].lock == False:
            self.nodes[num].lock = True
            self.nodes[num].lockUser = user
            return True
        return False

    def unlock(self, num, user):
        """
        :type num: int
        :type user: int
        :rtype: bool
        """
        if self.nodes[num].lock and self.nodes[num].lockUser == user:
            self.nodes[num].lock = False
            self.nodes[num].lockUser = -1
            return True
        return False
        
    def upgrade(self, num, user):
        """
        :type num: int
        :type user: int
        :rtype: bool
        """
        
        # It does not have any locked ancestors
        parent = num
        while parent != -1:
            if self.nodes[parent].lock:
                return False
            parent = self.nodes[parent].parent
        
        # It has at least one locked descendant (by any user)
        parents = [num]
        lockedNodes = 0
        
        while parents:
            parent = parents.pop(0)
            for c in self.nodes[parent].children:
                parents.append(c)
                if self.nodes[c].lock:
                    lockedNodes += 1
                    self.nodes[c].lock = False
                    self.nodes[c].userLock = -1

        if lockedNodes == 0:
            return False
        
        self.nodes[num].lock = True
        self.nodes[num].lockUser = user
        
        return True
        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)