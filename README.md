![Daily Verse Journal Image](/daily-verse-journal.png)

# Terminal Daily Bible Verse
Created for Mac.

This application scrapes the daily verse from [Verse of the Day](https://www.verseoftheday.com/) and displays it in the command line. Then the user is prompted to "Ponder, Picture, and Personalize" the verse to let it soak in and *allow the Holy Spirit to speak to them.* Then the user can journal on their experience, whether a revelation, prayer, thoughts, etc. 

Each time the user journals, it logs the verse, verse reference, journal notes, and date to a `.csv` file that can be viewed with Microsoft Excel for future reference. I use Webhook to connect to the users IFTTT account can send an email to the user each day.

## **How To**
 1. Clone or download this repo.
 2. `cd` to the folder and install in order the following dependencies.
```
$ sudo easy_install pip
$ sudo pip install BeautifulSoup4
$ sudo pip install requests
```
 3. Run the program in the package folder 
`$ python main.py`

## **I want to send each journal to my inbox**
[Here](https://anthscomputercave.com/tutorials/ifttt/using_ifttt_web_request_email.html) is a great tutorial on how to do it, and below is my implementation with Gmail.
 1. Log into IFTTT.com
 2. Click My Applets and create a New Applet
 3. For This, search for Webhooks
 4. Choose Receive a Web Request Trigger
 5. Choose Gmail and click send an email
 6. Name the Event Name `verse_of_day` (this is the `NAME_OF_EVENT`)
 7. Enter your email address so it can send to you.
 8. Enter whatever email subject you want. I prefer `Verse of the Day - {{OccurredAt}}` <- OccuredAt will print the date.
 9. Paste this code into the body (or personalize this HTML to fit your needs).
 ```
 <div>
<div style="font-family: ProximaNova, 'Montserrat', OpenSans; color: #b2b2b3; font-size: 24px; font-weight: 600;">Here's the Verse of the Day:</div>
<br>
<div id="verse" style="font-size: 30px; font-weight: bold; font-family: ProximaNova, 'Montserrat', OpenSans; color: #404041; line-height: 1.1;">{{Value1}}</div>
<div style="font-style: italic; font-family: ProximaNova, 'Montserrat', OpenSans; color: #b2b2b3; font-size: 18px;">{{Value2}}</div>
<br>
<br>
<div style="font-family: ProximaNova, 'Montserrat', OpenSans; color: #b2b2b3; font-size: 24px; font-weight: 600;">Here is my journaling for the day:</div>
<br>
<div id="journaling" style="font-family: ProximaNova, 'Montserrat', OpenSans; color: #404041; white-space: pre-wrap; font-size: 18px;">{{Value3}}</div>
</div>
 ``` 
 11. Save the applet.
 11. Open `main.py` file.
 12. Uncomment the following code
 ```
 def  notification(my_verse, my_verse_ref, my_journaling):
	report = {}
	report["value1"] = my_verse
	report["value2"] = my_verse_ref
	report["value3"] = my_journaling
	requests.post("https://maker.ifttt.com/trigger/NAME_OF_EVENT/with/key/ID_OF_THE_KEY", data=report)
	
notification(verse, verse_ref, journaling)
```
14. Insert your `(NAME_OF_EVENT)` and `(ID_OF_THE_KEY)` in `requests.post` method.
15. Save `main.py` and run `$ python main.py`

## **How to run every time the terminal is opened**
This is great for the person who wants to make God the center of their world. He does not have to be separated from our jobs, because He is intertwined throughout it all.
1. `$ cd ~`
2. `$ sudo nano ~/.bash_profile`
3. Add these lines of code to the end of the file. Fill in path to daily-verse-journal.
```
$ alias VERSE="cd [path to daily-verse-journal]; python main.py; cd ~/"
VERSE
```
4. Save the file and then run `$ source ~/.bash_profile`.
5. Close terminal and test program. It should work every time you open the terminal. 
6. Any time you are in the terminal and want to run the program, you can type `VERSE` and press enter.

## **Love God; Love Others.**
