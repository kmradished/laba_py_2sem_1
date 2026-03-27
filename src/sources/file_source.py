from src.models.task import Task
from typing import List


class FileSource:
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath

    def get_tasks(self) -> List[Task]:
        try:
            with open(self.filepath, 'r', encoding='utf-8') as file:
                tasks: List[Task] = []
                for line_number, line in enumerate(file, start=1):
                    line = line.strip()
                    if line:
                        tasks.append(Task(str(line_number), line))
                return tasks
        except FileNotFoundError:
            print(f"Файл {self.filepath} не найден. Возвращаю тестовые задачи.")
            return [
                Task("1", "тест1"),
                Task("2", "тест2"),
                Task("3", "тест3")
            ]
