#!/usr/bin/env bash
# Copy a hifi version into its own folder for GitHub Pages: ./publish.sh v5
set -euo pipefail
v="${1:?usage: ./publish.sh v5}"
here="$(cd "$(dirname "$0")" && pwd)"
src="$here/../hifi"
rm -rf "$here/$v" && mkdir -p "$here/$v/img"
# Only the images this page uses.
for img in $(grep -oE 'src="img/[^"]+"' "$src/why-direct-relief-hifi-$v.html" | sed -E 's/src="img\/(.*)"/\1/' | sort -u); do
  cp "$src/img/$img" "$here/$v/img/"
done
# Keep it out of search results and point version links at the published folders.
{
  # The hifi pages are fragments (no doctype), so give them one to avoid quirks mode.
  grep -qi '<!doctype' "$src/why-direct-relief-hifi-$v.html" || printf '<!doctype html>\n<html lang="en">\n'
  echo '<meta name="robots" content="noindex, nofollow">'
  sed -E -e 's#href="why-direct-relief-hifi-(v[0-9]+)\.html"#href="../\1/"#g' \
  "$src/why-direct-relief-hifi-$v.html"
} > "$here/$v/index.html"
# Hide links to versions that aren't published yet.
for link in $(grep -oE 'href="\.\./v[0-9]+/"' "$here/$v/index.html" | sed -E 's/.*\.\.\/(v[0-9]+)\/.*/\1/' | sort -u); do
  [ -d "$here/$link" ] || sed -i '' -E "s#<a class=\"vlink\" href=\"\.\./$link/\">[^<]*</a>#<!-- & -->#" "$here/$v/index.html"
done
# claude.ai artifacts are private to us, so the client can't open them.
sed -i '' -E 's#<a class="vlink" href="https://claude\.ai/[^"]*">[^<]*</a>#<!-- & -->#' "$here/$v/index.html"
# Design notes are for us, not the client.
python3 "$here/strip-notes.py" "$here/$v/index.html"
echo "Published $v -> $here/$v"
