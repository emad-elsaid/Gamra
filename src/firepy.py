'''
Created on Jun 3, 2010

@author: blaze
'''

from wx import App
from MainFrame import MainFrame

class Firepy(App):
    def OnInit(self):
        self.AppName = "Firepy"
        self.VendorName = "Schoolar Projects"
        self.Version = "0"
        
        frame = MainFrame()
        frame.Show(True)
        self.SetTopWindow(frame)
        return True


if __name__ == '__main__':
    firepy_obj = Firepy()
    firepy_obj.MainLoop()