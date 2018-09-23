import re, webbrowser

# regex for URL
regex = re.compile('(((http[s]?|ftp):\/)?\/?([^:\/\s]+)((\/\w+)*\/)([\w\-\.]+[^#?\s]+)(.*)?(#[\w\-]+)?)')

# filepath = input('Path for input file: ')
filepath = '/home/justin/school/ENGR2367/recRepNotes/reccomendationssources.txt'

with open(filepath) as file:
	links = regex.findall("".join(file.readlines()))
	links = [link[0] for link in links]

for url in links:
	webbrowser.open(url)
