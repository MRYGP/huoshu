import hashlib
import os
from collections import defaultdict


BASE_DIR = r"E:\活书"


def file_hash(path: str) -> str:
    """Return SHA256 hash of a file in chunks to handle large files."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def find_duplicates():
    groups = defaultdict(list)
    for root, _, files in os.walk(BASE_DIR):
        for name in files:
            path = os.path.join(root, name)
            try:
                hash_value = file_hash(path)
                groups[hash_value].append(path)
            except OSError:
                # Skip unreadable files
                continue
    dups = {h: paths for h, paths in groups.items() if len(paths) > 1}
    return dups


def main():
    duplicates = find_duplicates()
    if not duplicates:
        print("No duplicate files by content were found.")
        return
    print("Duplicate groups (same content):")
    for idx, (hash_value, paths) in enumerate(duplicates.items(), 1):
        print(f"\nGroup {idx} (hash={hash_value}):")
        for p in paths:
            print(f"  {p}")


if __name__ == "__main__":
    main()

