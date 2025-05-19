import requests
import requests_cache

# Cache sistemi aktif: aynı sorgu bir daha yapılmaz, dosyadan okunur
requests_cache.install_cache("conceptnet_cache", expire_after=86400)

BASE_URL = "http://api.conceptnet.io"



def get_related_concepts(term, lang="en", limit=10):
    """
    ConceptNet API üzerinden verilen bir kavramla ilişkili kavramları çeker.
    Sadece İngilizce kavramları döndürür.
    """
    url = f"https://api.conceptnet.io/c/{lang}/{term}?offset=0&limit={limit}"
    response = requests.get(url)
    data = response.json()

    edges = []
    for edge in data.get("edges", []):
        rel = edge.get("rel", {}).get("label")
        start = edge.get("start", {}).get("term")
        end = edge.get("end", {}).get("term")

        # Sadece İngilizce kavramları al
        if start.startswith("/c/en/") and end.startswith("/c/en/"):
            source = start.split("/")[3]
            target = end.split("/")[3]
            edges.append((target, rel, source))
    return edges