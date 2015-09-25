# -*- coding: utf-8 -*-

# Importing necessary modules
import sys, os, re, pygame
from urllib.request import urlopen


# Private method to convert texts from ascii to python readable format.
def _charchange(text):
	regex_result = re.findall('([^\w\s\-\;\'\.\,\!\"\'()\[\]\?\\\/\:]+\d+\;)', text)

	# Loops into regex result and replaces character encoding to parsable characters.
	for x in regex_result: text = text.replace(x, "")
	text = text.replace("b'", "").replace("<b>", "==").replace("</b>", "").replace("\\xe2\\x80\\x9d", '"').replace("\\xe2\\x80\\x9c", '"').replace("&#8211;", '-').replace("\\xe2\\x80\\x99", "'").replace("\\xe2\\x80\\x98", '').replace("&#1488;", u"\u2135").replace("/", "")

	return text[:-1]

# Bible class
class Bible():
	def __init__(self, book="Genesis", chapter=1, verse_begin="", verse_end=""):
		""" Initializes the Bible class"""
		self.book = book
		book_ = book.replace(" ", "%20")
		self.chapter = chapter
		self.verse_begin = verse_begin
		self.verse_end = verse_end
		self.size = width, height = 800, 600
		self.content = []

		# Switch between the two modes of (extra) verses
		if len(str(verse_end)) == 0:
			homepage = "http://labs.bible.org/api/?passage={}%20{}:{}".format (book_, chapter, verse_begin)
		else: homepage = "http://labs.bible.org/api/?passage={}%20{}:{}-{}".format(book_, chapter, verse_begin, verse_end)

		# Open parsed online data
		try:
			page_content = str(urlopen(homepage).read())
		except:
			sys.exit("Internet connection could not be established")

		# If heading is found, add it else put a space.
		try:
			header = re.match(r'[\sa-zA-Z]+', _charchange(page_content).split(":")[0]).group(0)
		except:
			header = ""

		# Get verses without the heading 
		page_content = _charchange(page_content).split(":", 1)[1]
		page_content = "{} {}:{}".format(book.title(), chapter, page_content)

		# Starting loop variables
		x = 0
		texter = ""

		# Check every content until there are 15 spaces and add an "==" 
		for x in page_content:
			texter += x
			space = texter.count(" ") 
			if space > 1 and space % 15 == 0:
				texter += x + "=="
				space = 0

		# Assign class variables to final result
		self.content = texter.split("==")
		self.page_content = page_content 
		self.header = header
		self.texter = texter

	# Class method to print out bible verse to console
	def read(self):
		""" Prints out bible verses to console"""
		results = (self.page_content).replace("==", "\n")

		if len(self.header) > 1:
			print("%s %s\n%s=%s\n" % (self.header.upper(), self.chapter, len(self.header) * "=", len(str(self.chapter))*"="))
		print (results)
		return ""

	# Private method to handle text display
	def _settings(self, screen, text, colour, font="verdana", size=16, position=(30,30)):
		""" Handles text formatting"""
		myfont = pygame.font.SysFont(font, size)
		# render text
		label = myfont.render(text, 1, colour)
		return screen.blit(label, position)

	# Class method to display bible text graphically
	def display(self, colour = (0, 0, 0), background = (255, 250, 250), size=28):
		""" Displays a bible verse"""

		# Initialises pygame and sets screen dimension
		pygame.init()
		size = width, height = 800, 600
		screen = pygame.display.set_mode(size, 32)

		# Game loop
		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT: running = False
				elif event.type == pygame.KEYDOWN: 
					if event.key == pygame.K_ESCAPE: running = False 
					elif event.key == pygame.K_q: running = False
					elif event.key == pygame.K_SPACE: running = False

			screen.fill(background)
			self._settings(screen, "GUI Bible For Python", colour, font="Arialbold", size=28, position = (30, 32) )

			height = 110
			if len(self.header) > 1:
				self._settings(screen, ("%s %s" % (self.header.upper(), self.chapter )), colour, font="verdanabold", size=25, position = (60, 72) )
			else: height = 80
			x = 0
			while x < len(self.content):
				self._settings(screen, self.content[x], colour, size=15, position = (30, 32*x+height))
				x +=1
			
			pygame.display.flip()
		pygame.quit()
		return ""