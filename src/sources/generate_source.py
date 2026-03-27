from src.models.task import Task
import random
from typing import List, Optional


class Generate:
    TASK_TEXTS = [
        "поспать",
        "поесть",
        "погулять",
        "посмотреть фильм",
        "почитать книгу",
        "написать код",
        "проверить почту",
        "сделать уборку",
        "поиграть в игры",
        "позвонить родителям",
    ]

    def __init__(self, count: Optional[int] = None) -> None:
        if count is None:
            self.count = random.randint(1, 10)
        else:
            self.count = count

    def _get_task_text(self) -> str:
        return random.choice(self.TASK_TEXTS)

    def get_tasks(self) -> List[Task]:
        print(f"Генерация {self.count} задач")
        tasks: List[Task] = []
        for i in range(1, self.count + 1):
            task_text = self._get_task_text()
            task = Task(
                id=str(i),
                payload=task_text
            )
            tasks.append(task)
        return tasks