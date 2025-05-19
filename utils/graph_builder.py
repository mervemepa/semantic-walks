import networkx as nx
from utils.conceptnet import get_related_concepts
import time

def build_concept_graph(start_term, depth=2, lang="en", delay=1.0):
    """
    ConceptNet'ten başlayarak ilişkileri çekip bir NetworkX grafı oluşturur.
    depth: kaç adım ileri gideceği (1 = sadece komşular, 2 = komşuların komşusu...)
    delay: API sorguları arası bekleme süresi (rate limit'e yakalanmamak için)
    """
    G = nx.DiGraph()
    visited = set()
    frontier = [(start_term, 0)]

    while frontier:
        current_term, level = frontier.pop(0)

        if level > depth or current_term in visited:
            continue

        visited.add(current_term)

        try:
            relations = get_related_concepts(current_term, lang=lang, limit=10)
        except Exception as e:
            print(f"[!] API error for {current_term}: {e}")
            continue

        for target, relation, source in relations:
            G.add_edge(source, target, label=relation)
            print(f"📎 {source} --[{relation}]--> {target}")
            if target not in visited:
                frontier.append((target, level + 1))

        time.sleep(delay)  # API'yi çok sık vurmayı önler

    return G