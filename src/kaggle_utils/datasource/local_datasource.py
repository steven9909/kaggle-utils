from abc import abstractmethod
from pathlib import Path

from kaggle_utils.datasource import DataSource


class LocalDataSource(DataSource):
    def __init__(self, dir: Path):

        self.dir = dir

    @abstractmethod
    def download(self):
        raise NotImplementedError()

    @abstractmethod
    def remove(self):
        raise NotImplementedError()
