# SoundCloud Track Scrapper
This tool allows scrapes the followers of a SoundCloud user and gets their track count.  
If a follower has tracks, their track url and the first 5 tracks will be printed to the console and added to a database to avoid being checked again in the future.

## Usage

Install requirements first

The script will prompt you to choose between entering a SoundCloud URL to check followers or viewing all entries in the database.  
If you choose to view all entries, the script will display all checked followers stored in the database.  

Enter a SoundCloud URL in the format:  

https://soundcloud.com/username/

For example:  
https://soundcloud.com/billieeilish  
or  
https://soundcloud.com/billieeilish/sets  
the text after the username gets ignored so you dont need to copy url from the mainpage

It might seem like the tool does nothing when entering the user url but it is scrapping the followers. The higher the count the longer it will take.
