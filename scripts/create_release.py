"""
Create a new release branch for the azure-cost-finops repository.

Automates the full release workflow:
  1. Validates the target repo git state (clean working tree, branch management)
  2. Creates a new branch named vbd-update-YYYY-MM-DD
  3. Copies the FinOps Module Repository Excel file into the authoring-guide source folder
  4. Runs export_scenario_modules.py to generate CSV and changelog outputs
  5. Copies outputs to the target repo
  6. Prompts for PPTX confirmation, then commits and pushes the new branch

Version: v1.2026-03-08.0 Dirk Brinkmann

Usage:
    python create_release.py
    python create_release.py --target-repo <path> --source-repo <path> --excel-file <path>
    python create_release.py --help
"""

__version__ = "v1.2026-03-08.0"

import argparse
import datetime
import os
import shutil
import subprocess
import sys

# ---------------------------------------------------------------------------
# Default paths
# ---------------------------------------------------------------------------
DEFAULT_TARGET_REPO = r"C:\Data\Github\azure-cost-finops"
DEFAULT_SOURCE_REPO = r"C:\Data\Github\finops-module-authoring-guide"
DEFAULT_EXCEL_FILE = (
    r"C:\Users\dirkbri\OneDrive - Microsoft\250-IP\FinOps\VBD\Modules\FinOpsCost-Module-Repository.xlsx"
)

TODAY = datetime.date.today().strftime("%Y-%m-%d")
BRANCH_NAME = f"vbd-update-{TODAY}"
COMMIT_MESSAGE = f"Update module repository {TODAY}"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def run_git(args, cwd, check=True):
    """Run a git command and return the completed process."""
    cmd = ["git", "--no-pager"] + args
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, check=check)


def prompt_yes_no(question):
    """Ask the user a yes/no question. Returns True for yes."""
    while True:
        answer = input(f"{question} [y/n]: ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please answer y or n.")


def abort(message):
    """Print an error message and exit."""
    print(f"\n❌ ABORTED: {message}", file=sys.stderr)
    sys.exit(1)


def info(message):
    """Print an informational message."""
    print(f"ℹ️  {message}")


def success(message):
    """Print a success message."""
    print(f"✅ {message}")


# ---------------------------------------------------------------------------
# Workflow steps
# ---------------------------------------------------------------------------

def validate_target_repo(target_repo):
    """
    Validate the git state of the target repository.

    If the repo is on a branch other than main:
      - Abort if there are uncommitted changes.
      - Prompt the user to delete the branch; abort if declined.
      - Switch to main, pull latest, delete the old local branch.
    If on main, just pull latest.
    """
    # Determine current branch
    result = run_git(["rev-parse", "--abbrev-ref", "HEAD"], cwd=target_repo)
    current_branch = result.stdout.strip()
    info(f"Target repo current branch: {current_branch}")

    if current_branch != "main":
        # Check for uncommitted changes
        status = run_git(["status", "--porcelain"], cwd=target_repo)
        if status.stdout.strip():
            abort(
                f"Branch '{current_branch}' has uncommitted changes. "
                "Please commit or stash them before running this script."
            )

        # Ask whether we can delete the branch
        if not prompt_yes_no(
            f"Branch '{current_branch}' exists. Delete it and start fresh from main?"
        ):
            abort("User declined branch deletion.")

        # Switch to main
        info("Switching to main...")
        run_git(["checkout", "main"], cwd=target_repo)

        # Pull latest
        info("Pulling latest from origin/main...")
        run_git(["pull", "origin", "main"], cwd=target_repo)

        # Delete old local branch
        info(f"Deleting local branch '{current_branch}'...")
        run_git(["branch", "-D", current_branch], cwd=target_repo)
        success(f"Deleted branch '{current_branch}'.")
    else:
        info("Already on main. Pulling latest...")
        run_git(["pull", "origin", "main"], cwd=target_repo)

    success("Target repo is up to date on main.")


def create_branch(target_repo):
    """Create and switch to the new release branch."""
    info(f"Creating branch '{BRANCH_NAME}'...")
    run_git(["checkout", "-b", BRANCH_NAME], cwd=target_repo)
    success(f"Created and switched to branch '{BRANCH_NAME}'.")


def copy_excel_file(excel_file, source_repo):
    """Copy the Excel file into the source folder of the authoring-guide repo."""
    source_dir = os.path.join(source_repo, "source")
    if not os.path.isdir(source_dir):
        os.makedirs(source_dir)

    dest = os.path.join(source_dir, os.path.basename(excel_file))
    info(f"Copying Excel file to {dest}...")
    shutil.copy2(excel_file, dest)
    success("Excel file copied.")
    return dest


