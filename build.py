# Rebuilds index.html from src/page.html by putting the base64 images back in.
import json
blobs = json.load(open("src/blobs.json"))
items = blobs if isinstance(blobs, list) else [blobs[k] for k in sorted(blobs)]
html = open("src/page.html").read()
for i, b in enumerate(items):
    html = html.replace(f"__BLOB_{i}__", b)
open("index.html", "w").write(html)
print("wrote index.html")
