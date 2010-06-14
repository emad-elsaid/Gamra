'''
Created on Jun 14, 2010

@author: blaze

@summary: This is like a Database tables of our Application Data
            it contain all data structure of the Image Document, and may
            contain library structure and so.
'''

class Path:
    def Apply(self, context ): pass
    def ToData(self): pass
    def FromData(self, data): pass

class Stroke:
    def Apply(self, context ): pass
    def ToData(self): pass
    def FromData(self, data): pass

class Fill:
    def Apply(self, context ): pass
    def ToData(self): pass
    def FromData(self, data): pass
    
class Object:
    '''
    the main object, out Image document will contain 
    many object of this we'll render them over each 
    others using the document Render
    '''
    def __init__(self):
        self.Path = Path()
        self.Stroke = Stroke()
        self.Fill = Fill()
        self.Visible = True
        self.Locked = False
        
    def Render(self): pass
    def ToData(self): pass
    def FromData(self, data): pass
       
class MetaData:
    '''
    this is the meta data class for document
    it'll hold all data of the author, creation date
    last modification...etc.
    '''
    
    def __init__(self):
        self.Author = ''
        self.Created = ''
        self.Modified = ''
        self.Comment = ''
    def ToData(self): pass
    def FromData(self, data): pass
    
class Document:
    '''
    Image main document
    '''
    def __init__(self,width,height):
        self.MetaData = MetaData
        self.Objects = []
        self.ToolObjects = []
        
    def Render(self): pass
    def ToData(self): pass
    def FromData(self, data): pass