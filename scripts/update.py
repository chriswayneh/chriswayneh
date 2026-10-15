"""Regenerate Recently shipped and assets/languages.svg from public repo data. Stdlib only."""
import json, os, re, urllib.request
U = "chriswayneh"
H = {"Accept": "application/vnd.github+json", "User-Agent": U}
if os.environ.get("GH_TOKEN"): H["Authorization"] = "Bearer " + os.environ["GH_TOKEN"]
def get(p): return json.load(urllib.request.urlopen(urllib.request.Request("https://api.github.com/" + p, headers=H)))
repos = [r for r in get(f"users/{U}/repos?per_page=100&type=owner") if not (r["fork"] or r["archived"] or r["private"]) and r["name"] != U]
rel, lang = [], {}
for r in repos:
    for x in get(f"repos/{U}/{r['name']}/releases?per_page=3"):
        if not (x["draft"] or x["prerelease"]): rel.append((x["published_at"][:10], r["name"], x["tag_name"], x["html_url"]))
    for k, v in get(f"repos/{U}/{r['name']}/languages").items(): lang[k] = lang.get(k, 0) + v
rel.sort(reverse=True)
seen=set(); rel=[x for x in rel if not (x[1] in seen or seen.add(x[1]))]
block = "\n".join(f"- [{n} {t}]({u}) · {d}" for d, n, t, u in rel[:5])
s = open("README.md").read()
s = re.sub(r"(<!-- RECENT:START -->).*?(<!-- RECENT:END -->)", lambda m: m.group(1) + "\n" + block + "\n" + m.group(2), s, flags=re.S)
open("README.md", "w").write(s)
tot = sum(lang.values()); top = sorted(lang.items(), key=lambda kv: -kv[1])[:6]
C = ["#3572A5", "#3178c6", "#f1e05a", "#89e051", "#e34c26", "#427819"]
W, x, bar, leg = 480, 20, [], []
for i, (k, v) in enumerate(top):
    w = 440 * v / tot; bar.append(f'<rect x="{x:.1f}" y="44" width="{w:.1f}" height="10" fill="{C[i]}"/>'); x += w
    lx, ly = 20 + (i % 2) * 220, 82 + (i // 2) * 22
    leg.append(f'<circle cx="{lx+5}" cy="{ly-4}" r="5" fill="{C[i]}"/><text x="{lx+16}" y="{ly}">{k} {100*v/tot:.1f}%</text>')
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="150" viewBox="0 0 {W} 150" role="img" aria-label="Languages across public repos">
<style>text{{font:13px -apple-system,Segoe UI,Helvetica,Arial,sans-serif;fill:#57606a}}.t{{font-weight:600;font-size:15px;fill:#2f81f7}}</style>
<rect x="0.5" y="0.5" width="{W-1}" height="149" rx="6" fill="none" stroke="#8b949e" stroke-opacity="0.4"/>
<text class="t" x="20" y="30">Languages across public repos</text>
<clipPath id="c"><rect x="20" y="44" width="440" height="10" rx="5"/></clipPath><g clip-path="url(#c)">{"".join(bar)}</g>
{"".join(leg)}</svg>'''
os.makedirs("assets", exist_ok=True); open("assets/languages.svg", "w").write(svg)
