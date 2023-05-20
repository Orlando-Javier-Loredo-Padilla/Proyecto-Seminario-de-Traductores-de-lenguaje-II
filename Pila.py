import ArbolSintactico

class elementoPila:

    def __init__(self,v,rNombre,id):

        self.valor = v
        self.nombreRegla = rNombre
        
        self.id = id
        self.nodo = ArbolSintactico.Nodo()

    def printValor(self):

        print(self.valor)

    def returnValor(self):

        return self.valor

class terminal(elementoPila):
    pass

class noTerminal(elementoPila):
    pass

class estado(elementoPila):
    pass

class stack:

    def __init__(self):
        
        self.stack = []

    def push(self,e):

        self.stack.append(e)

    def top(self):

        return self.stack[-1]

    def pop(self):

        return self.stack.pop()

    def stackSize(self):

        return len(self.stack)

    def isEmpty(self):

        if len(self.stack)==0:

            return True
        return False

    def limpiar(self):

        self.stack = []

    def printStack(self):

        line = ""

        for i in self.stack:

            line += i.valor

        print(line)