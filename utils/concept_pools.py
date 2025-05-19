from utils.conceptnet import get_related_concepts

# 🧠 Tanımlı Tematik Kavram Havuzları
concept_pools = {
    "nature": ["forest", "nest", "stone"],
    "air": ["wind", "breath", "atmosphere"],
    "technology": ["circuit", "signal", "machine"]
}

def expand_concept_pool(pool, depth=1, per_word=5):
    """
    Belirli bir kavram havuzunu, ConceptNet üzerinden genişletir.
    Her kavram için `per_word` kadar ilişkili kavram alır.
    """
    expanded = set(pool)
    for term in pool:
        try:
            related = get_related_concepts(term, limit=per_word)
            expanded.update([target for target, _, _ in related])
        except Exception as e:
            print(f"[!] Failed to expand '{term}': {e}")
    return list(expanded)