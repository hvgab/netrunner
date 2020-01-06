import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ListProperty

class Player():
	agendapoints = NumericProperty(0)
	credits = NumericProperty(0)
	trashpile = ListProperty([])
	click = NumericProperty(0)
	handofcards = ListProperty([])
	drawdeck = ListProperty([])



class NetrunnerGame(BoxLayout):
	pass


class NetrunnerApp(App):
	def build(self):
		self.title = 'Android Netrunner'
		game = NetrunnerGame()
		return game

if __name__ == '__main__':
	NetrunnerApp().run()