import re

# Lê o HTML da produção (baixado)
with open('production.html', 'r', encoding='utf-8') as f:
    prod_html = f.read()

# Lê o HTML local para pegar os nossos fixes de CSS e Script
with open('index.html', 'r', encoding='utf-8') as f:
    local_html = f.read()

# Extrai nosso bloco de CSS mobile
css_pattern = r'<style id="antigravity-mobile-fixes">.*?</style>'
css_match = re.search(css_pattern, local_html, re.DOTALL)

# Extrai nosso script booster
script_pattern = r'<script>\s*/\* REINOPLAY BOOSTER.*?</script>'
script_match = re.search(script_pattern, local_html, re.DOTALL)

our_css = css_match.group(0) if css_match else ''
our_script = script_match.group(0) if script_match else ''

print('CSS block found:', bool(our_css))
print('Script block found:', bool(our_script))
print()

# Map de UUIDs quebrados -> funcionais
uuid_map = {
    'c9fa452c-2227-402b-b812-54e545ce8bc5': '4aabe8ea-ac53-4543-89b5-7d52cf316705',
    'd72f8836-e696-489e-8730-80a91f544605': 'ba2ee446-52fc-4cb3-b88a-5d4832e204f5',
    '8334460b-8d18-4720-9988-cb9477038e24': '29acdcb9-7cf4-431a-9c15-ed8d90bd37ea',
    '8593457a-df28-498c-859a-115857209999': '4aabe8ea-ac53-4543-89b5-7d52cf316705',
    '3d516246-8051-4089-8089-ea3186851253': 'ba2ee446-52fc-4cb3-b88a-5d4832e204f5',
    '5139045b-389f-410a-810a-31a89045b410': '29acdcb9-7cf4-431a-9c15-ed8d90bd37ea',
}

new_html = prod_html
for old, new in uuid_map.items():
    count = new_html.count(old)
    if count:
        new_html = new_html.replace(old, new)
        print(f'Replaced {count}x {old[:8]}... -> {new[:8]}...')

# Injeta CSS e Script antes de </body>
injection = '\n'
if our_css:
    injection += our_css + '\n'
if our_script:
    injection += our_script + '\n'

if '</body>' in new_html:
    new_html = new_html.replace('</body>', injection + '</body>', 1)
    print('Injected CSS+Script before </body>')
elif '</html>' in new_html:
    new_html = new_html.replace('</html>', injection + '</html>', 1)
    print('Injected CSS+Script before </html>')

# Salva
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print()
print(f'DONE! index.html = {len(new_html)} bytes')
print(f'New UUIDs present (4aabe8ea): {new_html.count("4aabe8ea-ac53-4543-89b5-7d52cf316705")}')
print(f'Old UUIDs remaining (c9fa452c): {new_html.count("c9fa452c-2227-402b-b812-54e545ce8bc5")}')
