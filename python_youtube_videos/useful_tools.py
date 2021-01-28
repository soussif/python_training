import logging

logger = logging.getLogger(__name__)

# create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# Level and format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

stream_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(stream_format)
file_h.setFormatter(file_format)

# Add handlers to the logger
logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('This is a warning') # logged to the stream
logger.error('This is an error') # logged to the stream AND the file!


class Student:

    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False


class SpecialStudent(Student):

    def special_student(self):
        return "this student is special"
