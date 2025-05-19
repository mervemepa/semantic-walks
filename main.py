
import matplotlib.pyplot as plt
import networkx as nx
from utils.conceptnet import get_related_concepts

def main():
    term = "bird"
    relations = get_related_concepts(term)

    print(f"\n📚 Relations for: {term}")
    for idx, (related, relation, source) in enumerate(relations, 1):
        print(f"{idx}. {source} --[{relation}]--> {related}")

if __name__ == "__main__":
    main()

from utils.graph_builder import build_concept_graph
import networkx as nx

def main():
    start = "bird"
    end = "flying"
    depth = 1

    print(f"\n🌐 Building graph from '{start}' with depth {depth}...")
    G = build_concept_graph(start, depth=depth)
    print(f"\n✅ Graph built: {len(G.nodes)} nodes, {len(G.edges)} edges")

    if end in G:
        try:
            path = nx.shortest_path(G, source=start, target=end)
            print(f"\n🔗 Path from '{start}' to '{end}':")
            for step in path:
                print(" →", step)
        except nx.NetworkXNoPath:
            print(f"\n🚫 No path found from '{start}' to '{end}'")
    else:
        print(f"\n⚠️ '{end}' not found in graph.")

    # 🔵 Grafı çizme kısmı BURADA olacak:
    pos = nx.spring_layout(G, seed=42)  # düğümlerin pozisyonu
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_size=800, node_color="lightblue",
            font_size=10, font_weight="bold", edge_color="gray")
    edge_labels = nx.get_edge_attributes(G, "label")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red")
    plt.title(f"Concept Graph from '{start}'")
    plt.axis("off")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()