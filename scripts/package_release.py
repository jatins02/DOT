import os
import sys
import zipfile


def main():
    archive_name = sys.argv[1]
    project_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    package_directory = os.path.join(project_directory, "package")
    archive_path = os.path.join(project_directory, archive_name)

    with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for root, _, files in os.walk(package_directory):
            for filename in files:
                path = os.path.join(root, filename)
                archive.write(path, os.path.relpath(path, package_directory))

    print(f"Created release archive at {archive_path}")


if __name__ == "__main__":
    main()