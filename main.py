from loguru import logger
from pprint import pprint

from modpack_cli import load_manifest, download_from_manifest


logger.enable("modpack_downloader")

# https://addons-ecs.forgesvc.net/api/v2/addon/225643/file/3386883

def main():
    manifest = load_manifest("manifest.json")
    pprint(manifest)
    download_from_manifest(manifest)


if __name__ == "__main__":
    main()

