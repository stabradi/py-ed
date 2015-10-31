################################################################################
# The standard buffer has no file index and all of the contents must reside in
# memory. When the buffer is saved to disk, it will have to return a file_buffer
# object
class buffer:
    def __init__(self):
        self.open_lines = []

class file_buffer:
    def __init__(self, file_name, open_lines=[]):
        self.open_lines
