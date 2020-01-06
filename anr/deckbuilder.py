import json

import logging

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

class deckbuilder(object):
	"""docstring for deckbuilder."""
	def __init__(self, arg):
		super(deckbuilder, self).__init__()
		self.arg = arg

	def get_set(self, set_code):
		set_filename = set_code + '.json'
		with open(set_filename, encoding='utf-8') as set_file:
			return json.loads(set_file.read())

	def get_deck(self, set, faction, faction_side):
		deck = []
		for card in set:
			if card.faction_code == faction:
				deck.extend([card] * card['quantity'])

			if card['faction_code'] == 'neutral' and card['side_code'] == faction_side:
				temp_deck.extend([card] * card['quantity'])
				#print(card['title'] + ' * ' + str(card['quantity']))

		#print (type(temp_deck))

		return temp_deck
