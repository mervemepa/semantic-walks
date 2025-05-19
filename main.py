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
    end = "flying"   # veya "sky", "nest", "animal"
    depth = 1     # istersen sonra 2 yaparız

    print(f"\n🌐 Building graph from '{start}' with depth {depth}...")
    G = build_concept_graph(start, depth=depth)

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

if __name__ == "__main__":
    main()