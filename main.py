from utils.conceptnet import get_related_concepts
from utils.graph_builder import build_concept_graph, random_semantic_walk, hierarchy_pos, labeled_semantic_walk
import networkx as nx
import matplotlib.pyplot as plt

def main():
    start = "bird"
    end = "flying"
    depth = 1

    print(f"\n🌐 Building graph from '{start}' with depth {depth}...")
    G = build_concept_graph(start, depth=depth)
    print(f"\n✅ Graph built: {len(G.nodes)} nodes, {len(G.edges)} edges")

    if start in G:
        pos = hierarchy_pos(G, start)
    else:
        pos = nx.spring_layout(G, seed=42)

    # 🔗 En kısa yol
    if end in G:
        try:
            path = nx.shortest_path(G, source=start, target=end)
            print(f"\n🔗 Shortest path from '{start}' to '{end}':")
            for step in path:
                print(" →", step)
        except nx.NetworkXNoPath:
            print(f"\n🚫 No path found from '{start}' to '{end}'")
    else:
        print(f"\n⚠️ '{end}' not found in graph.")

    # 🎲 Rastgele yürüyüş
    while True:
        print("\n🎲 Random semantic walk:")
        from utils.graph_builder import labeled_semantic_walk  # import etmeyi unutma

        walk = labeled_semantic_walk(G, start, steps=4)
        print("\n🧭 Semantic Walk:")
        for a, rel, b in walk:
            print(f"{a} --[{rel}]--> {b}")
        again = input("\n↩️ Yeni bir yürüyüş için Enter’a bas, çıkmak için q yaz: ")
        if again.lower() == "q":
            break

    # 🌳 Hiyerarşik çizim (dosya yapısı gibi)
    

    plt.figure(figsize=(12, 8))
    nx.draw_networkx_nodes(G, pos, nodelist=pos.keys(), node_size=800, node_color="lightblue")
    nx.draw_networkx_labels(G, pos, labels={k: k for k in pos})
    nx.draw_networkx_edges(G, pos, edgelist=[(u, v) for u, v in G.edges() if u in pos and v in pos], edge_color="gray")
    edge_labels = nx.get_edge_attributes(G, "label")
    filtered_edge_labels = {(u, v): label for (u, v), label in edge_labels.items() if u in pos and v in pos}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=filtered_edge_labels, font_color="red")
    plt.title(f"Concept Hierarchy from '{start}'")
    plt.axis("off")
    plt.tight_layout()
    plt.show()

    plt.tight_layout()
    plt.savefig("concept_graph.png")  # ← Buraya ekle
    plt.show()

if __name__ == "__main__":
    main()