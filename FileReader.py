from setuptools.command.build import build

from FileReaderInterface import FileReaderInterface, contextmanager

class FileReader(FileReaderInterface):
    @contextmanager
    def read_file(self, file_name: str, buffer_size: int):
        try:
            file = open(file_name, "r")
            chunks = []
            chunk = file.read(buffer_size)
            while len(chunk) > 0:
                chunks.append(chunk)
                chunk = file.read(buffer_size)
            yield chunks
        except FileNotFoundError:
            print("File not found")
        finally:
            file.close()

