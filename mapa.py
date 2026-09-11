# Arquivo: mapa.py
# Grafo nao dirigido: cada cidade aponta para a lista de (vizinho, km).
# Toda estrada aparece duas vezes, uma em cada ponta. Figura 3.2.

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
print(len(mapa_romenia), len(heuristica_bucareste))
# 20 20

# Acrescente ao final de mapa.py, no lugar do print de conferencia.
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

# So executa quando mapa.py e rodado diretamente; nao executa no import.
if __name__ == '__main__':
    print('cidades:', len(mapa_romenia)) # cidades: 20
    print(vizinhos_de(mapa_romenia, 'Sibiu')) # [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ...]
    print(vizinhos_de(mapa_romenia, 'Lugano')) # [] <- cidade inexistente nao quebra, gracas ao .get
    print(custo_do_caminho(mapa_romenia,['Arad', 'Sibiu', 'Fagaras', 'Bucharest'])) # 450 <- confira a mao: 140 + 99 + 211
    print(custo_do_caminho(mapa_romenia,['Arad', 'Sibiu', 'Rimnicu Vilcea','Pitesti', 'Bucharest'])) # 418 <- este e o caminho otimo, e o numero a decorar
