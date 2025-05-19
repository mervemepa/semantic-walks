import requests
import requests_cache

# Cache sistemi aktif: aynı sorgu bir daha yapılmaz, dosyadan okunur
requests_cache.install_cache("conceptnet_cache", expire_after=86400)

BASE_URL = "http://api.conceptnet.io"



def get_related_concepts(term, lang="en", limit=20):
    """
    Verilen terimle ilişkili kavramları ConceptNet üzerinden getirir.
    """
    term = term.lower().replace(" ", "_")
    url = f"{BASE_URL}/c/{lang}/{term}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Hata: {response.status_code}")
        return []
    
    data = response.json()
    edges = data.get("edges", [])
    
    related = []
    for edge in edges[:limit]:
        start = edge.get("start", {}).get("label", "")
        end = edge.get("end", {}).get("label", "")
        rel = edge.get("rel", {}).get("label", "")
        
        if start.lower() != term:
            related.append((start, rel, end))
        else:
            related.append((end, rel, start))
    
    return related