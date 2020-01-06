
import logging

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

class Card(object):
	"""docstring for Card."""
	def __init__(self, arg):
		super(Card, self).__init__()

		self.last_modified = last_modified
		self.code = code
		self.title = title
		self.type = type
		self.type_code = type_code
		self.subtype = subtype
		self.subtype_code = subtype_code
		self.text = text
		self.baselink = baselink
		self.faction = faction
		self.faction_code = faction_code
		self.faction_letter = faction_letter
		self.flavor = flavor
		self.illustrator = illustrator
		self.influencelimit = influencelimit
		self.minimumdecksize = minimumdecksize
		self.number = number
		self.quantity = quantity
		self.setname = setname
		self.set_code = set_code
		self.side = side
		self.side_code = side_code
		self.uniqueness = uniqueness
		self.limited = limited
		self.cyclenumber = cyclenumber
		self.ancurLink = ancurLink
		self.url = url
		self.imagesrc = imagesrc
