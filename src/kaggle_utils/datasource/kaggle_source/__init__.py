from enum import Enum
from kaggle_utils.datasource.local_datasource import LocalDataSource
from pathlib import Path
import shutil
import kaggle
import zipfile

class KaggleAPIType(str, Enum):
    COMPETITION = "competition"
    DATASET = "dataset"



class KaggleSource(LocalDataSource):

    def __init__(self, data_dir: Path, name: str, api: KaggleAPIType):
        super().__init__(data_dir / name.split("/").pop())
        self.api = api
        self.name = name
    
    def download(self):
        if self.api == KaggleAPIType.COMPETITION:
            kaggle.api.competition_download_cli(self.name, path=self.data_dir)
        elif self.api == KaggleAPIType.DATASET:
            kaggle.api.dataset_download_cli(self.name, path=self.data_dir)
        else:
            raise TypeError(f"expected either KaggleAPIType.COMPETITION or KaggleAPIType.DATASET but got {type(self.api)} instead")

        if not self.data_dir.exists():
            with zipfile.ZipFile(self.data_zip, "r") as z:
                z.extractall(self.data_dir)

    def remove(self):
        '''
        remove all files from the paths self.data_dir and self.data_zip
        '''
        self.data_zip.unlink()
        shutil.rmtree(self.data_dir)

    def check_if_exists(self):
        '''
        check existence for data zip file and the data directory file lazily
        '''
        return self.data_zip.exists() and self.data_dir.exists()