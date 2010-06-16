'''
Created on Jun 4, 2010

@author: Ahmed Ghanem
'''
import wx
class GamraSplash():
	#============= Creating Gamra SplashSceen
	def __init__(self, splashName, splashTime):
		image = wx.Image(splashName)                                                 
		bmpSplash = image.ConvertToBitmap() # convert image to bitmap
		wx.SplashScreen(bmpSplash, wx.SPLASH_CENTRE_ON_SCREEN | 
		wx.SPLASH_TIMEOUT, splashTime, None, -1)
		#wx.Sleep(splashTime/1000) #sleep until the splash and calculate sec
		
