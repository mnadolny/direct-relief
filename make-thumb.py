"""Capture a full-page desktop thumbnail of a published version: python3 make-thumb.py v6"""
import os
import shutil
import subprocess
import sys
import tempfile

from PIL import Image

CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
STAGE = (217, 215, 209)  # --chrome, the grey around the page
WIDTH, THUMB_W = 1440, 480  # CSS px of the layout, px of the thumbnail

here = os.path.dirname(os.path.abspath(__file__))
v = sys.argv[1]
page = os.path.join(here, v, 'index.html')
os.makedirs(os.path.join(here, 'thumbs'), exist_ok=True)
tmp = tempfile.mkdtemp()
try:
    shot = os.path.join(tmp, 'shot.png')
    # A throwaway profile keeps this away from the user's Chrome; reduced motion skips the count-up animations.
    # Half scale keeps long pages under Chrome's 16,384px screenshot limit.
    subprocess.run([CHROME, '--headless=new', f'--user-data-dir={tmp}/profile', '--disable-gpu', '--hide-scrollbars',
                    '--force-device-scale-factor=0.5',
                    '--force-prefers-reduced-motion', f'--window-size={WIDTH},30000', '--virtual-time-budget=5000',
                    f'--screenshot={shot}', 'file://' + page],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    im = Image.open(shot).convert('RGB')
    px = im.load()
    bottom = im.height - 1
    while bottom > 0 and px[5, bottom] in (STAGE, (255, 255, 255)):
        bottom -= 1
    if bottom + 1 >= im.height:
        sys.exit(f'{v}: page is taller than the capture window; raise the window height')
    im = im.crop((0, 0, im.width, bottom + 1))
    im = im.resize((THUMB_W, round(im.height * THUMB_W / im.width)), Image.LANCZOS)
    out = os.path.join(here, 'thumbs', f'{v}.jpg')
    im.save(out, quality=74, optimize=True, progressive=True)
    print(f'Thumbnail {out} ({im.width}x{im.height})')
finally:
    shutil.rmtree(tmp, ignore_errors=True)
