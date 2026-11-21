from ordenacao import insertion_sort, merge_sort


def test_insertion_vazia():
    assert insertion_sort([])[0] == []


def test_insertion_um_elemento():
    assert insertion_sort([5])[0] == [5]


def test_insertion_ja_ordenada():
    v, c, m = insertion_sort([1, 2, 3, 4])
    assert v == [1, 2, 3, 4] and c == 3 and m == 0


def test_insertion_ordem_inversa():
    v, c, m = insertion_sort([4, 3, 2, 1])
    assert v == [1, 2, 3, 4] and c == 6


def test_insertion_repetidos():
    assert insertion_sort([3, 1, 3, 2, 1])[0] == [1, 1, 2, 3, 3]


def test_insertion_nao_altera_original():
    original = [3, 1, 2]
    insertion_sort(original)
    assert original == [3, 1, 2]



def test_merge_vazia():
    assert merge_sort([])[0] == []


def test_merge_um_elemento():
    assert merge_sort([5])[0] == [5]


def test_merge_ja_ordenada():
    assert merge_sort([1, 2, 3, 4])[0] == [1, 2, 3, 4]


def test_merge_ordem_inversa():
    assert merge_sort([4, 3, 2, 1])[0] == [1, 2, 3, 4]


def test_merge_repetidos():
    assert merge_sort([3, 1, 3, 2, 1])[0] == [1, 1, 2, 3, 3]


def test_merge_nao_altera_original():
    original = [3, 1, 2]
    merge_sort(original)
    assert original == [3, 1, 2]


def test_insertion_e_merge_dao_o_mesmo_resultado():
    dados = [38, 27, 43, 3, 9, 82, 10, 27, 3]
    assert insertion_sort(dados)[0] == merge_sort(dados)[0] == sorted(dados)




if __name__ == "__main__":
    testes = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for t in testes:
        t()
        print("OK  ", t.__name__)
    print("\n%d testes passaram." % len(testes))