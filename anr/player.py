
import logging

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

class Player(object):
	"""docstring for Player."""
	def __init__(self):
		super(Player, self).__init__()

		self.playername = playername
		self.identity = identity
		self.deck = deck
		self.discard_pile = []
		self.clicks = 0
		self.clicks_left = 0
		self.credits = 0
		self.hand = []
