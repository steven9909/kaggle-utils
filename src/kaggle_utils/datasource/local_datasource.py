from datasource import DataSource
from abc import abstractmethod
from pathlib import Path

class LocalDataSource(DataSource):

    def __init__(self, data_dir: Path):
        self.data_dir = data_dir
        self.data_zip = self.data_dir.with_suffix(".zip")

    @abstractmethod
    def download(self):
        pass

    @abstractmethod
    def remove(self):
        pass