# Semantic Walks

This project explores the construction of semantic networks through ConceptNet API to generate conceptual walks between words. It forms the foundation for a dynamic manifesto system by navigating meaningful paths between concepts, which can later be integrated with textual or media-based artistic expressions.

## 🔍 Project Structure

semantic-walks/
│
├── main.py # Core script to build graph and run semantic walks
├── requirements.txt # Required Python packages
├── README.md # You’re reading this!
│
├── utils/
│ ├── conceptnet.py # Functions for querying ConceptNet API
│ └── graph_builder.py # Functions for building graphs and semantic walks
│
└── conceptnet_cache.sqlite # Local cache of API requests (auto-generated)

---

## ⚙️ Installation

Create a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Usage

Run the main script:

python3 main.py

You will see:
	•	ConceptNet graph construction from a starting word
	•	Shortest semantic path to a target word
	•	Randomized conceptual walks with semantic relationships
	•	Optional: a hierarchical visualization of the concept graph

Press Enter to generate a new walk or q to exit and view the graph.

Semantic Walk Format

Each walk represents a meaningful traversal of the ConceptNet graph:
bird --[RelatedTo]--> nest
nest --[AtLocation]--> tree
tree --[UsedFor]--> shade
These relationships are sourced live (or from cache) and can serve as narrative seeds.

API Caching

All ConceptNet queries are locally cached using requests-cache:
	•	Cache file: conceptnet_cache.sqlite
	•	Located in the root directory
	•	Ensures faster access and enables offline exploration

Artistic Intent

This system was initially developed in relation to the Sub-Net Manifest project, which organized concept pools into dynamic manifesto sentences. By integrating ConceptNet’s semantic infrastructure, we aim to:
	•	Enrich the vocabulary of manifestos
	•	Allow thematic and relational expansion of concepts
	•	Generate live or pre-structured narrative texts
	•	Potentially associate semantic paths with audio/visual media

    Author

Developed by Merve Mepa
With support from GPT-based semantic engineering experiments 🌱
```
