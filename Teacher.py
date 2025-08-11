class Teacher:

    def __init__(self, id, name, matter, graduation):
        self._id = id
        self._name = name;
        self._matters = matter;
        self._graduation = graduation;
        self._teachCourses = [];

    def getName(self):
        return self._name

    def getId(self):
        return self._id

    def getMatter(self):
        return self._matters

    def getGraduation(self):
        return self._graduation

    def getTeachCourses(self):
        return self._teachCourses

    def toString(self):
        return f"Teacher name:{self._name}, matters:{self._matters}, graduation description:{self._graduation}, teach Courses:{self._teachCourses}"