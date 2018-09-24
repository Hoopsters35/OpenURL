import re, webbrowser, sys

# regex for URL
regex = re.compile('(((http[s]?|ftp):\/)?\/?([^:\/\s]+)((\/\w+)*\/)([\w\-\.]+[^#?\s]+)(.*)?(#[\w\-]+)?)')

if len(sys.argv) == 1:
	filepath = input('Path for input file: ')

	with open(filepath) as file:
		text = "".join(file.readlines())

if len(sys.argv) > 1:
	text = sys.argv[1]

links = regex.findall(text)
links = [link[0] for link in links]
for url in links:
	webbrowser.open(url)
