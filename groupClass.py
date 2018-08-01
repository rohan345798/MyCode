
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
                
    def generate(self, element):
        generatedGroup = []
        generator = self._f(element, element)
        generatedGroup.append(generator)

        while generator != element:
            generator = self._f(generator, element)
            generatedGroup.append(generator)

        return generatedGroup

    def is_cyclic_2(self):
        for i in self._elements:
            if len(self.generate(i)) == len(self._elements):
                return True
        return False

    def is_commutative(self):
        pass



def are_isomorphic(g1, g2, f):
    if len(g1._elements) != len(g2._elements):
        return False

    checklist = []
    for i in g1._elements:
        if f(i) in checklist:
            return False
        checklist.append(f(i))

    for i in g1._elements:
        for j in g1._elements:
            if f(g1._f(i, j)) != g2._f(f(i), f(j)):
                return False
    return True
    

l = [1,2,3,4]
l2 = [0,5]
l3 = [0,1]

def f_mod_2(a, b):
    return (a + b) % 2

def f_mod_10(a, b):
    return (a + b) % 10  

def multiply5(a):
    return a*5

g1 = group(l2, f_mod_10)
g2 = group(l3, f_mod_2)
print (are_isomorphic(g2,g1,multiply5))


'''
print(g.get_identity())
print(g.is_subgroup(l2))
print(g.is_subgroup(l3))
'''
        
            
        
        




