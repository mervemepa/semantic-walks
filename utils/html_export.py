def export_loop_to_html(loop, G, filename="semantic_loop.html"):
    with open(filename, "w") as f:
        f.write("<html><head><meta charset='utf-8'><style>")
        f.write("""
            body { font-family: sans-serif; padding: 2em; background: #f9f9f9; }
            .relation { color: #999; margin: 0 0.5em; }
            .semantic-line { margin-bottom: 0.5em; }
            .loop-title { font-weight: bold; font-size: 1.2em; margin-bottom: 1em; }
        """)
        f.write("</style></head><body>")
        f.write("<div class='loop-title'>🌀 Semantic Loop</div>\n")
        for i in range(len(loop) - 1):
            a, b = loop[i], loop[i + 1]
            rel = G.get_edge_data(a, b).get("label", "RelatedTo")
            f.write(f"<div class='semantic-line'>{a} <span class='relation'>--[{rel}]--></span> {b}</div>\n")
        f.write("</body></html>")