def run_export_script(source_repo, excel_path):
    """
    Run export_scenario_modules.py with the given Excel file.

    Returns the paths to the generated CSV and changelog files.
    """
    script = os.path.join(source_repo, "scripts", "export_scenario_modules.py")
    if not os.path.isfile(script):
        abort(f"Export script not found: {script}")

    scripts_dir = os.path.join(source_repo, "scripts")
    info("Running export_scenario_modules.py...")
    result = subprocess.run(
        [sys.executable, script, "--input", excel_path, "--output", scripts_dir],
        capture_output=True, text=True
    )

    if result.returncode != 0:
        print(result.stderr, file=sys.stderr)
        abort("export_scenario_modules.py failed.")

    print(result.stdout)

    csv_path = os.path.join(scripts_dir, "scenario_modules.csv")
    changelog_path = os.path.join(scripts_dir, "module_changes.md")

    if not os.path.isfile(csv_path):
        abort(f"Expected CSV output not found: {csv_path}")
    if not os.path.isfile(changelog_path):
        abort(f"Expected changelog output not found: {changelog_path}")

    success("Export script completed.")
    return csv_path, changelog_path


def copy_outputs(csv_path, changelog_path, target_repo):
    """Copy the CSV and changelog to the appropriate locations in the target repo."""
    csv_dest = os.path.join(target_repo, "modulemapping", "scenario_modules.csv")
    changelog_dest = os.path.join(target_repo, "module_changes.md")

    info(f"Copying CSV to {csv_dest}...")
    shutil.copy2(csv_path, csv_dest)

    info(f"Copying changelog to {changelog_dest}...")
    shutil.copy2(changelog_path, changelog_dest)

    success("Output files copied to target repo.")


def confirm_pptx(target_repo):
    """Prompt the user to confirm that PPTX files are ready."""
    pptx_dir = os.path.join(target_repo, "modulerepository")
    info(f"PPTX files location: {pptx_dir}")

    if not prompt_yes_no(
        "Are all the latest PPTX files in the modulerepository folder?"
    ):
        abort("User indicated PPTX files are not ready.")

    success("PPTX files confirmed ready.")


def commit_and_push(target_repo):
    """Stage all changes, commit, and push the new branch."""
    info("Staging all changes...")
    run_git(["add", "-A"], cwd=target_repo)

    # Show what will be committed
    status = run_git(["status", "--short"], cwd=target_repo)
    print("\nFiles to be committed:")
    print(status.stdout)

    if not status.stdout.strip():
        abort("No changes to commit.")

    info(f"Committing with message: '{COMMIT_MESSAGE}'...")
    run_git(["commit", "-m", COMMIT_MESSAGE], cwd=target_repo)

    info(f"Pushing branch '{BRANCH_NAME}' to origin...")
    run_git(["push", "-u", "origin", BRANCH_NAME], cwd=target_repo)

    success(f"Branch '{BRANCH_NAME}' published to origin.")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    """Orchestrate the full release workflow."""
    parser = argparse.ArgumentParser(
        description="Create a new release branch for the azure-cost-finops repository."
    )
    parser.add_argument(
        "--target-repo",
        default=DEFAULT_TARGET_REPO,
        help=f"Path to the azure-cost-finops repo (default: {DEFAULT_TARGET_REPO})"
    )
    parser.add_argument(
        "--source-repo",
        default=DEFAULT_SOURCE_REPO,
        help=f"Path to the finops-module-authoring-guide repo (default: {DEFAULT_SOURCE_REPO})"
    )
    parser.add_argument(
        "--excel-file",
        default=DEFAULT_EXCEL_FILE,
        help=f"Path to the FinOpsCost-Module-Repository.xlsx file (default: {DEFAULT_EXCEL_FILE})"
    )
    parser.add_argument(
        "--version", "-V",
        action="version",
        version=f"%(prog)s {__version__}"
    )
    args = parser.parse_args()

    target_repo = os.path.abspath(args.target_repo)
    source_repo = os.path.abspath(args.source_repo)
    excel_file = os.path.abspath(args.excel_file)

    # Pre-flight checks
    if not os.path.isdir(target_repo):
        abort(f"Target repo not found: {target_repo}")
    if not os.path.isdir(source_repo):
        abort(f"Source repo not found: {source_repo}")
    if not os.path.isfile(excel_file):
        abort(f"Excel file not found: {excel_file}")

    print(f"\n{'='*60}")
    print(f"  FinOps Module Release Automation  {__version__}")
    print(f"{'='*60}")
    print(f"  Target repo  : {target_repo}")
    print(f"  Source repo   : {source_repo}")
    print(f"  Excel file    : {excel_file}")
    print(f"  Branch name   : {BRANCH_NAME}")
    print(f"  Commit message: {COMMIT_MESSAGE}")
    print(f"{'='*60}\n")

    # Step 1: Validate and prepare the target repo
    validate_target_repo(target_repo)

    # Step 2: Create the release branch
    create_branch(target_repo)

    # Step 3: Copy the Excel file to the authoring-guide source folder
    excel_dest = copy_excel_file(excel_file, source_repo)

    # Step 4: Run the export script
    csv_path, changelog_path = run_export_script(source_repo, excel_dest)

    # Step 5: Copy outputs to the target repo
    copy_outputs(csv_path, changelog_path, target_repo)

    # Step 6: Confirm PPTX files are ready
    confirm_pptx(target_repo)

    # Step 7: Commit and push
    commit_and_push(target_repo)

    print(f"\n{'='*60}")
    print(f"  🎉 Release branch '{BRANCH_NAME}' is published!")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
