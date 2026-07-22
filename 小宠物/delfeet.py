import os
P = os.path.expanduser("~/Documents/小宠物/index.html")
c = open(P, encoding="utf-8").read()
# Find and remove the two foot lines
old = '<line x1="8" y1="95" x2="22" y2="95" stroke="#666" stroke-width="2.5" stroke-linecap="round"/>\n      <line x1="42" y1="95" x2="56" y2="95" stroke="#666" stroke-width="2.5" stroke-linecap="round"/>'
if old in c:
    c = c.replace(old, "")
    open(P, "w", encoding="utf-8").write(c)
    print("Feet removed!")
else:
    print("Pattern not found")
    # Debug: show the SVG area
    idx = c.find("<line class=")
    if idx >= 0:
        print(c[idx:idx+300])
