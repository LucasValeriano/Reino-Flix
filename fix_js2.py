with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the local JS path to absolute production URL
old_ref = 'src="/js/bPHQIq3403556.js"'
new_ref = 'src="https://www.reinoplay.online/js/bPHQIq3403556.js"'
count = html.count(old_ref)
html = html.replace(old_ref, new_ref)
print(f'Replaced {count} occurrence(s)')
print(f'Verified: {new_ref in html}')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Done.')
