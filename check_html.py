import sys

def check_html(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    stack = []
    # Simplified parser to count divs
    tags = content.split('<')
    for tag in tags[1:]:
        if tag.startswith('div'):
            # Check if it's an opening tag
            if not tag.startswith('div/'): # primitive check
                stack.append('div')
        elif tag.startswith('/div'):
            if stack:
                stack.pop()
            else:
                print("Extra closing div found!")
    
    print(f"Total open divs: {len(stack)}")
    if stack:
        print("Missing closing divs for index:", stack)

if __name__ == "__main__":
    check_html(sys.argv[1])
