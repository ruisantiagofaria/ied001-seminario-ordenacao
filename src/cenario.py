from ordenacao import insertion_sort, merge_sort

print("Cenario: a filial recebe lotes de protocolos fora de ordem")
print("e precisa ordena-los antes de gravar no sistema.")


def esta_ordenada(v):
    for k in range(len(v) - 1):
        if v[k] > v[k + 1]:
            return False
    return True


def processar(titulo, lote, detalhes=False):
    print("\n=== %s ===" % titulo)
    if len(lote) <= 12:
        print("Entrada (%d protocolos): %s" % (len(lote), lote))
    else:
        print("Entrada: %d protocolos, primeiros: %s" % (len(lote), lote[:6]))

    if detalhes:
        print("\n-- Insertion Sort, passo a passo --")
    ins, c_ins, m_ins = insertion_sort(lote, passo_a_passo=detalhes)
    if detalhes:
        print("\n-- Merge Sort, divisao e intercalacao --")
    mer, c_mer = merge_sort(lote, passo_a_passo=detalhes)

    print("\nInsertion Sort: %d comparacoes, %d movimentos" % (c_ins, m_ins))
    print("Merge Sort:     %d comparacoes" % c_mer)
    print("Mesmo resultado nos dois metodos:", ins == mer)
    print("Saida ordenada corretamente:", esta_ordenada(mer))
    if len(lote) <= 12:
        print("Saida:", mer)
    else:
        print("Primeiros ordenados:", mer[:6])


processar("1. Lote do dia (pequeno, quase ordenado)",
          [1001, 1002, 1004, 1003, 1005, 1006, 1008, 1007], detalhes=True)

processar("2. Lote ja ordenado",
          [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008])

processar("3. Condicao-limite: lote vazio", [])

processar("4. Lote de migracao (grande e embaralhado)",
          [1000 + (i * 37) % 1000 for i in range(1000)])