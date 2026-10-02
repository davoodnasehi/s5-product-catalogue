import os, re, json, glob, sys

REPO = r"C:/Users/DN/s5-product-catalogue"
FORBIDDEN = ["boltight", "boltight", "nord-lock", "nordlock"]

files = []
for root, dirs, fs in os.walk(REPO):
    if ".git" in root:
        continue
    for f in fs:
        if f.lower().endswith((".html", ".css", ".json", ".xml", ".txt", ".md")):
            files.append(os.path.join(root, f))

problems = []
print("=== forbidden-term scan ===")
hits = 0
for f in files:
    t = open(f, encoding="utf-8").read().lower()
    for w in FORBIDDEN:
        if w in t:
            hits += 1
            problems.append(f"FORBIDDEN '{w}' in {f}")
print(f"  scanned {len(files)} files, {hits} hits")

print("\n=== page inventory ===")
pages = sorted(glob.glob(os.path.join(REPO, "products", "*.html")))
print(f"  product pages: {len(pages)}")
for p in pages:
    print("   ", os.path.basename(p), os.path.getsize(p), "bytes")

print("\n=== per-page section check ===")
req = ["The problem", "plain language", "specifications", "Where it is used",
       "Who this is for"]
for p in pages:
    t = open(p, encoding="utf-8").read()
    missing = [r for r in req if r.lower() not in t.lower()]
    cta = re.search(r'<section class="cta".*?</section>', t, re.S)
    cta_links = len(re.findall(r'href="mailto:', cta.group(0) if cta else ""))
    img = re.findall(r'<img src="([^"]+)"', t)
    img_exists = all(os.path.exists(os.path.normpath(os.path.join(os.path.dirname(p), u)))
                     for u in img)
    noindex = "noindex" in t
    h2s = re.findall(r'<h2><span class="n">(\d+)</span>([^<]+)</h2>', t)
    status = "OK" if not missing else f"MISSING {missing}"
    print(f"  {os.path.basename(p):34s} {status:18s} sections={len(h2s)} "
          f"cta_links={cta_links} imgs_ok={img_exists} noindex={noindex}")
    if missing:
        problems.append(f"{p} missing sections {missing}")
    if cta_links != 1:
        problems.append(f"{p} has {cta_links} CTAs (expected 1)")
    if not img_exists:
        problems.append(f"{p} broken image refs")
    if len(h2s) < 6:
        problems.append(f"{p} only {len(h2s)} numbered sections")

print("\n=== index check ===")
idx = open(os.path.join(REPO, "index.html"), encoding="utf-8").read()
print("  cards:", len(re.findall(r'<article class="card"', idx)))
print("  links to product pages:", len(re.findall(r'href="products/', idx)))
held_linked = "bolt-tension-monitor" in idx
print("  held page linked from index:", held_linked)
if held_linked:
    problems.append("held page is linked from the catalogue index")

print("\n=== manifest ===")
man = json.load(open(os.path.join(REPO, "manifest.json"), encoding="utf-8"))
print("  pages:", len(man["pages"]))
for pg in man["pages"]:
    print("   ", pg["slug"], "|", pg["promotion_status"], "|", pg["cta_kind"],
          "|", pg["triage_verdict"], "| noindex", pg["noindex"])

print("\n=== html tag balance (rough) ===")
for p in pages + [os.path.join(REPO, "index.html")]:
    t = open(p, encoding="utf-8").read()
    opens = len(re.findall(r"<(section|div|table|article|main|header|footer)\b", t))
    closes = len(re.findall(r"</(section|div|table|article|main|header|footer)>", t))
    ok = "OK" if opens == closes else "MISMATCH"
    print(f"  {os.path.basename(p):34s} open={opens} close={closes} {ok}")
    if opens != closes:
        problems.append(f"{p} unbalanced block tags {opens}/{closes}")

print("\n=== RESULT ===")
if problems:
    for x in problems:
        print("  FAIL:", x)
    sys.exit(1)
print("  all checks passed")
