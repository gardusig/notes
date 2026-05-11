# Local preview, export, backup

## Full git tree zip (including `.git`)

When you need a **portable copy of the entire repository** (history included), archive from the **repository root** and write the file **outside** the tree so the archive is not nested inside itself.

### Filename convention

Use **calendar date in ISO form** plus the **project directory name** (basename of the git root), or the pattern in **[`../../../../git/zip-git-project-backup.md`](../../../../git/zip-git-project-backup.md)**.

### Exclude nested zips (optional)

Pass **`-x "*.zip"`** (or equivalent) so backups already in the repo are not packed again.

### Commands

See **[`../../../../git/zip-git-project-backup.md`](../../../../git/zip-git-project-backup.md)** for **`zip`** and **`git archive`** examples.

## Markdown preview / static export

<How to preview markdown or export a static site if applicable. Omit sections that do not apply.>
