import shutil
import zipfile
from enum import Enum
from pathlib import Path

from kaggle_utils.datasource.local_datasource import LocalDataSource

import kaggle


class KaggleAPIType(str, Enum):
    COMPETITION = "competition"
    DATASET = "dataset"


class KaggleDataSource(LocalDataSource):
    """
    Kaggle Data Source

    Args:
        data_dir (Path): data directory

    Attribute:
        dir (Path): data directory
        zip (Path): data zip file
    """

    def __init__(self, data_dir: Path, name: str, api: KaggleAPIType):

        super().__init__(data_dir / name.split("/").pop())
        self.zip = self.dir.with_suffix(".zip")
        self.name = name
        self.api = api

    def download(self):
        """
        Downloads data using Kaggle API
        """

        if self.api == KaggleAPIType.COMPETITION:
            kaggle.api.competition_download_cli(self.name, path=self.dir)

        elif self.api == KaggleAPIType.DATASET:
            kaggle.api.dataset_download_cli(self.name, path=self.dir)

        else:
            raise TypeError(
                "expected either KaggleAPIType.COMPETITION or KaggleAPIType.DATASET but"
                f"got {type(self.api)} instead"
            )

        if not self.dir.exists():
            with zipfile.ZipFile(self.zip, "r") as z:
                z.extractall(self.dir)

    def remove(self):
        """
        Removes data directory and data zip file
        """

        if self.dir.exists():
            shutil.rmtree(self.dir)

        if self.zip.exists():
            self.zip.unlink()

    def check_exists(self):
        return self.zip.exists() and self.dir.exists()
