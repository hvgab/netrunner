
import logging

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

class Deck(object):
	""" The Deck a player has to play with. """
	def __init__(self, cards:list):
		super(Deck, self).__init__()
		self.cards = cards

	def shuffle(self):

		random.shuffle(deck)
		random.shuffle(deck)
		random.shuffle(deck)
		random.shuffle(deck)
		random.shuffle(deck)

	def draw(self, arg):
		pass
