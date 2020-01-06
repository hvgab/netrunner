
import logging

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

class Runner(Player):
	"""docstring for Runner."""
	def __init__(self):
		super(Runner, self).__init__()
