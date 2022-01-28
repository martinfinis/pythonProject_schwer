from pickle import NONE
import pandas
from pandas.core.frame import DataFrame
from hiwi import Hiwi
from student import Student as st
import csv_handler as csvH
import pandas as pd
import ast
from csv_handler import CsvHandler
import wx
import logging
from ast import literal_eval

# create logger with 'spam_application'
logger = logging.getLogger('spam_application')
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)
logger.debug('####################################### start logging in main 1')


class Hauptklasse:
    logger.debug('Hauptklasse 1')
    def __init__(self):
        """
        Constructor mit leerer Studentenliste und leerem Data Frame
        """
        logger.debug('Hauptklasse init 2')
        #self.dataFrame: pandas.DataFrame
        self.dataFrame: None
        self.studentenListe = []

    def create_data_frame(self, filename):
        """
        Diese Methode öffnet eine CSV-Datei und schreibt die Daten in Pandas Data Frame Objekt

        *** done AUFGABE ***
        Lade die DAten aus der CSV Datei in ein pandas Data Frame hinein

        TIPPS:  - Achtung: du musst dir überlegen, wie du mit den Listen aus dem CSV umgehen willst
                - Listen lassen sich über die converter Funktion des Data Frames importieren (schau mal im Internet nach)
        """
        """todo"""
        logger.debug('Hauptklasse create_data_frame 3')
        self.dataFrame = pd.read_csv(filename,sep=';')
        #return 
        #pass

    def lade_studenten(self):
        """
         *** done AUFGABE ***
        Nutze den Data Frame (pandas) der Klasse, um die Liste studentenListe mit den Studenten und ihren Werten zu füllen

        TIPPS:  - überlege wie du die Daten aus dem Data Frame in die Liste übertragen kannst
                - die Methode gibt sonst nichts zurück
        """
        logger.debug('Hauptklasse start lade_studenten 4')

        #todo remove file comment
        app = wx.App(False)
        csvHandler = CsvHandler(None, "read student file")
        app.MainLoop()
        filename = csvHandler.returnFilename()
        #csv = csvH.CsvHandler(None,"read student file")
        #csv.initiateFileHandler()
        #filename='C:\\_dev\\python_basics\\pythonProject_schwer\\pythonProject_schwer\\students.csv'
        self.create_data_frame(filename)

        # put data from csv file into student objects
        """ replace """
        # 1             2       3          4      5        6        7        8           9          10
        # vorname, nachname, geschlecht, alter, wohnort, status, semester, punktzahl, faecher: [], kurse: []) -> object:
        #vorname;nachname;geschlecht;alter;wohnort;status;semester;punktzahl;faecher;kurse
        for index, row in self.dataFrame.iterrows():
            logger.debug('create student row:'+str(row))
            value = row['vorname']
            self.studentenListe.append(st(row[0],row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8],row[9]))
        logger.debug(f"Anzahl der Studenten {len(self.studentenListe)}")    
        logger.debug('Hauptklasse end lade_studenten 4')


    def map_student_to_hiwi(self, Student: st):
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
        hiwi_student = Hiwi( st.vorname, st.nachname, st.geschlecht, st.alter, st.wohnort, st.status, st.semester, st.punktzahl
        , lehrstuhl, professor, st.faecher,st.kurse, betreuteKurse)
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
        hiwi = NONE
        for i in haupt.studentenListe:
            hiwi_ja_nein = input(f"soll hiwi werden?{i.name}")
            if hiwi_ja_nein == ja:
                hiwi = self.map_student_to_hiwi(i)
                break

        print()
        #welcherStudent = "todo"
        #hiwi = "todo"
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
        average_age = self.dataFrame['alter'].mean()
        average_semester = self.dataFrame['semester'].mean()
        anzahl_studenten = len(self.dataFrame)
       

        self.dataFrame['faecher2']= self.dataFrame.faecher.apply(literal_eval)
        faecher_dic = {}
        for i,faecher in self.dataFrame['faecher2']:
            for fach in faecher:
                if fach in faecher_dic:
                    value = faecher_dic.get(fach)
                    value = value + 1
                    faecher_dic.update(fach,value)
                else:         
                    faecher_dic.update(fach,1)
            


        #average_age = "todo"
        #average_semester = "todo"
        print('Das Durchschnittsalter aller Studenten beträgt: ' + average_age)
        print('Das Durchschnitts-Semester aller Studenten beträgt: ' + average_semester)

        faecher_counter = len(faecher_dic)

        print()
        print(faecher_counter)
        print()

        
        
        print("Das häufigste Fach ist: " + "todo" + ". Es kam " + "todo" + "x vor.")




# den grünen Play-Pfeil in der IDE/SEU drücken, damit das Programm startet
if __name__ == '__main__':
    logger.debug('start logging in main method 1')
    
    
    haupt = Hauptklasse()
    haupt.lade_studenten()


    #zeige Daten des 1. Studenten in der Liste
    logger.debug(f"Anzahl der Studenten {len(haupt.studentenListe)}")
    logger.debug("Zeigt die Daten des 1. Studenten in der Liste\n")
    logger.debug(f"{haupt.studentenListe[0].zeige_mich()}")
    haupt.studentenListe[0].zeige_mich()
    
    
    #die Studenten studieren
    haupt.wir_studieren()

    #zeige u.a. veränderte Punktzahl nach Studierzeit des 1. Studenten in der Liste
    logger.debug(("So sieht der 1. Student nach der Studierzeit aus:\n"))
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

