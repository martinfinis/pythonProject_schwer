import wx

class CsvHandler:

    def __init__(self):
        self.filename = None

    def onButton(self, event):
        print("Button pressed")

    def initiateFileHandler(self):
        """
        Nutzt den Filehandler der Bibliothek wx um ein File auszuwählen

        *** AUFGABE ***
        Nutze einen filehandler um das CSV file auf dem Rechner zu suchen und auszuwählen

        TIPPS:  - nutze die Bibliothek wx dazu oder wähle einen eigenen Weg
                - Recherche im Internet hilft!
        """
        """todo"""

    def returnFilename(self):
        """
        gibt den Filenamen zurück
        :return: der Filename
        """
        return self.filename

    def writebacktofile(self):
        pass

