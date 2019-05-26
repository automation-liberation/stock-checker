from dataclasses import dataclass, asdict


@dataclass
class BaseDao:
    @property
    def as_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, dict_data):
        dao = {}
        for key, value in cls.__annotations__.items():
            dao[key] = dict_data.get(key)

        return cls(**dao)
