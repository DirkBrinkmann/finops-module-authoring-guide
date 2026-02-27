"""
Export Scenario-Module overview from the FinOps Module Repository Excel file.

Joins: VBD -> Map-VBD-Scenario -> VBD Scenarios -> Map-Scenario-Module -> VBD Module
Output columns: VBD Title, Scenario Title, Module Id, Module Title, Suggested Order, Module Type

Version: 1.1.0

Usage:
    python export_scenario_modules.py
    python export_scenario_modules.py --input <path_to_xlsx> --output <output_folder>
"""

__version__ = "1.1.0"

import argparse
import csv
import os
import sys
import openpyxl

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_EXCEL_FILE = os.path.join(SCRIPT_DIR, "FinOpsCost-Module-Repository.xlsx")
OUTPUT_FILENAME = "scenario_modules.csv"


def load_sheet_as_dict(wb, sheet_name, key_column):
    """Load a sheet into a dict keyed by the given column header."""
    ws = wb[sheet_name]
    headers = [cell.value for cell in ws[1]]
    key_idx = headers.index(key_column)
    result = {}
    for row in ws.iter_rows(min_row=2, max_row=ws.max_row, values_only=True):
        if row[key_idx] is not None:
            result[row[key_idx]] = dict(zip(headers, row))
    return result


def load_bridge_table(wb, sheet_name):
    """Load a bridge table as a list of dicts."""
    ws = wb[sheet_name]
    headers = [cell.value for cell in ws[1]]
    rows = []
    for row in ws.iter_rows(min_row=2, max_row=ws.max_row, values_only=True):
        if any(v is not None for v in row):
            rows.append(dict(zip(headers, row)))
    return rows


def main():
    parser = argparse.ArgumentParser(
        description="Export Scenario-Module overview from the FinOps Module Repository Excel file."
    )
    parser.add_argument(
        "--input", "-i",
        help="Path to the FinOpsCost-Module-Repository.xlsx file. "
             "If omitted, you will be prompted to enter it."
    )
    parser.add_argument(
        "--output", "-o",
        help="Output folder for the generated scenario_modules.csv. "
             "If omitted, you will be prompted to enter it."
    )
    args = parser.parse_args()

    # Resolve input file
    excel_file = args.input
    if not excel_file:
        default_display = DEFAULT_EXCEL_FILE
        excel_file = input(f"Path to Excel file [{default_display}]: ").strip()
        if not excel_file:
            excel_file = DEFAULT_EXCEL_FILE

    if not os.path.isfile(excel_file):
        print(f"Error: File not found: {excel_file}", file=sys.stderr)
        sys.exit(1)

    # Resolve output folder
    output_dir = args.output
    if not output_dir:
        default_output = SCRIPT_DIR
        output_dir = input(f"Output folder [{default_output}]: ").strip()
        if not output_dir:
            output_dir = default_output

    if not os.path.isdir(output_dir):
        print(f"Error: Output folder not found: {output_dir}", file=sys.stderr)
        sys.exit(1)

    output_csv = os.path.join(output_dir, OUTPUT_FILENAME)

    wb = openpyxl.load_workbook(excel_file, data_only=True)

    # Entity lookups
    vbds = load_sheet_as_dict(wb, "VBD", "VBD Id")
    modules = load_sheet_as_dict(wb, "VBD Module", "Module Id")

    # Bridge tables
    map_vbd_scenario = load_bridge_table(wb, "Map-VBD-Scenario")
    map_scenario_module = load_bridge_table(wb, "Map-Scenario-Module")

    # Build join: VBD -> Scenario -> Module
    output_rows = []
    for vs in map_vbd_scenario:
        vbd_id = vs["VBD Id"]
        scenario_id = vs["Scenario Id"]
        vbd_title = vbds[vbd_id]["VBD Title"] if vbd_id in vbds else vs.get("VBD", "")

        for sm in map_scenario_module:
            if sm["Scenario Id"] != scenario_id:
                continue
            module_id = sm["Module Id"]
            module_title = modules[module_id]["Module Title"] if module_id in modules else sm.get("Module", "")
            scenario_title = sm.get("Scenario", vs.get("Scenario", ""))

            output_rows.append({
                "VBD Title": vbd_title,
                "Scenario Title": scenario_title,
                "Module Id": module_id,
                "Module Title": module_title,
                "Suggested Order": sm.get("Suggested Order", ""),
                "Module Type": sm.get("Module Type", ""),
            })

    # Sort by VBD Title, Scenario Title, Suggested Order
    output_rows.sort(key=lambda r: (
        r["VBD Title"],
        r["Scenario Title"],
        int(r["Suggested Order"]) if str(r["Suggested Order"]).isdigit() else 9999,
    ))

    # Write CSV
    fieldnames = ["VBD Title", "Scenario Title", "Module Id", "Module Title", "Suggested Order", "Module Type"]
    with open(output_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(output_rows)

    print(f"Exported {len(output_rows)} rows to {output_csv}")


if __name__ == "__main__":
    main()
