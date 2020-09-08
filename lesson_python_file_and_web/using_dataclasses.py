from dataclasses import dataclass

@dataclass
class SongDataClass:
    title: str
    length: int

s = SongDataClass('mysong', 300)
print(s)
