# mangadex-adder
Helps transfer one's manga list from a different site to mangadex.

I made a simple python script in order to help in transferring one's manga list from a different site to Mangadex.
I made this script in order to reduce the time needed for me to transfer my manga list from Mangarock to Mangadex after Mangarock died and then I thought other people might also be able to benefit from it so I am adding it here (It's a bit late but still might be useful to some people who still haven't moved their list from Mangarock or are planning on moving in from a different site to Mangadex).

In the normal way you have to open mangadex search, enter the name of a manga, add it to your list and then continue in this manner for all of your mangas but this is a bit inefficient for those with a long manga list. But if you use this script you can simply enter the names of the mangas in your list in one go and it will open tabs for each of them which will help you save some time.

This simple python script in the first step takes the names of the manga from the user and then opens tabs in the mangadex search page for all of them 15 at a time. It doesn't open tabs for all of them at the same time because Mangadex soft bans the IP address of anyone who opens about 20 tabs simultaneously for an hour (this is acts as a defense against DDos attacks afaik).

Make sure you are logged in your mangadex account in your default browser before running the script or else you'll have to refresh all the pages after running the script and logging in.


Instructions:
1) Enter the names of the mangas.
2) When you are done enter q to finish.
3) The script will open tabs in mangadex search 15 at a time until all of the manga are 
added. The time interval per 15 tabs is 100s.
