from Teacher import Teacher


class Course:
    def __init__(self, courseName, teacher):
        if type(teacher) == Teacher:
            self._courseName = courseName;
            self._classes = [];
            self._students = [];
        else:
            print("only teacher can create a Course")

    def getCourseName(self):
        return self._courseName;

    def getClasses(self):
        return self._classes;

    def getStudents(self):
        return self._students;

    def toString(self):
        return f"Course:{self._courseName}, Classes:{self.getClasses()}, Students:{self._students}"