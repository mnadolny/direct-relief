# Why Direct Relief prototypes

Hi-fi prototypes for client review, served with GitHub Pages.

- v4: https://mnadolny.github.io/direct-relief/v4/
- v5: https://mnadolny.github.io/direct-relief/v5/

To add or refresh a version from `../hifi/why-direct-relief-hifi-<v>.html`:

```bash
./publish.sh v4
git add -A && git commit -m "Publish v4" && git push
```

Re-run `./publish.sh v5` after publishing a new version so its "Compare" link un-hides.
Update `index.html` if the root should point at a different version.
