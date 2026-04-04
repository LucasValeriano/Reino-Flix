import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix 1: Convert local /js/ path to absolute production URL
old_js = '/js/bPHQIq3403556.js'
new_js = 'https://www.reinoplay.online/js/bPHQIq3403556.js'
html = html.replace(f'src="{old_js}"', f'src="{new_js}"')
html = html.replace(f"src='{old_js}'", f"src='{new_js}'")
print(f'JS path fixed: {old_js} -> {new_js}')

# Fix 2: Also check for any other relative /js/ or /css/ paths
relative_paths = re.findall(r'(?:src|href)="(/(?:js|css|images|assets)/[^"]+)"', html)
if relative_paths:
    print('Other relative paths found:')
    for p in relative_paths:
        full_url = f'https://www.reinoplay.online{p}'
        html = html.replace(f'"{p}"', f'"{full_url}"')
        print(f'  Fixed: {p} -> {full_url}')
else:
    print('No other relative paths found.')

# Save
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('\nDONE! index.html saved.')
print('Verify js reference is now absolute:', 'reinoplay.online/js/bPHQIq3403556' in open('index.html').read())
