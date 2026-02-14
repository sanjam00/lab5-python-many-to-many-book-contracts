class Author:
	all = []

	def __init__(self, name):
		self.name = name

	def contracts(self):
		# returns a list of its contracts
		# structure: [EXPRESSION for ITEM in COLLECTION if CONDITION]
		# plain english: “Give me every contract in Contract.all where the contract’s author is me.”
		# we are looping through instaces of Contract, not the class itself. 
		# And it's singular because 'contract' represents one item at a time (technically just a variable name; could be 'contracts' but that's confusing bc it sounds like a list)
		return [contract for contract in Contract.all if contract.author == self]
	
	def books(self):
		# returns a list of related books
		# structure: [EXPRESSION for ITEM in COLLECTION]
		# plain english: “For each of my contracts, give me the book attached to it.”
		# we loop through contracts() because that's already filtered!
		# contract.book accesses that object's attribute
		return [contract.book for contract in self.contracts()]

	def sign_contract(self, book, date, royalties):
		return Contract(self, book, date, royalties)

	def total_royalties(self):
		# loop through to find all Contract.royalties, add the sum of all?
		royals = [contract.royalties for contract in self.contracts()]
		return sum(royals)

class Book:
	all = []

	def __init__(self, title):
		self.title = title

	def contracts(self):
		#returns a list of its contracts
		return [contract for contract in Contract.all if contract.book == self]
	
	def authors(self):
		#returns a list of related authors
		return [contract.author for contract in self.contracts()]

class Contract:
	all = []

	def __init__(self, author, book, date, royalties):
		self.author = author
		self.book = book
		self.date = date
		self.royalties = royalties
		Contract.all.append(self)

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

	@classmethod
	def contracts_by_date(cls, date):
		# This method should return all contracts that have the same date as the date passed into the method
		return [contract for contract in cls.all if contract.date == date]