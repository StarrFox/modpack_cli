"""
{
  "minecraft": {
    "version": "1.16.5",
    "modLoaders": [
      {
        "id": "forge-36.1.32",
        "primary": true
      }
    ]
  },
  "manifestType": "minecraftModpack",
  "manifestVersion": 1,
  "name": "1.16.5 mod testing",
  "version": "1.16.5",
  "author": "AstralIneundo",
  "files": [
    {
      "projectID": 238222,
      "fileID": 3345971,
      "required": true
    },
  ],
  "overrides": "overrides"
}
"""

import json
from pathlib import Path
from dataclasses import dataclass


@dataclass
class MinecraftManifest:
    version: str
    modloader: str


@dataclass
class ModPackFile:
    project_id: int
    file_id: int
    required: bool


@dataclass
class ModPackManifest:
    minecraft_manifest: MinecraftManifest
    pack_type: str
    name: str
    version: str
    author: str
    files: list[ModPackFile]


def load_manifest(file_path: str | Path) -> ModPackManifest:
    if isinstance(file_path, str):
        file_path = Path(file_path)

    manifest_data = json.load(file_path.open())

    minecraft = manifest_data["minecraft"]
    minecraft_version = minecraft["version"]
    minecraft_modloader = minecraft["modLoaders"][0]["id"]

    minecraft_manifest = MinecraftManifest(minecraft_version, minecraft_modloader)

    pack_type = manifest_data["manifestType"]
    name = manifest_data["name"]
    version = manifest_data["version"]
    author = manifest_data["author"]

    files = []

    for file in manifest_data["files"]:
        project_id = file["projectID"]
        file_id = file["fileID"]
        required = file["required"]

        files.append(ModPackFile(project_id, file_id, required))


    return ModPackManifest(minecraft_manifest, pack_type, name, version, author, files)
