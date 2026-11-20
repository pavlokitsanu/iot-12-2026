class File:
    def __init__(self, name, extension, size):
        self._name = name
        self._extension = extension
        self._size = size
        print(f"Створено файл {self.full_name}")

    def __del__(self):
        print(f"Видалено файл {self.full_name}")

    @property
    def name(self):
        return self._name

    @property
    def extension(self):
        return self._extension

    @property
    def size(self):
        return self._size

    @property
    def full_name(self):
        return f"{self._name}.{self._extension}"

    def print_tree(self, indent=0):
        print("    " * indent + f"- {self.full_name} ({self._size} КБ)")

    def longest_path(self, path=""):
        return path + self.full_name


class Folder:
    def __init__(self, name):
        self._name = name
        self._items = []
        print(f"Створено папку {self._name}")

    def __del__(self):
        print(f"Видалено папку {self._name}")

    @property
    def name(self):
        return self._name

    @property
    def items(self):
        return self._items

    def add(self, item):
        self._items.append(item)

    def remove(self, item):
        self._items.remove(item)

    def print_tree(self, indent=0):
        print("    " * indent + f"+ {self._name}/")
        for item in self._items:
            item.print_tree(indent + 1)

    def longest_path(self, path=""):
        path += self._name + "/"
        best = path
        for item in self._items:
            candidate = item.longest_path(path)
            if len(candidate) > len(best):
                best = candidate
        return best


def main():
    root = Folder("root")
    docs = Folder("Documents")
    work = Folder("Work")
    pics = Folder("Pictures")

    root.add(docs)
    root.add(pics)
    docs.add(work)

    work.add(File("report", "pdf", 2450))
    work.add(File("budget", "xlsx", 380))
    docs.add(File("resume", "docx", 95))
    pics.add(File("photo", "jpg", 3200))
    root.add(File("readme", "txt", 2))

    print("\nДерево файлів:")
    root.print_tree()

    print("\nНайдовший шлях:", root.longest_path())

    print("\nВидаляємо папку Pictures:")
    root.remove(pics)
    root.print_tree()

    print("\nНовий об'єкт Folder:")
    my_folder = Folder("MyFolder")
    my_folder.add(File("notes", "txt", 12))
    my_folder.add(File("song", "mp3", 4500))
    my_folder.add(File("image", "png", 780))

    print("\nІмена всіх об'єктів у папці:")
    for item in my_folder.items:
        print(item.full_name)

    print("\nЗавершення програми:")


if __name__ == "__main__":
    main()

