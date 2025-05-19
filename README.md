# Semantic Walks

This project explores the construction of semantic networks through ConceptNet API to generate conceptual walks between words. It forms the foundation for a dynamic manifesto system by navigating meaningful paths between concepts, which can later be integrated with textual or media-based artistic expressions.

## 🔍 Project Structure

```
semantic-walks/
│
├── main.py                      # Core script to build graph and run semantic walks
├── requirements.txt             # Required Python packages
├── README.md                    # You're reading this!
│
├── utils/
│   ├── conceptnet.py            # Functions for querying ConceptNet API
│   ├── graph_builder.py         # Functions for building graphs and semantic walks
│   └── concept_pools.py         # Thematic concept clusters and expansion logic
│
└── conceptnet_cache.sqlite      # Local cache of API requests (auto-generated)
```

---

## ⚙️ Installation

Create a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🚀 Usage

Run the main script:

```bash
python3 main.py
```

You will see:

- ConceptNet graph construction from a starting word
- Shortest semantic path to a target word
- Randomized conceptual walks with semantic relationships
- Optional: a hierarchical visualization of the concept graph

Press `Enter` to generate a new walk or `q` to exit.

---

## 🧐 Semantic Walk Format

Each walk represents a meaningful traversal of the ConceptNet graph:

```
bird --[RelatedTo]--> nest
nest --[AtLocation]--> tree
tree --[UsedFor]--> shade
```

These relationships are sourced live (or from cache) and can serve as narrative seeds.

---

## 📦 API Caching

All ConceptNet queries are locally cached using `requests-cache`:

- Cache file: `conceptnet_cache.sqlite`
- Located in the root directory
- Ensures faster access and enables offline exploration

---

## 💡 Concept Pools (NEW!)

You can define your own semantic "theme pools" like so:

```python
concept_pools = {
    "nature": ["forest", "nest", "stone"],
    "air": ["wind", "breath", "atmosphere"],
    "technology": ["circuit", "signal", "machine"]
}
```

Then dynamically expand them via ConceptNet:

```python
expanded_air = expand_concept_pool(concept_pools["air"], per_word=5)
```

This creates a live-growing vocabulary for each theme.

---

## 🔄 Roadmap / Modular Layers

This project is structured to grow in modular layers:

1. **Semantic Graph & Walk** – foundation (complete)
2. **Concept Pool Expansion** – thematic clustering (in progress)
3. **Semantic Drift Engine** – bridging themes with narrative transitions (next)
4. **Manifest Generator** – walk-based sentence generation
5. **Media Mapping** – audiovisual pairing for each concept
6. **Interface Layer** – terminal, web, or installation interface

---

## 👩‍💻 Author

Developed by Merve Yılmaz
With support from GPT-based semantic engineering experiments 🌱
