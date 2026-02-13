class Author:
	all = []

	def __init__(self, name):
		self.name = name

class Book:
	all = []

	def __init__(self, title):
		self.title = title

class Contract:
	all = []

	def __init__(self, author, book, date, royalties):
		self.author = author
		self.book = book
		self.date = date
		self.royalties = royalties