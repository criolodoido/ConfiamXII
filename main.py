#!/usr/bin/env python
# -*- coding: utf-8 -*-
import kivy, time, webbrowser
from kivy.app import App
from kivy.app import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.core.window import Window;

class PrimeiroScreen(Screen):
	def __init__(self, **kwargs):
		self.name = 'um'
		super(Screen,self).__init__(**kwargs)

class SegundoScreen(Screen):
	def __init__(self, **kwargs):
		self.name = 'dois'
		super(Screen,self).__init__(**kwargs)
		
	def abre(self):
		webbrowser.open('http://www.inscricoes.fmb.unesp.br/principal.asp')


class MinicursosScreen(Screen):
	def __init__(self, **kwargs):
		self.name = 'mc'
		super(Screen,self).__init__(**kwargs)
		
class PalestrantesScreen(Screen):
	def __init__(self, **kwargs):
		self.name = 'pa'
		super(Screen,self).__init__(**kwargs)
	
	
	
class RootScreen(ScreenManager):
    pass
    
class mudaApp(App):
	title = 'XIIConfiam!'
	def on_pause(self):
		return True
		
	def on_resume(self):
	   
	   pass
      
	def build(self):
		return RootScreen()
if __name__ == '__main__':
    appVar = mudaApp()
    mudaApp().run()
