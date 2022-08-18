import click
import os
import subprocess
from send2trash import send2trash


def get_files(directory: str, recursive=False) -> list[str]:
    files = []
    if recursive:
        for dirpath, dirnames, filenames in os.walk(directory):
            for filename in filenames:
                files.append(os.path.join(dirpath, filename))
    else:
        for filename in os.listdir(directory):
            files.append(os.path.join(directory, filename))
    return files


@click.command()
@click.argument("directory")
@click.option("--recursive", is_flag=True)
def main(directory: str, recursive: bool):
    for filepath in get_files(directory, recursive):
        root, ext = os.path.splitext(filepath)
        if ext.lower() in [".heic", ".heif"]:
            print(f"Converting '{filepath}'...")
            subprocess.run(
                ["magick", filepath, "-quality", "90", f"{root}.jpg"], check=True
            )
            send2trash(filepath)


if __name__ == "__main__":
    main()
