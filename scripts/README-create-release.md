v1.2026-03-08.0 Dirk Brinkmann

# Create Release Automation

Automates the creation of a new release branch for the
[azure-cost-finops](https://github.com/asd-management/azure-cost-finops) repository.

## Prerequisites

- **Python 3.8+** with `openpyxl` installed (`pip install openpyxl`)
- Git configured with push access to the `azure-cost-finops` remote
- The FinOps Module Repository Excel file available at the default (or custom) path

## What it does

The script performs these steps in order:

1. **Validates the target repo** — checks the current branch of `azure-cost-finops`.
   If on a feature branch, it verifies no uncommitted changes exist, asks to delete the
   branch, then switches to `main` and pulls the latest.
2. **Creates a new branch** — `vbd-update-YYYY-MM-DD` (using today's date).
3. **Copies the Excel file** — from the OneDrive source into `finops-module-authoring-guide/source/`.
4. **Runs the export script** — `export_scenario_modules.py` generates `scenario_modules.csv`
   and `module_changes.md`.
5. **Copies outputs** — CSV goes to `azure-cost-finops/modulemapping/`, changelog to the repo root.
6. **Confirms PPTX files** — prompts you to verify that all latest PowerPoint modules are in
   `azure-cost-finops/modulerepository/`.
7. **Commits and pushes** — stages all changes, commits with message
   `"Update module repository YYYY-MM-DD"`, and pushes the branch to origin.

## Usage

### Default paths (recommended)

```bash
python scripts/create_release.py
```

### Custom paths

```bash
python scripts/create_release.py \
  --target-repo "C:\Data\Github\azure-cost-finops" \
  --source-repo "C:\Data\Github\finops-module-authoring-guide" \
  --excel-file "C:\path\to\FinOpsCost-Module-Repository.xlsx"
```

### CLI arguments

| Argument | Default | Description |
|---|---|---|
| `--target-repo` | `C:\Data\Github\azure-cost-finops` | Path to the azure-cost-finops repository |
| `--source-repo` | `C:\Data\Github\finops-module-authoring-guide` | Path to the authoring-guide repository |
| `--excel-file` | `C:\Users\dirkbri\OneDrive - Microsoft\...\FinOpsCost-Module-Repository.xlsx` | Path to the Excel source file |
| `--version`, `-V` | — | Show script version and exit |

## Abort conditions

The script will stop and print an error if:

- The target repo has uncommitted changes on a non-main branch
- You decline to delete the existing branch
- You indicate PPTX files are not ready
- The export script fails
- There are no changes to commit
