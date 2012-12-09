import wx

class save():
   def saveas(self):
      application = wx.PySimpleApp()

      # Create a save file dialog

      filters = '(*.png)|*.png|(*.jpg)|*.jpg|(*.bmp)|*.bmp|(*.gif)|*.gif'

      dialog = wx.FileDialog ( None, style = wx.SAVE | wx.OVERWRITE_PROMPT, wildcard = filters )

      # Show the dialog and get user input

      if dialog.ShowModal() == wx.ID_OK:
         dialog.Destroy()
         return dialog.getPath()
      else:
         dialog.Destroy()
         return None

      
