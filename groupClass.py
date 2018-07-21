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

    
    def get_identity(self):
        return self._identity

l = [0,1,2,3,4]
def f_mod_5(a, b):
    return (a + b) % 5

def f_add(a, b):
    return a + b

g = group(l, f_add)

print(g.get_identity())
        
            
        
        




