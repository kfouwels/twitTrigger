from time import sleep
import tweepy
import json

consumer_key2=""
consumer_secret2=""

access_token2=""
access_token_secret2=""

auth = tweepy.OAuthHandler(consumer_key2, consumer_secret2)
auth.secure = True
auth.set_access_token(access_token2, access_token_secret2)

myApi = tweepy.API(auth)

print "I am: ", myApi.me().name

class Listener(tweepy.StreamListener):
    def on_data(self, data):
        data = json.loads(data)
        msg = (data['text']).encode('UTF-8')
        name = (data['user']['screen_name']).encode('UTF-8')
        print name, ": ", msg, '\n\n-----------\n\n'
        fobj = open('dump.txt', 'w')
        fobj.write(msg)
        fobj.close()
        myApi.update_status("@" + name + " Game ready, play it here: asdasd")
        return True

    def on_error(self, status):
        print status

l = Listener()

stream = tweepy.Stream(auth, l)
#stream.filter(track=['Basketball'])
stream.filter(track=['10minutedistraction'])