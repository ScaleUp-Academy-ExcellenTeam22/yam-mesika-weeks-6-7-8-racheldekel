class RegularUser:
    """
    Saved the regular users
    """

    def __init__(self, username: str, password: str, manager=False):
        self.username = username
        self.password = password
        self.manager = manager


class SystemAdministrator:
    """
        Saved the system administrator users
        """

    def __init__(self):
        self.root = []

    def mkdir(self, path):
        self.root.append(Directory(path))


class Directory:
    """
     Class's for all the directories.
     contains a file functions
    """

    def __init__(self, name):
        self.name = name
        self.files_list = []

    def add_file(self, file):
        if file not in self.files:
            self.files.append(file)

    def remove_file(self, file_name):
        for file in self.files:
            if file.get_name() == file_name:
                self.files.remove(file)
                return True
        return False


class File:
    """
    Class for all files params
    """

    def __init__(self, file_name: str, weight: float, content: str, composer):
        self.name = file_name
        self.weight = weight
        self.content = content
        self.composer = composer

    def read(self, user):
        if self.composer == user.username or user.managr:
            return self.content
        else:
            return None


class Text(File):
    """
    Class for text files
    """

    def __init__(self, weight, content, composer):
        super().__init__(weight, content, composer)

    def count(self, words):
        return self.content.count(words)


class Binary(File):
    """
    Class for binary files
    """

    def __init__(self, weight, content, composer):
        super().__init__(weight, content, composer)


class Image(Binary):
    """
    Class for image files
    """

    def __init__(self, weight, content, composer):
        super().__init__(weight, content, composer)

    def get_dimensions(self):
        pass
