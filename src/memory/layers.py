from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, List

@dataclass
class Entry:
    key: str
    value: Any
    layer: str
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

class Store:
    def __init__(self):
        self.data = {"working": [], "episodic": [], "semantic": []}
    def put(self, layer: str, key: str, value: Any):
        self.data[layer].append(Entry(key, value, layer))
