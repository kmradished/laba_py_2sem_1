from src.models.task import Task
from typing import List


class FileSource:
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath

    def get_tasks(self) -> List[Task]:
        try:
            with open(self.filepath, 'r', encoding='utf-8') as file:
                tasks: List[Task] = []
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) != 2:
                        print(f"Неверный формат строки: {line.strip()}. Ожидается 2 части, разделённые запятыми.'")
                        continue
                    task = Task(id=parts[0].strip(), payload=parts[1].strip())
                    tasks.append(task)
                return tasks
            
        except FileNotFoundError:
            print(f"Файл {self.filepath} не найден. Возвращаю тестовые задачи.")
            return [
                Task("1", "тест1"),
                Task("2", "тест2"),
                Task("3", "тест3")
            ]
