# Seminário IED001 - Insertion Sort e Merge Sort

**Grupo:** The Office
**Disciplina:** IED001 - Estruturas de Dados (FATEC Mauá, 2026/2)
**Tema:** Métodos de Ordenação II

**Integrantes:**
- Anderson Rodrigues Sales
- Gabriely Alvim dos Santos Fonseca
- João Victor dos Santos Ferreira
- Matheus Peres do Nascimento
- Rui Santiago Faria

**Repositório (complementar):** https://github.com/ruisantiagofaria/ied001-seminario-ordenacao

## O que o projeto faz

Ordena a mesma coleção por dois métodos, Insertion Sort e Merge Sort, mostrando o
resultado, os passos intermediários e a contagem de comparações de cada um.

Cenário realista: a filial recebe lotes de protocolos fora de ordem e precisa
ordená-los antes de gravar no sistema.

## Linguagem e dependências

- Python 3 (testado com Python 3.13)
- Nenhuma biblioteca externa: usa só a biblioteca padrão.

## Como executar

Abra o terminal na pasta do projeto e rode:

- Cenário (demonstração principal): `py src/cenario.py`
- Passo a passo e casos limite: `py src/demo.py`
- Testes: `py src/test_ordenacao.py`

(Linux/macOS: trocar `py` por `python3`.)

## Entrada de exemplo

Lote de protocolos do cenário: `[1001, 1002, 1004, 1003, 1005, 1006, 1008, 1007]`

Saída: `[1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008]` pelos dois métodos.
O Insertion Sort faz 9 comparações e o Merge Sort faz 12.

Coleção usada no `demo.py`: `[38, 27, 43, 3, 9, 82, 10]`, ordenada como
`[3, 9, 10, 27, 38, 43, 82]`.

## Estrutura

- `src/ordenacao.py`: Insertion Sort e Merge Sort
- `src/cenario.py`: cenário realista (lotes de protocolos)
- `src/demo.py`: passo a passo e casos limite
- `src/test_ordenacao.py`: 13 testes (vazia, um elemento, já ordenada, ordem inversa, repetidos, original preservado)
- `docs/relatorio.pdf`: relatório técnico (inclui a declaração de uso de IA)
- `docs/slide.pdf`: apresentação
- `evidencias/`: prints e saídas das execuções
