class Classes:
    def __init__(self, titleClasse, minutesClasses):
        self._titleClasse = titleClasse;
        self._minutesClasses = minutesClasses;

    def getTittleClasse(self):
        return self._titleClasse

    def getMinutes(self):
        return self._minutesClasses;

    def toString(self):
        return f"tittleClasse: {self._titleClasse}, minutes:{self._minutesClasses}"