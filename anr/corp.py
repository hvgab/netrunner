
import logging

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

class Corp(Player):
	"""docstring for Corp."""
	def __init__(self):
		super(Corp, self).__init__()
