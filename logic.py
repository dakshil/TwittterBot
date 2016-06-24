"""
Copyright 2016 Dakshil Shah 
This file is part of the TwitterBot library.
The TwitterBot library is available under the terms of the Apache License 2.0.
The TwitterBot library is distributed WITHOUT ANY WARRANTY or CLAIMS, use at your own discretion.
"""

from twitter import Twitter, OAuth, TwitterHTTPError
from time import sleep

#All the print statements are merely for debugging and seeing the code in action and do not affect the basic function itself.

try:
# put your twitter tokens, keys, secrets, and twitter handle in the following variables
    OAUTH_TOKEN = "enter within these quotes, do not remove these quotation marks"
    OAUTH_SECRET = "enter within these quotes, do not remove these quotation marks"
    CONSUMER_KEY = "enter within these quotes, do not remove these quotation marks"
    CONSUMER_SECRET = "enter within these quotes, do not remove these quotation marks"
    TWITTER_HANDLE = "Your twitter accounts handle without @, do not remove these quotation marks"

    t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,
                CONSUMER_KEY, CONSUMER_SECRET))

    def theTweet(sent):
        #This is the part which actually posts the tweet
    	if len(sent)<=140:
            #Twitter allows only 140 character tweets
    		print("tweetable")
    		t.statuses.update(status=sent)
    	else:
    		print("140 characters crossed")
    def theBrain():
        #The area where we can do whatever we want
        #Fetch n number of tweets where n is given by count, having the keyword given in q
    	statement =t.search.tweets(q="tea", count=1)
        #tweets are fetched in JSON format with a lot of related data
    	tweets = statement['statuses']
    	#process each tweet individually
        for statement in tweets:
            #extract the actual tweet from all the other data like location data etc which is not needed by us
            #and convert to string. We encode using utf-8 as the format is actually ascii and will cause errors
            #for certain characters.
    		text=str(statement['text'].encode("utf-8"))
    		print(text)
            #We replace our keyword(replace(old,new)) and store in a new variable as python strings are immutable.
    		textN=text.replace('tea','coffee')
    		print(textN)
            #We now create the text we want to tweet. As we want to to tweet back to the original tweeter, we mention
            #them in the new tweet(alternately we could reply back to the tweet but lets not do that now).
            #We first extract the twitter handle for that particular user and then create the tweet.
    		handle=str(statement['user']['screen_name'])
    		sent='@' + handle + ' ' + textN
    		print sent
    		theTweet(sent)
    			
    def main():
    	while True:
            #This loop is merely to keep the code running. you may eliminate the above line and the sleep if you want to run the code everytime or just test.
    		theBrain()
            #To prevent abuse of the twitter API and usage limit, calling it only once an hour.
    		sleep(3600)

    	


    if __name__ == "__main__":
    	main()

except Exception as err:
    errmsg = 'There has been an error.'
    print(errmsg)#replace with err to see actual error
    #I have used a dummy error message here as when we later write a hosted version, if an error occurs, the Auth details would get exposed
    #on application crash and we don't want that happening so we simply mask it.
