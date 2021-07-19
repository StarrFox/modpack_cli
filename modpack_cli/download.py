from modpack_downloader.manifest import ModPackManifest
import requests
from loguru import logger

from .constants import MOD_FILE, USERAGENT


def download_modpack_file(project_id: int, file_id: int):
    target = MOD_FILE.format(mod_id=project_id, file_id=file_id)

    logger.info(f"Getting {target}")

    headers = {
        "User-Agent": USERAGENT
    }

    with requests.get(target, headers=headers) as res:
        logger.info(f"Response: {res.status_code=} {res.reason=}")
        file_data = res.json()

    download_url = file_data["downloadUrl"].replace("edge.", "media.")
    logger.info(f"Would download {file_data['fileName']=} {download_url=}")


def download_from_manifest(manifest: "ModPackManifest"):
    for file in manifest.files:
        download_modpack_file(file.project_id, file.file_id)
