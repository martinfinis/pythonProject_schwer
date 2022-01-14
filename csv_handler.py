import wx

class CsvHandler(wx.Frame):
    

    def __init__(self, parent, title):
        self.filename = None
        # A "-1" in the size parameter instructs wxWidgets to use the default size.
        # In this case, we select 200px width and the default height.
        wx.Frame.__init__(self, parent, title=title, size=(400,400))

        # Setting up the menu.
        filemenu= wx.Menu()
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open"," Open a file to edit")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

        # Events.
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)

        self.Show()

    def OnOpen(self,e):
        """ Open a file"""
        with wx.FileDialog(self, "Open XYZ file", wildcard="*.*",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return     # the user changed their mind

            # Proceed loading the file chosen by the user
            self.filename = fileDialog.GetPath()
            print(self.filename)

    def returnFilename(self):
        """
        gibt den Filenamen zurück
        :return: der Filename
        """
        return self.filename

    def writebacktofile(self):
        pass