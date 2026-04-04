import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Achar referencias a JS locais (sem http)
local_js = re.findall(r'<script[^>]+src="([^"]+)"', html)
local_css = re.findall(r'<link[^>]+href="([^"]+)"', html)

print('=== Todos os JS ===')
for js in local_js:
    if not js.startswith('http'):
        print('  [LOCAL 404?]', js)
    else:
        print('  [CDN OK]    ', js[:80])

print()
print('=== Todos os CSS ===')
for css in local_css:
    if not css.startswith('http'):
        print('  [LOCAL 404?]', css)
    else:
        print('  [CDN OK]    ', css[:80])
