from pathlib import Path
from urllib.parse import urlparse

import requests
from kaggle_utils.datasource.kaggle import KaggleAPIType, KaggleDataSource
from kaggle_utils.datasource.type.image.classification import IImageClassification


def download_file(url: str, dir: Path):

    if not dir.exists():
        dir.mkdir(parents=True)

    with open(dir / Path(urlparse(url).path).name, "wb") as f:
        f.write(requests.get(url, headers={"User-Agent": "Mozilla/5.0"}).content)


class IMaterialistFashion2021FGVC8(KaggleDataSource, IImageClassification):
    def __init__(self, data_dir: Path):

        super().__init__(
            data_dir, "imaterialist-fashion-2021-fgvc8", KaggleAPIType.COMPETITION
        )

    def download(self):

        super().download()
        download_file(
            "https://s3.amazonaws.com/ifashionist-dataset/images/train2020.zip",
            self.dir,
        )
        download_file(
            "https://s3.amazonaws.com/ifashionist-dataset/images/val_test2020.zip",
            self.dir,
        )
