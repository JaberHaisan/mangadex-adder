# mangadex_mass_searcher.py - Helps in adding manga to mangadex by taking manga names
# in one go and then opening tabs for each in mangadex search in your default
# browser. Also keeps a record of each search in a text file.

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
	manga_name = input("%s) Manga Name: " % (len(manga_list)+1))
	if manga_name == 'q':
		break
	if manga_name == '':
		continue
	manga_list.append(manga_name)

# Saves search history in a text file.
with open("Search History.txt", 'a') as f_obj:
	f_obj.write(time.asctime())
	f_obj.write('\n')
	i=1
	for manga in manga_list:
		f_obj.write("%s) %s\n" % (i, manga))
		i+=1
	f_obj.write('\n')
	
'''
Mangadex soft bans your IP for an hour if you open about 20 tabs simultaneously 
so for this reason the script opens 15 tabs in one go and then after 
100 seconds opens the next 15 tabs until tabs are opened for all manga inputed.
'''

completed = 0
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
		completed += 1
	print("\nRemaining manga:", len(manga_list)-completed)
	n += 15
	
	if n < len(manga_list):
		t = 100
		interval = 1
		while t != -interval:
			z = "Time Left for opening next tabs: " + str(t).rjust(3)
			print(z, end="")
			print("\b" * len(z), end="",flush=True)
			time.sleep(interval)
			t -= interval
			
		print()
		
	else:
		print("\nTask Completed.")
