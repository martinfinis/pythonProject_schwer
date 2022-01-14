import pandas
from student import Student as st
from hiwi import Hiwi
import CsvHandler as csvH
import pandas as pd
import ast
from CsvHandler import CsvHandler
import wx


class Hauptklasse:

    def __init__(self):
        """
        Constructor mit leerer Studentenliste und leerem Data Frame
        """
        self.dataFrame: pandas.DataFrame
        self.studentenListe = []

    def create_data_frame(self, filename):
        """
        Diese Methode öffnet eine CSV-Datei und schreibt die Daten in Pandas Data Frame Objekt

        *** AUFGABE ***
        Lade die DAten aus der CSV Datei in ein pandas Data Frame hinein

        TIPPS:  - Achtung: du musst dir überlegen, wie du mit den Listen aus dem CSV umgehen willst
                - Listen lassen sich über die converter Funktion des Data Frames importieren (schau mal im Internet nach)
        """
        """todo"""

        #return self.dataFrame
        pass

    def lade_studenten(self):
        """
         *** AUFGABE ***
        Nutze den Data Frame (pandas) der Klasse, um die Liste studentenListe mit den Studenten und ihren Werten zu füllen

        TIPPS:  - überlege wie du die Daten aus dem Data Frame in die Liste übertragen kannst
                - die Methode gibt sonst nichts zurück
        """
        csv = csvH.CsvHandler()
        csv.initiateFileHandler()
        self.create_data_frame(csv.returnFilename())

        # put data from csv file into student objects
        """ replace """


    def map_student_to_hiwi(self, student: st):
        """
        Erzeugt ein Hiwi-Objekt aus dem gewählten Studenten-Objekt
        :param student: der gewählte Student wird übergeben
        :return: der erzeugte Hiwi-Student
        """
        professor = "Prof. Einstein"
        lehrstuhl = "Mathematik"
        betreuteKurse = ["Stochastik", "Lineare Algebra"]


        """
         *** AUFGABE ***
        Erstelle einen Hiwi-Studenten mit den Daten des Studenten, den die Methode übergeben bekommt.

        TIPPS:  - schau dir die Konstruktoren der Klassen Hiwi und Student an und überlege, wie du unten bei todo 
                weiter machen musst, damit aus dem Studenten ein Hiwi erzeugt wird.
                - der Hiwi erbt all Attribute und Fähigkeiten eines Studenten, hat aber drei neue Attribute: 
                siehe die obigen Parameter
        """
        hiwi_student = "todo."

        return hiwi_student


    def wer_wird_hiwi(self):
        """
        Funktion erstellt aus einem Studenten einen Hiwi

        *** AUFGABE ***
        Finde einen Weg den Benutzer zu fragen, welcher Student nun Hiwi werden soll

        TIPPS:  - wie kannst du eine Eingabe vom Benutzer abfragen?
                - gib dem Nutzer Hilfestellung und zeige ihm all verfügbaren Studenten
                - der Nutzer soll dann den Index (innerhalb der Liste) angeben, um einen Studenten zu wählen
                - lasse dann den Hiwi mit den Daten des gewählten Studenten erstellen
        """

        for i in haupt.studentenListe:
            "todo"
        print()
        welcherStudent = "todo"
        hiwi = "todo"
        print()
        print("Folgender Student ist nun Hiwi: ")
        hiwi.zeige_mich()
        print()
        return hiwi

    def wir_studieren(self):
        """
        in dieser Funktion studieren alle Studenten entsprechend der Werte in der Liste studierzeiten
        """
        # Studierzeiten für die Studenten
        studierzeiten = [60, 100, 40, 300, 20, 45, 150, 15, 200]

        # Studenten einzeln studieren lassen
        x = 0
        for i in haupt.studentenListe:
            i.studier_zeit(studierzeiten[x])
            x = x + 1

    def erstelle_Statistiken(self):
        """
        Durschschnittsalter der Studenten
        Durschschnittssemester der Studenten
        Häufigstes Fach?

         *** AUFGABE ***
        Beantworte obige Fragen und gib sie auf dem Screen aus

        TIPPS:  - wo bekommst du die nötigen Informationen her?
                - was musst du mit ihnen machen?
                - welche Strukturen bzw. Abläufe eignen sich dafür?
                - du brauchst keine speziellen Bibliotheken dafür; kannst du aber gerne nutzen
                - Tipp 1: iteriere über alle entsprechenden Werte der STudenten und bilde die Mittelwerte
                - Tipp 2: überlege dir, mit welcher Datenstruktur du recht gut die Häufigkeiten der Fächer zählen kannst
        """
        average_age = "todo"
        average_semester = "todo"
        anzahl_studenten = "todo"
        faecher_counter = "todo"

        for i in "todo":
            "todo"


        average_age = "todo"
        average_semester = "todo"
        print('Das Durchschnittsalter aller Studenten beträgt: ' + "todo")
        print('Das Durchschnitts-Semester aller Studenten beträgt: ' + "todo")

        "todo"

        print()
        print(faecher_counter)
        print()

        "todo"

        print("Das häufigste Fach ist: " + "todo" + ". Es kam " + "todo" + "x vor.")




# den grünen Play-Pfeil in der IDE/SEU drücken, damit das Programm startet
if __name__ == '__main__':

    app = wx.App(False)
    csvHandler = CsvHandler(None, "Main Gui")
    app.MainLoop()
    filename = csvHandler.returnFilename()

    haupt = Hauptklasse()
    haupt.lade_studenten()


    #zeige Daten des 1. Studenten in der Liste
    print()
    print("Zeigt die Daten des 1. Studenten in der Liste\n")
    haupt.studentenListe[0].zeige_mich()
    print()

    #die Studenten studieren
    haupt.wir_studieren()

    #zeige u.a. veränderte Punktzahl nach Studierzeit des 1. Studenten in der Liste
    print("So sieht der 1. Student nach der Studierzeit aus:\n")
    haupt.studentenListe[0].zeige_mich()

    #Liste mit neuen Fächern
    neue_faecher = ["Anglistik", "Chemie"]
    print()
    print("Folgende Fächer werden ergänzt: " + str(neue_faecher))
    print()
    #ergänze neue Fächer beim 1. Studenten der Studentenliste
    haupt.studentenListe[0].ergaenze_faecher(neue_faecher)
    # zeige mit ergänzten Fächern
    print("Hier der Student mit seinen neuen Fächerntodo\n")
    haupt.studentenListe[0].zeige_mich()
    print()

    #erzeuge einen Hiwi aus dem Studenten
    print("Wer wird Hiwi?\n")
    hiwi_student = haupt.map_student_to_hiwi(haupt.wer_wird_hiwi())
    hiwi_student.zeige_professor()
    hiwi_student.zeige_lehrstuhl()
    hiwi_student.zeige_betreuteKurse()
    print()


    #erstelle Statistiken zur Beantwortung der Fragen
    print("Nun zu den Statistiken:\n")
    haupt.erstelle_Statistiken()

