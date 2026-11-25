# Why Direct Relief prototypes

Hi-fi prototypes for client review, served with GitHub Pages.

- Index of all versions: https://mnadolny.github.io/direct-relief/
- **v8 (current):** https://mnadolny.github.io/direct-relief/v8/
- v7: https://mnadolny.github.io/direct-relief/v7/
- v6: https://mnadolny.github.io/direct-relief/v6/
- v5: https://mnadolny.github.io/direct-relief/v5/
- v4: https://mnadolny.github.io/direct-relief/v4/

## Versions

- **v8** is the live directrelief.org charity-rating page's full content, set in the v7 design. To the client it's the new direction after v6, because they never saw v7.
  - Type: Roboto only, no all caps. The lightest weight is 400, because 300 breaks down on non-Apple machines.
  - Colour: one orange, `#DA3D01`, for text, buttons, rules and accents. It has about 4.5:1 contrast against white. The other colours are light blues.
  - Links: arrow links (orange ring and arrow) are for calls to action; the orange underline is only for "Source:" citations and archive lists.
  - Motion: the map's moving packets and the dot that travels along the Prepare → Respond → Recover line. Everything else is static.
- **v7**: internal design pass on v6 (Roboto, light blues, no photo tiles). The client never saw it.
- **v6**: the client's regrouping of v5.
- **v5**: client prototype content in the v4 styling.
- **v4**: structured rebuild.

## Publishing

To add or refresh a version from `../hifi/why-direct-relief-hifi-<v>.html`:

```bash
./publish.sh v8
git add v8 thumbs/v8.jpg && git commit -m "Publish v8" && git push
```

Stage the version's folder and thumbnail by name, not with `git add -A`, so unrelated local edits stay out of the commit.

`publish.sh` also strips the design notes and saves a full-page thumbnail to `thumbs/` (needs Google Chrome and Python's Pillow).
Re-run the previous version's publish after a new one so its "Compare" link un-hides.
Add a card for each new version to `index.html`, the versions index.

## Hosting

GitHub Pages deploys on every push to `main` and is the link to share.
The Netlify mirror (dr-alley.netlify.app) has run out of credits and has paused production deploys, so it still shows v4–v7.
When it's back, bump the target in `_redirects` (Netlify only) to the current version.
