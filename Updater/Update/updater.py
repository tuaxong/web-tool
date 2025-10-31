import requests
import os
import zipfile
from io import BytesIO

# --- CONFIG ---
UPDATE_JSON = "http://127.0.0.1/update-server/version.json"
CURRENT_VERSION = "1.0"  # your app's current version
DOWNLOAD_FOLDER = os.getcwd()  # where to extract updates

# --- CHECK FOR UPDATE ---
try:
    response = requests.get(UPDATE_JSON)
    response.raise_for_status()
    data = response.json()
    latest_version = data["latest"]
    zip_url = data["url"]
    changelog = data.get("changelog", "")

    print(f"Current version: {CURRENT_VERSION}")
    print(f"Latest version: {latest_version}")
    print(f"Changelog: {changelog}\n")

    if latest_version > CURRENT_VERSION:
        print("New version available! Downloading update...")

        # download ZIP in memory
        r = requests.get(zip_url)
        r.raise_for_status()
        zip_data = BytesIO(r.content)

        # extract ZIP to folder
        with zipfile.ZipFile(zip_data) as z:
            z.extractall(DOWNLOAD_FOLDER)
        print(f"Update downloaded and extracted to: {DOWNLOAD_FOLDER}")

        # optionally, update your CURRENT_VERSION variable
        CURRENT_VERSION = latest_version
        print(f"Update complete! Now running version {CURRENT_VERSION}")
    else:
        print("Your app is already up to date.")

except requests.exceptions.RequestException as e:
    print("Error connecting to update server:", e)
except zipfile.BadZipFile:
    print("Downloaded file is not a valid ZIP.")
except Exception as e:
    print("Unexpected error:", e)
