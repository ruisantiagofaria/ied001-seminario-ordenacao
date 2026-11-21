# ===== 1. INSERTION SORT =====
def insertion_sort(lista, passo_a_passo=False):
   
    v = list(lista)                
    comparacoes = 0
    movimentos = 0
    
    for i in range(1, len(v)):
        chave = v[i]                # elemento que vamos encaixar
        j = i - 1
        while j >= 0:
            comparacoes += 1
            if v[j] > chave:        # maior que a chave: desloca para a direita
                v[j + 1] = v[j]
                movimentos += 1
                j -= 1
            else:
                break               # achou o lugar da chave
        v[j + 1] = chave            # encaixa a chave

        if passo_a_passo:
            print("  i=%d, chave=%d -> %s" % (i, chave, v))
    return v, comparacoes, movimentos


# ===== 2. MERGE SORT =====
def merge_sort(lista, passo_a_passo=False):

    contador = [0]    # lista de 1 posicao: a contagem sobrevive as chamadas recursivas
    resultado = _dividir(list(lista), contador, passo_a_passo, 0)
    return resultado, contador[0]


def _dividir(v, contador, passo_a_passo, nivel):
    recuo = "  " * nivel
    if len(v) <= 1:                   # caso base: 0 ou 1 elemento ja esta ordenado
        return v
    meio = len(v) // 2
    if passo_a_passo:
        print("%sdivide    %s -> %s | %s" % (recuo, v, v[:meio], v[meio:]))
    esquerda = _dividir(v[:meio], contador, passo_a_passo, nivel + 1)
    direita = _dividir(v[meio:], contador, passo_a_passo, nivel + 1)
    juntada = _intercalar(esquerda, direita, contador)
    if passo_a_passo:
        print("%sintercala %s + %s -> %s" % (recuo, esquerda, direita, juntada))
    return juntada


def _intercalar(esq, dire, contador):
    
    resultado = []
    i = 0
    j = 0
    while i < len(esq) and j < len(dire):
        contador[0] += 1
        if esq[i] <= dire[j]:         # <= mantem a ordem dos iguais (estavel)
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dire[j])
            j += 1
    resultado.extend(esq[i:])         # sobras de um dos lados
    resultado.extend(dire[j:])
    return resultado