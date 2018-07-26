
"""
This class takes in a list of elements and an bi-valued operation and checks 
if the list is a group under the operation. To test for group it does the following 
checks

1) that the group is complete under the operation 
2) that the group has an identity element
3) that every element of the group has an inverse.
"""
class group:

    def identityCheck(self):
        for a in self._elements:
            identity = True
            for b in self._elements:
                if self._f(a, b) != b or self._f(b, a) != b:
                    identity = False
                    break
            if identity:
                self._identity = a
                return
            
        raise EnvironmentError('group is without identity; add identity to make group')
    
    def calculateInverses(self):
        self._inverses = {}
        for i in self._elements:
            if i in self._inverses:
                continue
            for j in self._elements:
                if self._f(i, j) == self._f(j, i) == self._identity:
                    self._inverses[i] = j
                    self._inverses[j] = i
                    break
        if len(self._inverses) != len(self._elements):
            raise EnvironmentError('group is incomplete; not every element has its inverses; add elements necessary to make it complete')
                
    def __init__(self, elements, f):
        self._element_set = set(elements)
        self._f = f
        self._elements = elements
        closed = True
        for i in elements:
            for j in elements:
                if f(i, j) not in self._element_set:
                    closed = False
                    raise EnvironmentError('group is incomplete; add elements necessary to make it complete')
        self.identityCheck()
        self.calculateInverses()

    def get_inverse(self,element):
        return self._inverses[element]
    
    def get_identity(self):
        return self._identity

    """
    Given this group, this method returns True if the list of elements in itemlist 
    is a subgroup of this group. 
    """
    def is_subgroup(self, itemlist):
        result = True
        for i in itemlist:
            for j in itemlist:
                if not self._f(i, self._inverses[j]) in itemlist:
                    result = False
                    break

        return result
                

    def is_cyclic(self):
        pass

    def is_commutative(self):
        pass



def are_isomorphic(g1, g2):
    pass


l = [1,2,3,4]
l2 = [1, 4]
l3 = [1, 2, 3, 4]

def f_mod_5(a, b):
    return (a * b) % 5

def f_add(a, b):
    return a + b

g = group(l, f_mod_5)

print(g.get_identity())
print(g.is_subgroup(l2))
print(g.is_subgroup(l3))

        
            
        
        




