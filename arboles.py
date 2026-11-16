def crear_nodo(valor):
    return {"valor": valor, "izq": None, "der": None}

def insertar(raiz, valor):
    if raiz is None:
        return crear_nodo(valor)
    if valor < raiz["valor"]:
        raiz["izq"] = insertar(raiz["izq"], valor)
    elif valor > raiz["valor"]:
        raiz["der"] = insertar(raiz["der"], valor)
    return raiz

raiz = None
for numero in [50, 30, 70, 20, 40, 60, 80]:
    raiz = insertar(raiz, numero)

def buscar(raiz, valor):
    if raiz is None:
        return False
    if raiz["valor"] == valor:
        return True
    if valor < raiz["valor"]:
        return buscar(raiz["izq"], valor)
    return buscar(raiz["der"], valor)

def inorden(raiz):
    if raiz is not None:
        inorden(raiz["izq"])
        print(raiz["valor"], end=" ")
        inorden(raiz["der"])

print(buscar(raiz, 60))
inorden(raiz)



def preorden(raiz):
    if raiz is not None:
        print(raiz["valor"], end=" ")
        preorden(raiz["izq"])
        preorden(raiz["der"])


def postorden(raiz):
    if raiz is not None:
        postorden(raiz["izq"])
        postorden(raiz["der"])
        print(raiz["valor"], end=" ")


print("\nPreorden:")
preorden(raiz)

print("\nPostorden:")
postorden(raiz)


def contar_nodos(raiz):
    if raiz is None:
        return 0
    return 1 + contar_nodos(raiz["izq"]) + contar_nodos(raiz["der"])


def contar_hojas(raiz):
    if raiz is None:
        return 0
    if raiz["izq"] is None and raiz["der"] is None:
        return 1
    return contar_hojas(raiz["izq"]) + contar_hojas(raiz["der"])


def altura(raiz):
    if raiz is None:
        return -1
    return 1 + max(altura(raiz["izq"]), altura(raiz["der"]))


def eliminar(raiz, valor):
    if raiz is None:
        return None

    if valor < raiz["valor"]:
        raiz["izq"] = eliminar(raiz["izq"], valor)

    elif valor > raiz["valor"]:
        raiz["der"] = eliminar(raiz["der"], valor)

    else:
        # Caso 1 y 2: Sin hijos o con un hijo
        if raiz["izq"] is None:
            return raiz["der"]

        if raiz["der"] is None:
            return raiz["izq"]

        # Caso 3: Dos hijos
        menor = raiz["der"]

        while menor["izq"] is not None:
            menor = menor["izq"]

        raiz["valor"] = menor["valor"]
        raiz["der"] = eliminar(raiz["der"], menor["valor"])

    return raiz


def crear_nodo(valor):
    return {"valor": valor, "izq": None, "der": None}


def registrar(raiz, codigo):
    if raiz is None:
        return crear_nodo(codigo)

    if codigo < raiz["valor"]:
        raiz["izq"] = registrar(raiz["izq"], codigo)
    elif codigo > raiz["valor"]:
        raiz["der"] = registrar(raiz["der"], codigo)

    return raiz


def consultar(raiz, codigo):
    if raiz is None:
        return False
    if raiz["valor"] == codigo:
        return True
    if codigo < raiz["valor"]:
        return consultar(raiz["izq"], codigo)
    return consultar(raiz["der"], codigo)


def listar(raiz):
    if raiz is not None:
        listar(raiz["izq"])
        print(raiz["valor"], end=" ")
        listar(raiz["der"])


def retirar(raiz, codigo):
    if raiz is None:
        return None

    if codigo < raiz["valor"]:
        raiz["izq"] = retirar(raiz["izq"], codigo)
    elif codigo > raiz["valor"]:
        raiz["der"] = retirar(raiz["der"], codigo)
    else:
        if raiz["izq"] is None:
            return raiz["der"]
        if raiz["der"] is None:
            return raiz["izq"]

        menor = raiz["der"]
        while menor["izq"] is not None:
            menor = menor["izq"]

        raiz["valor"] = menor["valor"]
        raiz["der"] = retirar(raiz["der"], menor["valor"])

    return raiz

raiz = None

for codigo in [50, 30, 70, 20, 40, 60, 80]:
    raiz = registrar(raiz, codigo)

print("Libros registrados:")
listar(raiz)

print("\nConsultar código 40:", consultar(raiz, 40))

raiz = retirar(raiz, 30)

print("Después de retirar el código 30:")
listar(raiz)

