from src.protocols.source_protocol import TaskSource
from src.models.task import Task


class TaskProcessor:
    def process(self, source: TaskSource) -> None:
        if not isinstance(source, TaskSource):
            print(f"Ошибка: {type(source).__name__} не соответствует контракту TaskSource")
            return

        print(f"{type(source).__name__} прошёл проверку контракта")

        try:
            tasks: list[Task] = source.get_tasks()
        except Exception as e:
            print(f"Ошибка при получении задач: {e}")
            return

        print(f"Получено {len(tasks)} задач")

        for task in tasks:
            print(f"Задача {task.id}: {task.payload}")
