class Student:

    def __init__(self, id, name, averageGrade, matriculedCourses):
        self._id = id;
        self._name = name;
        self._averageGrade = averageGrade;
        self._matriculedCourses = matriculedCourses;

    def getId(self):
        return self._id;

    def getName(self):
        return  self._name

    def getAverageGrade(self):
        return self._averageGrade

    def getMatriculedCourses(self):
        return self._matriculedCourses

    def toString(self):
        return f"id:{self._id}, name:{self._name}, averageGrade:{self._averageGrade}"