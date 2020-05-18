# mangadex_adder.py - Helps in adding manga to mangadex by taking manga names
# in one go and then opening tabs for each in mangadex search 15 at a time 
# in your default browser.

import webbrowser, re, time


def string_processor(string, sub_char='_'):
	'''Processes string to make it suitable for adding to link.'''
	space_regex = re.compile(r' ')
	
	if space_regex.search(string) != None:
		return space_regex.sub(sub_char, string)
	else:
		return string
		
manga_list = [] 

print("Enter 'q' to finish entering manga names.")
while True:
	manga_name = input("Manga Name: ")
	if manga_name == 'q':
		break
	if manga_name == '':
		continue
	manga_list.append(manga_name)

print("\nTotal: ", len(manga_list))


'''
Mangadex soft bans your IP for an hour if you open about 20 tabs simultaneously 
so for this reason the script opens 15 tabs in one go and then after 
100 seconds opens the next 15 tabs until tabs are opened for all manga inputed.
'''

n = 0
while n < len(manga_list):
	print("\nOpening tabs for the following manga:")
	for i in range(n, n + 15):
		if i == len(manga_list):
			break
		v = manga_list[i]
		print(v)
		url = "https://mangadex.org/search?title=" + string_processor(v,'%20')
		webbrowser.open(url)
	
	n += 15
	
	if n < len(manga_list):
		print("\nOpening next tabs after:")
		
		z = 100
		interval = 5
		while z != -interval:
			print(z)
			time.sleep(interval)
			z -= interval
		print()
	
	else:
		print("\nTask Completed.")
