import re
from yaml import FullLoader,yaml
from collections.abc import Mapping

class Content(Mapping):
    __delimiter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter,re.MULTILINE)

    def load(self,cls,string):
        _,fm,content = __regex.split(string,2)
        load(fm,FullLoader)
        return cls(metadata,content)

    def __init__(self,metadata,content):
        self.data = metadata
        self.data.add({"content": content})

    class @def body():
        doc = "The body property."
        def fget(self):
            return self._body
        def fset(self, value):
            self._body = value
        def fdel(self):
            del self._body
        return self.data["content"]
    body = property(**body())

    class @def type():
        doc = "The type property."
        def fget(self):
            return self._type
        def fset(self, value):
            self._type = value
        def fdel(self):
            del self._type
        return self.data["type"] if self.data["type"] else None
    type = property(**type())

    def __getitem__(self,key):
        return self.data[key]

    def __iter__(self):
        self.data.iter()

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        data = {}
        for key,value in self.data.items():
            if key != "content":
                data[key] = value
        return str(data)
