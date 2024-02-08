class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def evaluar_arbol(nodo):
    if nodo.valor.isdigit():
        return int(nodo.valor)
    else:
        izquierda = evaluar_arbol(nodo.izquierda)
        derecha = evaluar_arbol(nodo.derecha)
        if nodo.valor == '+':
            return izquierda + derecha
        elif nodo.valor == '-':
            return izquierda - derecha
        elif nodo.valor == '*':
            return izquierda * derecha
        elif nodo.valor == '/':
            return izquierda / derecha

# Crear el árbol aritmético: 3 * (4 + 5)
nodo_mul = NodoArbol('*')
nodo_mul.izquierda = NodoArbol('3')
nodo_suma = NodoArbol('+')
nodo_suma.izquierda = NodoArbol('4')
nodo_suma.derecha = NodoArbol('5')
nodo_mul.derecha = nodo_suma

# Evaluar el árbol aritmético
resultado = evaluar_arbol(nodo_mul)
print("Resultado de la expresión:", resultado)
