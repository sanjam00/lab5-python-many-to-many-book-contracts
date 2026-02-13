class Author:
	all = []

	def __init__(self, name):
		self.name = name

class Book:
	all = []

	def __init__(self, title):
		self.title = title

	def contracts(self):
		return [contracts.contract for contracts in Contract.all if contracts.book == self]

class Contract:
	all = []

	def __init__(self, author, book, date, royalties):
		self.author = author
		self.book = book
		self.date = date
		self.royalties = royalties

	@property
	def author(self):
		return self._author
	
	@author.setter
	def author(self, value):
		if not isinstance (value, Author):
			raise Exception
		self._author = value

	@property
	def book(self):
		return self._book
	
	@book.setter
	def book(self, value):
		if not isinstance(value, Book):
			raise Exception
		self._book = value

	@property
	def date(self):
		return self._date
	
	@date.setter
	def date(self, value):
		if not isinstance (value, str):
			raise Exception
		self._date = value

	@property
	def royalties(self):
		return self._royalties
	
	@royalties.setter
	def royalties(self, value):
		if not isinstance(value, int):
			raise Exception
		self._royalties = value

	def contracts_by_date(self):
		pass
		#this method should return all contracts that have the same date as the date passed into the method