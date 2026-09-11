# Arquivo: mapa.py

mapa_romenia = {
 'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
 'Zerind': [('Arad', 75), ('Oradea', 71)],
 'Oradea': [('Zerind', 71), ('Sibiu', 151)],
 'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
 'Timisoara': [('Arad', 118), ('Lugoj', 111)],
 'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
 'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
 'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
 'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
 'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
 'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
 'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
 'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
 'Giurgiu': [('Bucharest', 90)],
 'Urziceni': [('Bucharest', 85), ('Vaslui', 142), ('Hirsova', 98)],
 'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
 'Eforie': [('Hirsova', 86)],
 'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
 'Iasi': [('Vaslui', 92), ('Neamt', 87)],
 'Neamt': [('Iasi', 87)],
}
# h(n) = distancia em linha reta ate Bucareste. Figura 3.22.
heuristica_bucareste = {
 'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242,
 'Eforie': 161, 'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151,
 'Iasi': 226, 'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234,
 'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193, 'Sibiu': 253,
 'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374,
}

def vizinhos_de(grafo, cidade):
    """Devolve a lista de (vizinho, custo) de uma cidade."""
    return grafo.get(cidade, [])

def custo_do_caminho(grafo, caminho):
    """Soma o custo real das arestas de um caminho ja pronto."""
    total = 0
    for i in range(len(caminho) - 1):
        for vizinho, custo in grafo[caminho[i]]:
            if vizinho == caminho[i + 1]:
                total += custo
                break
    return total

def grau(grafo):
    """Devolve um dicionario com o numero de vizinhos de cada cidade."""
    return {cidade: len(vizinhos) for cidade, vizinhos in grafo.items()}

def cidades_alcancaveis(grafo, inicio, k):
    """Devolve o conjunto de cidades alcançáveis a partir de `inicio` em até `k` passos."""
    visitados = {inicio}
    fila = [inicio]

    for passo in range(k):
        proxima_fila = []
        for cidade in fila:
            for vizinho, passo in grafo.get(cidade, []):
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    proxima_fila.append(vizinho)
        fila = proxima_fila  # avança para o próximo nível/passo

    return visitados


def verificar_e_corrigir_simetria(grafo):
    """Verifica se o grafo é simétrico e corrige se necessário."""
    faltantes = []

    # 1. Identifica arestas que não possuem a volta correspondente
    for origem, vizinhos in list(grafo.items()):
        for destino, custo in vizinhos:
            vizinhos_destino = grafo.get(destino, [])
            if (origem, custo) not in vizinhos_destino:
                faltantes.append((origem, destino, custo))

    # 2. Diagnóstico e Correção
    if not faltantes:
        print("\nO grafo JÁ É SIMÉTRICO: todas as conexões possuem ida e volta iguais.")
        return True

    print(f"\nO grafo NÃO é simétrico! Encontradas {len(faltantes)} arestas sem a volta:")
    for orig, dest, c in faltantes:
        print(f"  - Falta a volta de ({dest} -> {orig}) com custo {c}")

    # Realiza as correções necessárias
    for orig, dest, c in faltantes:
        if dest not in grafo:
            grafo[dest] = []
        grafo[dest].append((orig, c))
    return True

if __name__ == '__main__':
    print('\nQuantidade de Cidades na Romênia:', len(mapa_romenia), '\n')

    resultado = grau(mapa_romenia)

    # Saída da quantidade de cidades da Romênia. Além disso, mostra a quantidade de vizinhos em Ordem Alfabética.
    for cidade in sorted(resultado):
        print(f'{cidade:16}: {resultado[cidade]} vizinhos')

    # Saída das cidades com os maiores e menores números de conexões.
    mais_estradas = max(resultado, key=resultado.get)
    menos_estradas = min(resultado, key=resultado.get)
    print(f"\nMaior número de conexões: {mais_estradas} ({resultado[mais_estradas]})")
    print(f"Menor número de conexões: {menos_estradas} ({resultado[menos_estradas]})")

    # Saída dos possíveis caminhos em no máximo dois passos saindo de Arad.
    alcancaveis = cidades_alcancaveis(mapa_romenia, 'Arad', 2)
    print("\nCidades alcançáveis a partir de Arad em no máximo 2 passos:")
    print(alcancaveis)

    verificar_e_corrigir_simetria(mapa_romenia)
