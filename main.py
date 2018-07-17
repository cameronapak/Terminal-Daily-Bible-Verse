# -*- coding: utf-8 -*-
# I followed a tutorial:
# https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe

# June 2018. My goal with this is to get the verse of the day.

# import libraries
import urllib2
import time
import requests, json
from bs4 import BeautifulSoup
import csv
from datetime import date
import sys

# specify the url
quote_page = 'https://www.verseoftheday.com/'
data = []

# query the website and return the html to the variable 'page'
page = urllib2.urlopen(quote_page)

# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')

# get the verse
name_box = soup.find('div', attrs={'class': 'bilingual-left'})
verse = name_box.text.strip() # strip() is used to remove starting and trailing

# remove the pesky unicode character -
x = verse.find(u'—')

# separate ref from verse
verse_ref = verse[x+1:]
verse = verse[:x]

# display verse
print "\n" + verse + "\n"
print "- " + verse_ref

# allow the user to think on the verse
time.sleep(3)
print "\nPonder. Picture. Personalize."
time.sleep(10)

# get user prayer and thoughts
thoughts = raw_input('\nJournal? [y/n] ')

if thoughts == "y":
    print "\nType away! Press ctrl+d (Mac) when complete."
    thoughts = sys.stdin.readlines()

    # test and see if the data was completed
    journaling = ""
    for item in thoughts:
        # manipulate user input data
        journaling += item

    # open a csv file with append, so old data will not be erased
    with open('journal.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([verse, verse_ref, journaling, date.today()])
        print "\n\nSaved. Now love God and love others!\n"

    # use IFTTT webhook to upload verse, verse_ref, and journaling
    # def notification(my_verse, my_verse_ref, my_journaling):
    #     report = {}
    #     report["value1"] = my_verse
    #     report["value2"] = my_verse_ref
    #     report["value3"] = my_journaling
    #     requests.post("https://maker.ifttt.com/trigger/verse_of_day/with/key/dd4_iTJuEQFOniJgqngjA9", data=report)

    # notification(verse, verse_ref, journaling)
        