# First things, first. Import the wxPython package.
import wx

# Next, create an application object.
app = wx.App()

# Then a frame.
frm = wx.Frame(None, title="Hello World")

# Show it.
frm.Show()

# Start the event loop.
app.MainLoop()

"""
see also from https://www.programcreek.com/python/example/3163/wx.FileDialog

https://stackoverflow.com/questions/55698056/minimal-wx-filedialog-example-freezes-program
"""
