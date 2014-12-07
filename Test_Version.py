#####Made by TECOED####
####WHAT TYPE OF elf ARE YOU?###
###SEND A TWEET - HASH THE LETTERS, RETURNS FROM A LIST, NAME AND PICTURE, RETWEETED BACK###
####TWITTER SECTION###

import sys, subprocess, urllib, time, tweepy

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key= 'XXXXXXXXXXXXXXXXXXXXXXXX'
consumer_secret= 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located 
# under "Your access token")
access_token= 'XXXXXXXXXXXXXXXXXXXXXXXXXXX'
access_token_secret= 'XXXXXXXXXXXXXXXXXXXXXXXX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

####THE ELF PART####

Letters = {"_": 0, "@": 0, "1": 0, "a": 1, "b": 2, "c": 30, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16,
           "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26, " ": 0}
         
Names = {0: "Grimoid", 1: "Boris", 2: "Doris", 3: "Loris", 4: "Wrangler", 5: "Sooty", 6: "Mandrake", 7: "Jingles", 8: "Bongel", 9: "Raven", 10: "Floppsy", 11: "Badoo",
         12: "Banger", 13: "Tinsel", 14: "Snowdrop", 15: "Zanta", 16: "Jeffery", 17: "Scoot", 18: "Tinker", 19: "Sparkle", 20: "Bob", 21: "Snazzy", 22: "Bopsee",
         23: "Twinkle", 24: "Santo", 25: "Fanta", 26: "Moonie", 27: "Lunar", 28: "Snazzale Dazzle", 29: "Jazz", 30: "Dixie"}

global name
global Elf_name
global final_first_name

def What_is_your_elf_name():
    global name
    global Elf_name
    global final_first_name
    what_to_play = []
    ###test
    print Letters
    ###test
    for key, value in Letters.items():
        print (key, value)

    print""        
    #name = raw_input("Please enter your name ").lower()
    
    ###checks to see if the letter is in the dictionary and returns the value###
    
    for letter in name:
        name_code = Letters [letter]
        what_to_play.append(name_code)
    print "The value of the notes", what_to_play

    ###adds together the appended values to return an overall total###
    
    total_name_value = 0
    for item in what_to_play:
        total_name_value = total_name_value + item

    print "The total value of the letters is ", total_name_value

    ####divides the total by the length###
    
    print "what the total is divided by"
    print len(what_to_play)
    final_first_name = total_name_value % len(what_to_play)
    print "The value is ", final_first_name

    ####returns the value of the Elf name###
    
    Elf_name = Names[final_first_name]

    print Elf_name

    #print "Your Elf name is %s" %(Elf_name)
    print ""

class Which_Xmas_Elf_Are_YouStreamListener(tweepy.StreamListener):
    def on_status(self, tweet):
        global final_first_name
        global name
        global Elf_name

        tweet_to_check = tweet.text

        does_the_tweet_contain_key_word = tweet_to_check.find("@PiTests #Elfme")
        print does_the_tweet_contain_key_word
        #time.sleep(50)
                
        if does_the_tweet_contain_key_word >= 0:
            user_name = tweet.text ###to add lower case
            name = tweet.user.screen_name.lower()
            What_is_your_elf_name() 
            print "Your Elf name is %s" %(Elf_name)
            photo_path = '/home/pi/elfpics/%i.jpg' %(final_first_name)

            user = tweet.user.screen_name
            print user ###prints the users name
            
            final_message = "@%s Your Elfname is %s, more at www.tecoed.co.uk/xmas-elf.html" %(user, Elf_name) 
            

            print final_message
            
           ###send the name and the photo
            
            api.update_with_media(photo_path, final_message)
            print ""
            print "Tweet Posted"
            time.sleep(5)
            
        else:
            print tweet.user.screen_name
            print tweet.text
            print ""
            time.sleep(5)

stream = tweepy.Stream(auth, Which_Xmas_Elf_Are_YouStreamListener())            
            
while True:
    stream.userstream()

 
