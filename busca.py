# Arquivo: busca.py - deve ficar na MESMA pasta de mapa.py
from mapa import mapa_romenia

def busca_generica(grafo, inicio, objetivo):
    """Esqueleto de busca: quem define o algoritmo e a ordem da fronteira."""
    fronteira = [(0, inicio, [inicio])] # (valor, cidade, caminho)
    visitados = set()

    while fronteira:
        fronteira.sort(key=lambda item: item[0])
        valor, atual, caminho = fronteira.pop(0)
        print(f'expandindo {atual:16} valor={valor}')

        if atual == objetivo: # teste de objetivo
            return caminho, valor

        if atual not in visitados:
            visitados.add(atual)
            for vizinho, custo in grafo.get(atual, []):
                if vizinho not in visitados:
                    fronteira.append((valor + custo, vizinho, caminho + [vizinho]))

    return None, float('inf') # fronteira vazia: falhou

if __name__ == '__main__':
    caminho, custo = busca_generica(mapa_romenia, 'Arad', 'Bucharest')
    print(' -> '.join(caminho))
    print(f'{custo} km em {len(caminho) - 1} passos')

# ... (as primeiras expansoes) ...
# expandindo Craiova valor=366
# expandindo Drobeta valor=374
# expandindo Bucharest valor=418
# Arad -> Sibiu -> Rimnicu Vilcea -> Pitesti -> Bucharest
# 418 km em 4 passos