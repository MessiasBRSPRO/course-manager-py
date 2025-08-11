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

    def __eq__(self, other):
        #If two 2 objects are equals, the hash code are equals too
        if not isinstance(other, Teacher):
            return NotImplemented
        return self._id == other._id

    def __hash__(self):
        return hash(self._id)

    def toString(self):
        return f"Teacher name:{self._name}, matters:{self._matters}, graduation description:{self._graduation}, teach Courses:{self._teachCourses}"