import wx

class open_f():
   def openfile(self):
      application = wx.PySimpleApp()

      # Create a save file dialog

      filters = '(*.png)|*.png|(*.jpg)|*.jpg|(*.bmp)|*.bmp'

      dialog = wx.FileDialog ( None, style = wx.OPEN, wildcard = filters )

      # Show the dialog and get user input

      if dialog.ShowModal() == wx.ID_OK:
         dialog.Destroy()
         return dialog.GetPath()
      else:
         dialog.Destroy()
         return None
