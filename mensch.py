class Mensch:

    def __init__(self, vorname, nachname, alter, wohnort, geschlecht):
        """
        :param str vorname: Vorname des Menschen
        :param str nachname: Nachname des Menschen
        :param int alter: Alter des Menschen
        :param str wohnort: Wohnort des Menschen
        :param str geschlecht: Männlich oder weiblich
        """
        self.vorname = vorname
        self.nachname = nachname
        self.alter = alter
        self.wohnort = wohnort
        self.geschlecht = geschlecht


