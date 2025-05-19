import random

def themed_semantic_walk(G, start, nodes, steps=5, accepted_relations=None):
    """
    Loop zorunluluğu olmadan, tematik kavramlar arasında yönlü bir semantik zincir üretir.
    Yalnızca belirli kavram havuzunda kalır (nodes).
    """
    path = [start]
    current = start

    for _ in range(steps):
        neighbors = list(G.successors(current))
        if accepted_relations:
            neighbors = [n for n in neighbors
                         if G.get_edge_data(current, n).get("label") in accepted_relations and n in nodes]
        else:
            neighbors = [n for n in neighbors if n in nodes]

        if not neighbors:
            break

        next_node = random.choice(neighbors)
        path.append(next_node)
        current = next_node

    return path if len(path) > 1 else []