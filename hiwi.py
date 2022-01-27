from student import Student

import logging
logger = logging.getLogger('spam_application')
logger.debug('----------------------------------- start logging in hiwi 1')


class Hiwi(Student):
	def __init__(self, vorname, nachname, geschlecht, alter, wohnort, status, semester, punktzahl, lehrstuhl, professor, faecher: [],
                 kurse: [], betreuteKurse = []):
		super.__init__(vorname, nachname, geschlecht, alter, wohnort, status, semester, punktzahl, faecher, kurse)

		self.betreuteKurse = betreuteKurse
        self.lehrstuhl = lehrstuhl
        self.professor = professor

	def zeige_lehrstuhl(self):
        """
        Zeigt den Lehrstuhl des Studenten
        """
        print("Ich bin am Lehrstuhl: " + self.lehrstuhl)
		logger.debug("Ich bin am Lehrstuhl: " + self.lehrstuhl)

    def zeige_betreuteKurse(self):
        """
        Zeigt die Kurse, die der Student betreut
        """
        print("Ich betreue folgende Kurse: " + str(self.betreuteKurse))

    def zeige_professor(self):
        """
        Zeigt den Professor des Studenten
        """
        print("Ich arbeite bei Professor: " + self.professor)


    """
            *** AUFGABE ***
            Implementiere die Klasse Hiwi

            TIPPS:  - die Klasse erbt von Student
                    - sie hat 3 zusätzliche Attribute:
                        - lehrstuhl (String)
                        - betreuteKurse (als Liste)
                        - professor (String)
                    - drei Methoden sollen die zusätzlichen Attribute einfach als print() auf dem Screen ausgeben
                    - zeige_lehrstuhl()
                    - zeige_betreuteKurse()
                    - zeige_professor()
            """

    pass