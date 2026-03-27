from src.sources.file_source import FileSource
from src.sources.generate_source import Generate
from src.processors.task_processor import TaskProcessor
from src.sources.api_source import ApiSource


def main() -> None:
    processor = TaskProcessor()

    file_source = FileSource("data/tasks.txt")
    processor.process(file_source)

    gen_source = Generate(5)
    processor.process(gen_source)

    api_source = ApiSource("demo_api")
    processor.process(api_source)


if __name__ == "__main__":
    main()