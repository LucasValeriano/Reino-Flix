import re

def fix_html_encoding(filename):
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Mapeamento de corrupções UTF-8 -> Latin1 mal interpretadas
    replacements = {
        'Ã“': 'Ó',
        'Ã³': 'ó',
        'Ã”': 'Ô',
        'Ã´': 'ô',
        'Ã¡': 'á',
        'Ã€': 'À',
        'Ã ': 'à',
        'Ã©': 'é',
        'ÃŠ': 'Ê',
        'Ãª': 'ê',
        'Ã­': 'í',
        'Ã': 'Í',
        'Ãº': 'ú',
        'Ãµ': 'õ',
        'Ã£': 'ã',
        'Ã§': 'ç',
        'Ã‡': 'Ç',
        'BÃ“': 'BÔ', # Caso específico de BÔNUS as vezes vindo como BÃ"NUS
        'BÃ"': 'BÔ',
        'BÃ”NUS': 'BÔNUS',
        'PRÃ“XIMO': 'PRÓXIMO',
        'HistÃ³rias': 'Histórias',
        'crianÃ§a': 'criança',
        'vocÃª': 'você'
    }

    # First, move meta charset to line 2
    # Find existing <meta charset="utf-8">
    content = re.sub(r'<meta charset="utf-8">', '', content)
    # Insert after <head>
    content = content.replace('<head>', '<head>\n<meta charset="utf-8">')

    # Apply replacements
    for corrupt, correct in replacements.items():
        content = content.replace(corrupt, correct)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    fix_html_encoding('index.html')
