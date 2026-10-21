"""Remove the internal design notes (pins, panel, toolbar button and their JS) from a published page."""
import re
import sys

path = sys.argv[1]
s = open(path).read()
before = s

s = re.sub(r'\s*<button class="pin"[^>]*>\d+</button>', '', s)
s = re.sub(r'<aside class="notes-panel".*?</aside>\n*', '', s, flags=re.S)
# Drop the notes button, and the divider before it when nothing else follows.
s = re.sub(r'(\s*<span class="sep" aria-hidden="true"></span>)?\s*<button type="button" id="b-notes"[^>]*>[^<]*</button>(?=\s*</div>)',
           lambda m: '' if m.group(1) else '', s)
s = re.sub(r'\s*<button type="button" id="b-notes"[^>]*>[^<]*</button>', '', s)
s = s.replace(",bn=document.getElementById('b-notes'),panel=document.getElementById('notes')", '')
s = re.sub(r"\n[ \t]*function notes\(on\)\{.*", '', s)
s = re.sub(r"\n[ \t]*bn\.onclick=.*", '', s)
s = re.sub(r"\n[ \t]*document\.querySelectorAll\('\.pin'\)\.forEach.*", '', s)

left = [w for w in ('class="pin"', 'notes-panel"', 'b-notes', 'notes(') if w in s.split('</style>', 1)[-1]]
if left:
    sys.exit(f"strip-notes: still found {left} in {path}")
open(path, 'w').write(s)
