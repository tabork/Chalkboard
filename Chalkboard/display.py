import wx

class disp():
   def display(self):
      application = wx.PySimpleApp()

      dialog = wx.MessageDialog(parent=None,message="Would you like to save changes before you continue?",caption="Save Changes?",style = wx.YES_NO | wx.YES_DEFAULT)
      if dialog.ShowModal() == wx.ID_YES:
         dialog.Destroy()
         return True
      else:
         dialog.Destroy()
         return False

      
