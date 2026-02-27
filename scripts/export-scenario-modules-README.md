# Module Mapping File Creation Guidance

> **Script:** `export_scenario_modules.py` · **Version:** 1.1.0
> **Purpose:** Generates `scenario_modules.csv` from the Module Repository Excel workbook.

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

Download the latest version of `FinOpsCost-Module-Repository.xlsx` from the [Module Repository Database](https://microsofteur-my.sharepoint.com/personal/dirkbri_microsoft_com/Documents/250-IP/FinOps/VBD/Modules/FinOpsCost-Module-Repository.xlsx?web=1).

---

## Usage

The script accepts the Excel input file and CSV output folder either as command-line arguments or via interactive prompts.

### Interactive Mode (default)

Run the script without arguments — it will prompt for the input file and output folder, offering sensible defaults:

```
python scripts/export_scenario_modules.py
```

```
Path to Excel file [<scripts_dir>/FinOpsCost-Module-Repository.xlsx]: <Enter to accept>
Output folder [<scripts_dir>]: C:\Data\Output
Exported 108 rows to C:\Data\Output\scenario_modules.csv
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
| `--output` | `-o` | Folder where `scenario_modules.csv` will be written |

Both arguments are optional — if omitted, the script prompts interactively.

---

## What the Script Does

The script joins data across four sheets in the Excel workbook:

```
VBD → Map-VBD-Scenario → VBD Scenarios → Map-Scenario-Module → VBD Module
```

It produces a flat CSV file (`scenario_modules.csv`) with one row per scenario–module combination, sorted by VBD title, scenario title, and suggested delivery order.

### Output Columns

| Column | Description |
|--------|-------------|
| `VBD Title` | Name of the workshop (e.g., Knowledge Transfer) |
| `Scenario Title` | Name of the scenario within the workshop |
| `Module Id` | Module identifier (e.g., `M-001`) |
| `Module Title` | Full title of the module |
| `Suggested Order` | Delivery sequence number within the scenario (lower = earlier) |
| `Module Type` | Inclusion type: `mandatory`, `recommended`, or `optional` |

---

## Output File

The generated CSV is written to:

```
scripts/scenario_modules.csv
```

This file is committed to the [VBD Delivery Repo](https://github.com/asd-management/azure-cost-finops) as part of the publishing process (see [VBD Development Guide §7](../VBD-DEVELOPMENT-GUIDE.md#7-publishing-to-production)).
