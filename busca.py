# Arquivo: busca.py
from mapa import mapa_romenia

def busca_generica(grafo, inicio, objetivo):
    """Esqueleto de busca com contador de nós expandidos."""
    fronteira = [(0, inicio, [inicio])]  # (valor, cidade, caminho)
    visitados = set()
    nos_expandidos = 0

    while fronteira:
        fronteira.sort(key=lambda item: item[0])
        valor, atual, caminho = fronteira.pop(0)

        # Só conta como nó expandido quando ele realmente sai da fronteira para ser processado
        nos_expandidos += 1
        print(f'expandindo {atual:16} valor={valor}')

        if atual == objetivo:  # teste de objetivo
            print(f'Total de nós expandidos: {nos_expandidos}')
            return caminho, valor, nos_expandidos

        if atual not in visitados:
            visitados.add(atual)
            for vizinho, custo in grafo.get(atual, []):
                if vizinho not in visitados:
                    fronteira.append((valor + custo, vizinho, caminho + [vizinho]))

    print(f'Total de nós expandidos: {nos_expandidos}')
    return None, float('inf'), nos_expandidos

if __name__ == '__main__':
    caminho, custo, expandidos = busca_generica(mapa_romenia, 'Arad', 'Bucharest')
    print(' -> '.join(caminho))
    print(f'{custo} km em {len(caminho) - 1} passos')
    print(f'Número para anotação: {expandidos} nós expandidos')