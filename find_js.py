import re

with open('production.html', 'r', encoding='utf-8') as f:
    prod = f.read()

# Find bPHQIq3403556 context
idx = prod.find('bPHQIq3403556')
print('Context in production.html:')
print(repr(prod[max(0, idx-200):idx+300]))
print()

# Find all script src tags
scripts = re.findall(r'<script[^>]+src="([^"]*bPHQIq[^"]*)"', prod)
print('Scripts with bPHQIq:', scripts)

# Find ALL src attributes
all_srcs = re.findall(r'src="([^"]+)"', prod)
for s in all_srcs:
    if 'bPHQIq' in s or '.js' in s:
        print('SRC:', s)
