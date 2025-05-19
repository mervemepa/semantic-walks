from utils.semantic_drift import build_extended_graph, semantic_drift, labeled_path, multi_node_loop
from utils.concept_pools import concept_pools, expand_concept_pool
from utils.conceptnet import get_related_concepts
from utils.graph_builder import build_concept_graph, random_semantic_walk, hierarchy_pos, labeled_semantic_walk
import networkx as nx
import matplotlib.pyplot as plt

def main():
    start = "bird"
    end = "flying"
    depth = 1

    # 🔨 Ana grafı ilk başta kur
    print(f"\n🌐 Building graph from '{start}' with depth {depth}...")
    G = build_concept_graph(start, depth=depth)
    print(f"\n✅ Graph built: {len(G.nodes)} nodes, {len(G.edges)} edges")

    # 🧪 Semantic Drift Test
    print("\n🧪 Semantic Drift:")
    source_term = "nest"
    target_theme = concept_pools["technology"]
    G_ext = build_extended_graph([source_term] + target_theme, depth=2)
    drift_path = semantic_drift(G_ext, source_term, targets=target_theme, max_steps=6)
    if drift_path:
        for a, rel, b in labeled_path(G_ext, drift_path):
            print(f"{a} --[{rel}]--> {b}")
    else:
        print("No semantic drift path found.")

    # 🔁 Geliştirilmiş Çoklu Kavram Loop
    print("\n🔁 Multi-node Semantic Loop:")
    loop_nodes = ["air", "wind", "breath", "atmosphere", "oxygen", "gas"]
    accepted = {"IsA", "UsedFor", "HasProperty", "CapableOf", "AtLocation"}
    G_loop = build_extended_graph(loop_nodes, depth=3)

    loop = []
    for _ in range(10):
        loop = multi_node_loop(G_loop, nodes=loop_nodes, steps=6, accepted_relations=accepted)
        if loop:
            break

    if loop:
        for i in range(len(loop) - 1):
            a, b = loop[i], loop[i + 1]
            rel = G_loop.get_edge_data(a, b).get("label", "RelatedTo")
            print(f"{a} --[{rel}]--> {b}")
        print(f"✅ Loop completed: {loop[0]} → ... → {loop[-1]}")
    else:
        print("❌ No looped path found after 10 attempts.")

    # 📚 Havuz genişletme
    print("\n📚 Expanding concept pool: 'air'")
    expanded_air = expand_concept_pool(concept_pools["air"], per_word=5)
    for word in expanded_air:
        print("-", word)

    # 🌐 Görselleştirme için pozisyon
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

    # 🎲 Rastgele yürüyüş
    while True:
        print("\n🎲 Random semantic walk:")
        walk = labeled_semantic_walk(G, start, steps=4)
        print("\n🧭 Semantic Walk:")
        for a, rel, b in walk:
            print(f"{a} --[{rel}]--> {b}")
        again = input("\n↩️ Yeni bir yürüyüş için Enter’a bas, çıkmak için q yaz: ")
        if again.lower() == "q":
            break

    # 🌳 Görselleştirme
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
    plt.savefig("concept_graph.png")
    plt.show()

if __name__ == "__main__":
    main()