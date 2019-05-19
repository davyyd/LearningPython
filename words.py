#!/usr/bin/env python3

#!/usr/local/bin/python3
"""Retrieve and print words from a URL.

Usage:
	python3 words.py <URL>

"""
from urllib.request import urlopen
import sys

def fetch_words(url):
	"""Fecth a list of words from a URL.

	Args:
		url: The URL of a UTF-8 text document

	Returns:
		A list of strings containing the words
		from the document.
	"""
	#with urlopen('http://sixty-north.com/c/t.txt') as story:
	with urlopen(url) as story:
		story_words = []
		for line in story:
			line_words = line.decode('utf-8').split()
			for word in line_words:
				story_words.append(word)
	return story_words


def print_items(items):
	"""Print items one per line

	Args:
		An iterable series of printable items
	"""
	for item in items:
		print(item)


def main(url):
	"""Print each word from text document from a URL.

	Args:
		url: The URL of a UTF-8 text document.

	"""
	#url = sys.argv[1] #second argument, from imported sys
	words = fetch_words(url)
	print_items(words)


if __name__ == '__main__':
	main(sys.argv[1])

