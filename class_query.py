from dataclasses import dataclass
from typing import Optional

import marshmallow
import marshmallow_dataclass


@dataclass
class Query:
    file_name: Optional[str]
    cmd1: Optional[str]
    value1: Optional[str]
    cmd2: Optional[str]
    value2: Optional[str]

    class Meta:
        unknown = marshmallow.EXCLUDE


QuerySchema = marshmallow_dataclass.class_schema(Query)
