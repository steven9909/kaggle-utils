from typing import List

from kaggle_utils.datasource.type import DataSourceType
from torch.utils.data import Dataset


class Task(Dataset):
    def __init__(self, datasource_types: List[DataSourceType]):

        self.datasource_types = datasource_types
