'''
Created on Jun 4, 2010

@author: Ahmed Ghanem
'''
import wx
class Splash(wx.Frame):
	#============= Creating Gamra SplashSceen
	def __init__(self, splashTime):
		wx.Frame.__init__( self, None, -1, style=wx.FRAME_NO_TASKBAR|wx.FRAME_NO_WINDOW_MENU)
		
		image = wx.Image("data/splash/splash.png").ConvertToBitmap()                                               
		
		wx.StaticBitmap(self,-1,image)
		self.Fit()
		self.CenterOnScreen()
		
		self.Show()
		wx.Yield()
		wx.Sleep(splashTime)
		self.Hide()
		self.Destroy()
		
