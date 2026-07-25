import html, re, sys
from pathlib import Path
from urllib.parse import unquote
bundle = html.unescape(Path(sys.argv[1]).read_text(errors='replace'))
platform = sys.argv[2]
product = sys.argv[3]

# Normalize escaped slashes sometimes found in JS string literals.
text = bundle.replace('\\/', '/')

def fail(msg):
    raise SystemExit(msg)

def version_from_url(url):
    decoded = unquote(url)
    # Known current layouts include antigravity-hub/<version>/ and stable/<version>/.
    for pattern in (r'/antigravity-hub/([^/]+)/', r'/stable/([^/]+)/', r'/(\d+\.\d+\.\d+(?:-[^/]+)?)/'):
        m = re.search(pattern, decoded)
        if m:
            return m.group(1).split('-', 1)[0]
    return 'unknown'

if product == 'desktop':
    marker = 'id:"antigravity-2"'
    next_marker = 'id:"antigravity-cli"'
    filename_patterns = [r'Antigravity\.tar\.gz']
    label = 'Antigravity 2.0'
elif product == 'ide':
    marker = 'id:"antigravity-ide"'
    next_marker = 'id:"antigravity-sdk"'
    filename_patterns = [r'Antigravity%20IDE\.tar\.gz', r'Antigravity\+IDE\.tar\.gz', r'Antigravity IDE\.tar\.gz']
    label = 'Antigravity IDE'
else:
    fail(f'Unknown product: {product}')

sections = []
start = text.find(marker)
if start != -1:
    end = text.find(next_marker, start)
    sections.append(text[start:end if end != -1 else None])
sections.append(text)

for section in sections:
    for filename_re in filename_patterns:
        pattern = r'https?://[^"\'\s<>)]*/' + re.escape(platform) + r'/' + filename_re
        matches = re.findall(pattern, section)
        if matches:
            url = matches[-1]
            print(version_from_url(url), url)
            sys.exit(0)

fail(f'Could not find official {label} tarball for {platform} in Google download bundle')