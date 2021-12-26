import json
import os

import requests

URL_PREFIX = "https://raw.githubusercontent.com/off-by-0point5/fabric-modlists/master/"
VERSIONS_FILE = URL_PREFIX+"version.json"

print("=== Mc mods installation ===")

available_versions = requests.get(VERSIONS_FILE).json()
for version_key in available_versions.keys():
    print(version_key)
version_key = input("> ")

mod_lists = available_versions[version_key]
for mod_list in mod_lists:
    print(mod_list)
mod_list = input("> ")

mods = requests.get(URL_PREFIX+mod_list).json()

downloads = []
for mod_key in mods.keys():
    install = input("Install {}? (y/n) ".format(mod_key))
    if install.lower() in ["y", "yes"]:
        downloads.append((mod_key, mods[mod_key]))

print("============================\n")
print("Download directory is ./mods/\n")

for dl in downloads:
    print("Download {}".format(dl[0]))
    exit_code = os.system("wget -P ./mods/ {}".format(dl[1]))
    if exit_code != 0:
        print("Error downloading the file")
