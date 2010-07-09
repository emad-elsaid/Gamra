'''
Created on Jul 8, 2010

@author: blaze
'''
import wx

class Generic(object):
    '''
    Generic Exporter is the parent of all exporters
    exporter: a class reponsible for exporting the document to file
    '''


    def __init__(self,label='Generic Exporter',mask='All Files (*.*)|*.*',extension=''):
        # menu Item text for that
        self.Label = label 
        #mask for Dialog
        self.Mask = mask
        # the file extension of the exported file 
        self.Extension = extension 
        # the file path to export, this will be changed by a Prepare method
        self.File = ''
       
    def Prepare(self):
        frame = wx.GetApp().Frame
        saveDLG = wx.FileDialog( frame, self.Label, wildcard=self.Mask, style=wx.FD_SAVE )
        
        if saveDLG.ShowModal()==wx.ID_OK :
            self.File = saveDLG.GetPath()
            if not self.File.endswith('.'+self.Extension) :
                self.File += '.'+self.Extension
                
            self.File = str(self.File)
            return True
        else:
            return False
         
    def Export(self):
        pass
    
    # i added *args because this function will be bind to event
    def Launch(self, *args):
        if self.Prepare() :
            self.Export()
    
if __name__ == '__main__':
    app = wx.App()
    g = Generic()
    g.Prepare()
    app.MainLoop()