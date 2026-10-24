# Why Direct Relief prototypes

Hi-fi prototypes for client review, served with GitHub Pages.

- Index of all versions: https://mnadolny.github.io/direct-relief/
- v4: https://mnadolny.github.io/direct-relief/v4/
- v5: https://mnadolny.github.io/direct-relief/v5/
- v6: https://mnadolny.github.io/direct-relief/v6/

To add or refresh a version from `../hifi/why-direct-relief-hifi-<v>.html`:

```bash
./publish.sh v4
git add -A && git commit -m "Publish v4" && git push
```

`publish.sh` also strips the design notes and saves a full-page thumbnail to `thumbs/` (needs Google Chrome and Python's Pillow).
Re-run the previous version's publish after a new one so its "Compare" link un-hides.
Add a card for each new version to `index.html`, the versions index.
