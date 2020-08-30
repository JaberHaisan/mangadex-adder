# mangadex_adder.py - Helps in adding manga to mangadex by taking manga names
# in one go and then opening tabs for each in mangadex search in your default
# browser. Also saves search history in a text file.

import webbrowser, time

manga_list = [] 

print("Enter 'q' to finish entering manga names.")
while True:
	manga_name = input("%s)".ljust(4)  % (len(manga_list)+1))
	if manga_name == 'q':
		break
	if manga_name == '':
		continue
	manga_list.append(manga_name)

# Saves search history in a text file.
with open("Search History.txt", 'a') as f_obj:
	f_obj.write(time.asctime())
	f_obj.write('\n')
	for i, manga in enumerate(manga_list):
		f_obj.write("%s) %s\n" % (i + 1, manga))
	f_obj.write('\n')
	
'''
Mangadex soft bans your IP for an hour if you open about 20 tabs simultaneously 
so there is a time delay after every 15 tabs.
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
		url = "https://mangadex.org/search?title=" + v.replace(" ", "%20")
		webbrowser.open(url)
		completed += 1
	print("\nRemaining manga:", len(manga_list) - completed)
	n += 15
	
	if n < len(manga_list):
		t = 10
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
