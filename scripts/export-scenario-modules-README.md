# Module Mapping File Creation Guidance

> **Script:** `export_scenario_modules.py` · **Version:** 1.4.0 (2026-03-01 13:54)
> **Purpose:** Generates `scenario_modules.csv` and optionally `module_changes.md` from the Module Repository Excel workbook.

---

## Prerequisites

### 1. Python

Python 3.8 or later must be installed. Verify with:

```
python --version
```

### 2. openpyxl

The script requires the `openpyxl` package to read Excel files. Install it with:

```
pip install openpyxl
```

### 3. Module Repository Excel File

Download the latest version of `FinOpsCost-Module-Repository.xlsx` from the [Module Repository Database](https://microsofteur-my.sharepoint.com/personal/dirkbri_microsoft_com/Documents/250-IP/FinOps/VBD/Modules/FinOpsCost-Module-Repository.xlsx?web=1) and place it in the `source/` folder at the repository root. The script looks for it there by default.

---

## Usage

The script accepts the Excel input file and CSV output folder either as command-line arguments or via interactive prompts. By default it also generates a Markdown changelog of recently changed modules.

### Interactive Mode (default)

Run the script without arguments — it will prompt for the input file and output folder, offering sensible defaults:

```
python scripts/export_scenario_modules.py
```

```
Path to Excel file [<repo_root>/source/FinOpsCost-Module-Repository.xlsx]: <Enter to accept>
Output folder [<scripts_dir>]: C:\Data\Output
Exported 108 rows to C:\Data\Output\scenario_modules.csv
Exported 5 module changes to C:\Data\Output\module_changes.md
```

Press **Enter** at each prompt to accept the default value shown in brackets.

### Command-Line Mode

Provide `--input` and `--output` to skip the prompts:

```
python scripts/export_scenario_modules.py --input "C:\Data\FinOpsCost-Module-Repository.xlsx" --output "C:\Data\Output"
```

| Argument | Short | Description |
|----------|-------|-------------|
| `--input` | `-i` | Path to the `FinOpsCost-Module-Repository.xlsx` file |
| `--output` | `-o` | Folder where output files will be written |
| `--no-changelog` | | Disable generation of `module_changes.md` (enabled by default) |
| `--days` | | Number of days to look back for module changes (default: 30) |

Both arguments are optional — if omitted, the script prompts interactively.

---

## What the Script Does

The script joins data across four sheets in the Excel workbook:

```
VBD → Map-VBD-Scenario → VBD Scenarios → Map-Scenario-Module → VBD Module
```

It produces a flat CSV file (`scenario_modules.csv`) with one row per scenario–module combination, sorted by VBD title, scenario title, and suggested delivery order.

### Output Columns (scenario_modules.csv)

| Column | Description |
|--------|-------------|
| `VBD Title` | Name of the workshop (e.g., Knowledge Transfer) |
| `Scenario Title` | Name of the scenario within the workshop |
| `Module Id` | Module identifier (e.g., `M-001` for content modules, `A-001` for artefacts) |
| `Module Title` | Full title of the module |
| `Suggested Order` | Delivery sequence number within the scenario (lower = earlier) |
| `Module Type` | Inclusion type: `mandatory`, `recommended`, or `optional` |
| `Module first release date` | Date when the module was first released |
| `Module last modified` | Date when the module content was last modified |

---

## Module Changes Changelog

Unless `--no-changelog` is passed, the script generates a Markdown file (`module_changes.md`) listing all modules that were newly released or modified within the lookback window (default: 30 days, configurable via `--days`).

### Changelog Columns

| Column | Description |
|--------|-------------|
| `Status` | `New` if the module was first released within the period; `Modified` otherwise |
| `Module Id` | Module identifier (e.g., `M-001` for content modules, `A-001` for artefacts) |
| `Module Name` | Full title of the module |
| `Module first release date` | Date when the module was first released |
| `Module last modified` | Date when the module content was last modified |

The table is sorted with **New** modules first, then by **Module Id**.

---

## Output Files

The generated files are written to the output folder (defaults to `scripts/`):

- **`scenario_modules.csv`** — flat CSV with one row per scenario–module combination
- **`module_changes.md`** — Markdown changelog of recently changed modules (unless disabled)

This file is committed to the [VBD Delivery Repo](https://github.com/asd-management/azure-cost-finops) as part of the publishing process (see [VBD Development Guide §7](../VBD-DEVELOPMENT-GUIDE.md#7-publishing-to-production)).
