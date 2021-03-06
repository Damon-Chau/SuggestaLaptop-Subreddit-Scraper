# -------------------------------------------------------------------------------
# Name:		    SuggestaLaptop Scraper.py
# Purpose:		Goes through recent posts from the subreddit, SuggestaLaptop, and
#               sends a message to me when a keyword is picked up
#
# Author:		Chau.D
#
# Created:		06/07/2015
# ------------------------------------------------------------------------------

# IMPORTANT: outdated since Reddit mandated OAUTH2.0 

import praw
import time

r = praw.Reddit("SuggestaLaptop bot scraper /u/072665995")

r.login("REDDITAPIBRO", "biostarz77ke")

has_key = ("$1000", "CAN", "Canada", "Engineering", "University")
# Used to keep track of what has already been looked at so bot does not do double work
scanned = []

while True:
    subreddit = r.get_subreddit("SuggestaLaptop")
    for submission in subreddit.get_hot(limit=10):
        original_text = submission.selftext
        has_laptop = any(string in original_text for string in has_key)
		# Test if the words in original_text contain any of the keywords
        if submission.id not in scanned and has_key:
            message = "Read this thread" % submission.short_link
            r.send_message("072665995", "Laptop Search Find", message)
            scanned.append(submission.id)

    time.sleep(1800)