import math
from mensch import Mensch
import logging
logger = logging.getLogger('spam_application')
logger.debug('----------------------------------- start logging in student 1')


class Student(Mensch):

    def __init__(self, vorname, nachname, geschlecht, alter, wohnort, status, semester, punktzahl, faecher: list, kurse: list) -> object:
        """
        :param str status: Neuling, Student, Junior, Senior
        :param int semester: Derzeitiges Semester des Studenten
        :param float punktzahl: Aktuelle Punktzahl des Studenten
        :param list feacher: Belegte Fächer des Studenten (1. Position = Hauptfach, 2. Position = Nebenfach)
        :param list kurse: Aktuelle Kurse im Semester
        :rtype: object
        """
        super().__init__(vorname, nachname, alter, wohnort, geschlecht)

        self.status = status
        self.semester = semester
        self.punktzahl = punktzahl
        self.faecher = faecher
        self.kurse = kurse

    def zeige_mich(self):
        """
        Gibt alle Werte eines Studenten aus
        """
        print("Vorname: " + self.vorname + "\n"
              "Nachname: " + self.nachname + "\n"
              "Geschlecht: " + self.geschlecht + "\n"
              "Alter: " + str(self.alter) + "\n"
              "Status: " + self.status + "\n"
              "Punktzahl: " + str(self.punktzahl) + "\n"
              "Semester: " + str(self.semester) + "\n"
              "Ort: " + str(self.wohnort) + "\n"                                        
              "Fächer: " + str(self.faecher) + "\n"
              "Kurse: " + str(self.kurse))
        logger.debug("Vorname: " + self.vorname + "\n"
              "Nachname: " + self.nachname + "\n"
              "Geschlecht: " + self.geschlecht + "\n"
              "Alter: " + str(self.alter) + "\n"
              "Status: " + self.status + "\n"
              "Punktzahl: " + str(self.punktzahl) + "\n"
              "Semester: " + str(self.semester) + "\n"
              "Ort: " + str(self.wohnort) + "\n"                                        
              "Fächer: " + str(self.faecher) + "\n"
              "Kurse: " + str(self.kurse))      

    def studier_zeit(self, studier_zeit):
        """
        Berechnet auf Basis der studier_zeit die neue Punktzahl des Studenten
        :param int studier_zeit:
        """
        if round(self.punktzahl + math.log(int(studier_zeit), 10), 1) < 4.0:
            self.punktzahl = round(self.punktzahl + math.log(int(studier_zeit), 10), 1)
        else:
            # max. 4.0 Punkte möglich
            self.punktzahl = 4.0

    def ergaenze_faecher(self,faecher):
        """
        *** AUFGABE ***
        SCHAFFE EINE MÖGLICHKEIT, UM DIE FÄCHERLISTE DES STUDENTEN UM WEITERE (x STÜCK) ZU ERGÄNZEN

        TIPPS:  - überlege, wie du die aktuelle Fächerliste ergänzen kannst
                - in welcher Datenstruktur liegen die Fächer aktuell vor
                - kannst du diese erweitern bzw. ergänzen?
                - was musst du der Methode mitgeben, damit es variabel von außen funktioniert
                - denke daran, dass du mit SELF auf die Attribute der Klasse zugreifen kannst
        """
        self.faecher.extend(faecher)




