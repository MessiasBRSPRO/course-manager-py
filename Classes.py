class Classes:
    def __init__(self, titleClasse, minutesClasses):
        self._titleClasse = titleClasse;
        self._minutesClasses = minutesClasses;

    def getTittleClasse(self):
        return self._titleClasse

    def getMinutes(self):
        return self._minutesClasses;

    def __eq__(self, other):
        #If two 2 objects are equals, the hash code are equals too
        if not isinstance(other, Classes):
            return NotImplemented
        return self._titleClasse == other._titleClasse

    def __hash__(self):
        return hash(self._titleClasse)

    def toString(self):
        return f"tittleClasse: {self._titleClasse}, minutes:{self._minutesClasses}"