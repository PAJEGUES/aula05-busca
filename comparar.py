# Arquivo: comparar.py - um esqueleto, quatro algoritmos.
from mapa import mapa_romenia, heuristica_bucareste

h = heuristica_bucareste

def busca(grafo, inicio, objetivo, prioridade):
    """prioridade(g, cidade, passos) devolve o valor do campo 0."""
    fronteira = [(0, 0, inicio, [inicio])] # (chave, g, cidade, caminho)
    visitados = set()

    while fronteira:
        fronteira.sort(key=lambda item: item[0])
        chave, g, atual, caminho = fronteira.pop(0)

        if atual == objetivo:
            return caminho, g

        if atual not in visitados:
            visitados.add(atual)
            for vizinho, custo in grafo.get(atual, []):
                if vizinho not in visitados:
                    novo_g = g + custo
                    passos = len(caminho)
                    fronteira.append((prioridade(novo_g, vizinho, passos), novo_g, vizinho, caminho + [vizinho]))
    return None, float('inf')

algoritmos = {
 'largura': lambda g, cidade, passos: passos,
 'custo uniforme': lambda g, cidade, passos: g,
 'gulosa': lambda g, cidade, passos: h[cidade],
 'A*': lambda g, cidade, passos: g + h[cidade],
}

for nome, prioridade in algoritmos.items():
    caminho, custo = busca(mapa_romenia, 'Arad', 'Bucharest', prioridade)
    print(f'{nome:15} {custo:3} km {len(caminho) - 1} passos')

# largura 450 km 3 passos
# custo uniforme 418 km 4 passos
# gulosa 450 km 3 passos
# A* 418 km 4 passos
