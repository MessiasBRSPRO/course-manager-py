class Student:

    def __init__(self, id, name):
        self._id = id
        if len(self._id) != 5:
            print("the id will have 5 numbers")
            self._id = None
        self._name = name;
        self._averageGrade = 0.0;
        self._matriculedCourses = [];

    def getId(self):
        return self._id;

    def getName(self):
        return  self._name

    def getAverageGrade(self):
        return self._averageGrade

    def getMatriculedCourses(self):
        return self._matriculedCourses

    def __eq__(self, other):
        #If two 2 objects are equals, the hash code are equals too
        #in this case, a student can have the same name, but not the same id(matricula)
        if not isinstance(other, Student):
            return NotImplemented
        return self._id == other._id

    def __hash__(self):
        return hash(self._id)

    def toString(self):
        return f"id:{self._id}, name:{self._name}, averageGrade:{self._averageGrade}"