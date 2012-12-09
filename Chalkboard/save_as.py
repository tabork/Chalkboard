import wx

class save():
   def saveas(self):
      application = wx.PySimpleApp()

      # Create a save file dialog

      filters = '(*.png)|*.png|(*.jpg)|*.jpg|(*.bmp)|*.bmp'

      dialog = wx.FileDialog ( None, style = wx.SAVE | wx.OVERWRITE_PROMPT, wildcard = filters )

      # Show the dialog and get user input

      if dialog.ShowModal() == wx.ID_OK:
         dv = dialog.GetPath()
         if dialog.GetFilterIndex() == 0:
            if ".png" not in dv:
               dv = dv + ".png"
         elif dialog.GetFilterIndex() == 1:
            if ".jpg" not in dv:
               dv = dv + ".jpg"
         elif dialog.GetFilterIndex() == 2:
            if ".bmp" not in dv:
               dv = dv + ".bmp"
         dialog.Destroy()
         return dv
      else:
         dialog.Destroy()
         return None

      
