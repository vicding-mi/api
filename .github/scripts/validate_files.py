import os
import sys
import json
import httpx


# External service URL
VALIDATION_URL = "http://localhost:4010/"
CHANGED_FILES = os.getenv("CHANGED_FILES", "")
changed_files = []
if CHANGED_FILES and CHANGED_FILES != "":
    changed_files: list = CHANGED_FILES.split()

print(f"CHANGED_FILES: {CHANGED_FILES}")

def get_pushed_files():
    return [file for file in changed_files if file.endswith(".json")]


def validate_file(file_path):
    """Validate a single file against the external service."""
    print(f"Validating {file_path}...")
    filename = os.path.basename(file_path)
    url_part = file_path.split("/")[-2]  # Get the folder name, which is the url part
    # TODO: update the URL and path, this should take the jsons from parent directory
    url = VALIDATION_URL + "products/" + filename
    url = VALIDATION_URL + f"{url_part}/" + filename
    print(f"Validation URL: {url}")
    response = httpx.get(url)
    print(f"Response: {response.status_code} {response.text}")
    if 200 <= response.status_code < 303:
        print(f"✅ {file_path} is valid.")
        return True
    else:
        print(f"❌ {file_path} is invalid.")
        return False


def main():
    """Main function to validate pushed files."""
    print(f"CHANGED_FILES: {CHANGED_FILES}")
    # pushed_files = get_pushed_files()
    # TODO: the pushed_files in the next line is for debugging only, it should be replaced with the line above
    pushed_files = ["../../openapi/ver/current/sample_data/products/test.json",
                   "../../openapi/ver/current/sample_data/products/test1.json"]
    print(f"Pushed files: {pushed_files}")
    if not pushed_files:
        print("No JSON files to validate.")
        return

    all_valid = True
    for file_path in pushed_files:
        if os.path.exists(file_path):
            if not validate_file(file_path):
                all_valid = False
        else:
            print(f"⚠️ File {file_path} does not exist locally.")
            all_valid = False

    if not all_valid:
        exit(1)


if __name__ == "__main__":
    main()
