"""
Script to create SDK mod zip files from source directories.

This script packages Python files, TOML configuration, and markdown documentation
into a zip archive with the .sdkmod extension for use with the Willow 2 SDK.
"""

import zipfile
from pathlib import Path


def zip_dir(dir_name: str) -> None:
    """
    Create a .sdkmod zip archive from a directory containing SDK mod files.

    This function packages Python files (.py), configuration files (.toml),
    and documentation files (.md) from the specified directory into a zip archive.
    The resulting archive is renamed to have a .sdkmod extension.

    Args:
        dir_name: Path to directory containing mod files

    Raises:
        FileNotFoundError: If specified directory doesn't exist
    """
    # Create Path objects
    dir_path = Path(dir_name)
    zip_file_path = dir_path / f"{dir_name}.zip"
    sdkmod_file_path = dir_path / f"{dir_name}.sdkmod"

    # Create zip file using context manager
    with zipfile.ZipFile(zip_file_path, mode="w") as zip_file:
        # Find and add relevant files to the zip
        for item_path in dir_path.iterdir():
            if item_path.suffix in (".py", ".toml", ".md"):
                print(item_path.name)
                zip_file.write(item_path)

    # Replace existing .sdkmod file if it exists
    if sdkmod_file_path.exists():
        sdkmod_file_path.unlink()

    # Rename zip file to .sdkmod
    zip_file_path.rename(sdkmod_file_path)


if __name__ == "__main__":
    zip_dir("save_file_organizer")
    # zip_dir("speedrun_practice")
