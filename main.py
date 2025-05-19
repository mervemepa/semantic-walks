from utils.conceptnet import get_related_concepts

def main():
    term = "bird"
    relations = get_related_concepts(term)

    print(f"\n📚 Relations for: {term}")
    for idx, (related, relation, source) in enumerate(relations, 1):
        print(f"{idx}. {source} --[{relation}]--> {related}")

if __name__ == "__main__":
    main()