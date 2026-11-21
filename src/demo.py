from ordenacao import insertion_sort, merge_sort

dados = [38, 27, 43, 3, 9, 82, 10]
print("Original:", dados)

print("\n--- Insertion Sort: passo a passo ---")
resultado, comp, mov = insertion_sort(dados, passo_a_passo=True)
print("Resultado:", resultado)
print("Comparacoes:", comp, "| Movimentos:", mov)

print("\n--- Insertion Sort: casos limite ---")
casos = [
    ("vazia", []),
    ("um elemento", [5]),
    ("ja ordenada", [1, 2, 3, 4, 5, 6, 7]),
    ("ordem inversa", [7, 6, 5, 4, 3, 2, 1]),
    ("repetidos", [4, 2, 4, 1, 2]),
]
for nome, lista in casos:
    saida, c, m = insertion_sort(lista)
    print("%-14s %s -> %s | comparacoes=%d movimentos=%d" % (nome, lista, saida, c, m))



    print("\n--- Merge Sort: divisao e intercalacao ---")
resultado, comp = merge_sort(dados, passo_a_passo=True)
print("Resultado:", resultado)
print("Comparacoes:", comp)

print("\n--- Merge Sort: casos limite ---")
for nome, lista in casos:
    saida, c = merge_sort(lista)
    print("%-14s %s -> %s | comparacoes=%d" % (nome, lista, saida, c))

print("\n--- Comparacao: lista em ordem inversa (comparacoes) ---")
print("%6s %12s %12s" % ("n", "insertion", "merge"))
for n in (10, 100, 1000):
    inversa = list(range(n, 0, -1))
    c_ins = insertion_sort(inversa)[1]
    c_mer = merge_sort(inversa)[1]
    print("%6d %12d %12d" % (n, c_ins, c_mer))