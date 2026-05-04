# Zip backup of a git project (full tree)

**Filename:** **`<project>-yyyy-mm-dd.zip`** where **`<project>`** is the basename of **`git rev-parse --show-toplevel`**. ISO **date only** (no time-of-day). Repo-first groups backups per checkout; date stays sortable within a project.

**Include** **`.git`** by archiving from the **repository root** so history is preserved.

**Exclude nested zips:** **`-x "*.zip"`** when building the archive so existing backups in the tree are not packed again.

**Default output location:** parent of the repo root so the new file is not inside the tree being zipped.

## Example (run from parent of repo folder)

Replace **`myrepo`** with your checkout directory name:

```bash
cd /path/to/parent && zip -r "myrepo-$(date +%Y-%m-%d).zip" "myrepo" -x "*.zip"
```

Adjust paths for Windows or use your preferred archiver with the same rules.

## Alternative: contents-only archive (no `.git`)

Smaller shareable tree without history:

```bash
git -C myrepo archive --format=zip -o "myrepo-snapshot-$(date +%Y-%m-%d).zip" HEAD
```

Tradeoff: no **`.git`**; good for handoff or CI artifact, not for full backup.

## Related

- Optional wiki-style notes: [`../doc/wiki/profiles/knowledge/operations-local-preview-export.md`](../doc/wiki/profiles/knowledge/operations-local-preview-export.md).
