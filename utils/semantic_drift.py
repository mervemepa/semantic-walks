import random
import networkx as nx
from utils.conceptnet import get_related_concepts
from utils.graph_builder import build_concept_graph



def multi_node_loop(G, nodes, steps=5, accepted_relations=None):
    """
    Belirli bir kavram kümesi içinde döngüsel bir yürüyüş yapar.
    Yürüyüş başladığı kavrama geri dönerse başarılı kabul edilir.
    accepted_relations: geçerli ilişki türleri (örn: {"IsA", "UsedFor"})
    """
    start = random.choice(nodes)
    path = [start]
    current = start

    for _ in range(steps):
        neighbors = list(G.successors(current))
        if accepted_relations:
            neighbors = [
                n for n in neighbors
                if G.get_edge_data(current, n).get("label") in accepted_relations and n in nodes
            ]
        else:
            neighbors = [n for n in neighbors if n in nodes]

        if not neighbors:
            return []
        next_node = random.choice(neighbors)
        path.append(next_node)
        current = next_node

    # Döngü tamamlandıysa
    if path[-1] == path[0]:
        return path
    else:
        return []

def looped_drift(G, start, steps=6, accepted_relations=None):
    """
    Başlangıç kavramından çıkıp yine aynı kavrama dönen semantik bir döngü üretir.
    steps: ara adım sayısı (başlangıç ve kapanış hariç)
    accepted_relations: filtrelemek istenen ilişki türleri (set)
    """
    path = [start]
    current = start

    for _ in range(steps):
        neighbors = list(G.successors(current))
        if accepted_relations:
            neighbors = [n for n in neighbors
                         if G.get_edge_data(current, n).get("label") in accepted_relations]
        if not neighbors:
            return []
        next_node = random.choice(neighbors)
        path.append(next_node)
        current = next_node

    if start in G.successors(current):
        path.append(start)
        return path
    else:
        return []  # döngü tamamlanamıyorsa boş dön

def build_extended_graph(core_terms, depth=2):
    """
    Verilen kelime listesi üzerinden genişletilmiş bir kavramsal ağ kurar.
    """
    G = nx.DiGraph()
    for term in core_terms:
        subgraph = build_concept_graph(term, depth=depth)
        G.update(subgraph)
    return G

def semantic_drift(G, start, targets, max_steps=8):
    """
    Verilen graf üzerinde, bir kavramdan başlayarak hedef temaya yürüyen bir yol bulur.
    """
    for target in targets:
        if target not in G:
            continue
        try:
            path = nx.shortest_path(G, source=start, target=target)
            if len(path) <= max_steps:
                return path
        except nx.NetworkXNoPath:
            continue
    return []

def labeled_path(G, path):
    """
    Verilen yol içindeki her adımı ilişki etiketiyle birlikte döner.
    """
    labeled = []
    for i in range(len(path) - 1):
        source = path[i]
        target = path[i + 1]
        relation = G.get_edge_data(source, target).get("label", "RelatedTo")
        labeled.append((source, relation, target))
    return labeled