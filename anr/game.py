
import logging

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

class Game(object):
	"""docstring for Game."""
	def __init__(self, arg):
		super(Game, self).__init__()
		self.winner = None

	def setup(self):
		pass

	def run(self):
		while not self.winner:
			corp.turn
			runner.turn
