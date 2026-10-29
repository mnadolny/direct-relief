"""Remove internal preview chrome from a published page: the design notes (pins, panel, their JS) and the preview toolbar."""
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

# The preview toolbar (version tag, compare link, desktop/375 and labels toggles) is for us, not the client.
s = re.sub(r'<div class="toolbar".*?</div>\n*', '', s, flags=re.S)
s = re.sub(r'\n[ \t]*// toolbar\n.*?\n(?=\n)', '', s, flags=re.S)
s = re.sub(r'\n(\.toolbar|@media \(max-width:560px\)\{#b-desk)[^\n]*', '', s)

left = [w for w in ('class="pin"', 'notes-panel"', 'b-notes', 'notes(', 'class="toolbar"', 'b-desk', 'b-eye') if w in s.split('</style>', 1)[-1]]
if left:
    sys.exit(f"strip-notes: still found {left} in {path}")
open(path, 'w').write(s)
