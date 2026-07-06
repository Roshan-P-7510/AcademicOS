import json
from pathlib import Path
from typing import List


class RecentService:

    FILE_PATH = Path.home() / ".academicos_recent.json"
    MAX_ITEMS = 10

    @staticmethod
    def load() -> List[str]:
        if not RecentService.FILE_PATH.exists():
            return []

        try:
            return json.loads(RecentService.FILE_PATH.read_text())
        except Exception:
            return []

    @staticmethod
    def add(path: str):

        items = RecentService.load()

        if path in items:
            items.remove(path)

        items.insert(0, path)

        items = items[: RecentService.MAX_ITEMS]

        RecentService.FILE_PATH.write_text(json.dumps(items, indent=2))