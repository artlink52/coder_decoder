from setuptools.command.build import build

from FileReaderInterface import FileReaderInterface, contextmanager

class FileReader(FileReaderInterface):
    @contextmanager
    def read_file(self, file_name: str, buffer_size: int):
        try:
            file = open(file_name, "r")
            def read_chunks():
                while True:
                    chunk = file.read(buffer_size)
                    if not chunk:
                        break
                    yield chunk
            yield read_chunks()
        except FileNotFoundError:
            print("File not found")
        finally:
            file.close()

