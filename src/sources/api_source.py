from src.models.task import Task
from typing import List, Dict, Any


class ApiSource:
    def __init__(self) -> None:
        self._data: List[Dict[str, Any]] = [
            {"id": 1, "text": "Помыть посуду"},
            {"id": 2, "text": "Сходить в магазин"},
            {"id": 3, "text": "Сделать дз"},
        ]

    def get_tasks(self) -> List[Task]:
        tasks: List[Task] = []
        for item in self._data:
            task = Task(
                id=str(item["id"]),
                payload=item["text"]
            )
            tasks.append(task)
        return tasks
