from torch.utils.data import Dataset
from typing import List
from kaggle_utils.datasource.type import DataSourceType

class Task(Dataset):
    def __init__(self, types: List[DataSourceType]):
        self.types = types