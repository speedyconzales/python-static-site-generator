from typing import List
from pathlib import Path
import shutil

class Parser():

    def __init__(self):
        self.extensions: List[str] = []

    def valid_extension(self,extension):
        if extension in self.extensions:
            return True
        else:
            return False

    def parse(self,path,source,dest):
        self.path = Path(path)
        self.source = Path(source)
        self.dest = Path(dest)
        raise NotImplementedError

    def read(self,path):
        with open(path) as file:
            return file.read()

    def write(self,path,dest,content,ext=".html"):
        self.full_path = self.dest / path.with_suffix(ext).name

    def copy(self,path,source,dest):
        shutil.copy2(path,dest / path.relative_to(source))

class ResourceParser(Parser):
    self.extensions = [".jpg",".png",".gif",".css",".html"]

    def __init__(self):
        super().__init__()

    def parse(self,path,source,dest):
        super.copy(path,source,dest)
