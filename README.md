# mangadex-mass-searcher
This script helps reduce the time needed to transfer a large number of manga (from your manga lists in a different website for example) to Mangadex.

In the normal way you have to open mangadex search, enter the name of a manga, add it to your list and then continue in this manner for all of your mangas but this is a bit inefficient and extremely boring. By using this script you can simply enter the names of the mangas in your list in one go and it will open tabs for each of them in mangadex search which will help you save some time.

This python script in the first step takes the names of the manga from the user and then opens tabs in the mangadex search page for all of them 15 at a time. It doesn't open tabs for all of them at the same time because Mangadex soft bans the IP address of anyone who opens about 20 tabs simultaneously for an hour (this acts as a defense against DDos attacks). This script also saves your search history in a text file.

Make sure you are logged in your mangadex account in your default browser before running the script or else you'll have to refresh all the pages after running the script and logging in for adding manga to your lists in your mangadex account.

Instructions:
1) Enter the names of the mangas.
2) When you are done enter q to finish.
3) The script will open tabs in mangadex search 15 at a time until all of the manga are added. The time interval per iteration is 100s.
