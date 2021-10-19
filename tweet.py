import tweepy

#keys and tokens
consumer_key = "nRwoI61wzJRrgZBFPIbubL63E"
consumer_secret="Ons0EzwFEiQD0R5Fv5cfwOkGfDsqUBqHXeZU4WsZBVFQKKQPef"
access_token="1013444741625675777-oy33VopYyQzrNEgHC9DTwdqma0ufic"
access_secret="56Yhh1ssj6DHE4d0FGZYAFo0pILay3WCHEyeLVXiW5SNx"

#authorization and API 
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api = tweepy.API(auth)

#parameters for user and number of tweets
name = input ("Screen name: ")
n= int(input("Number of tweets: "))
print(name+"'s "+ str(n) +" most recent tweets:"+"\n")

#Recover user timeline for n most recent tweets and prints them
cursor= tweepy.Cursor(api.user_timeline,screen_name=name).items(n)
for i in cursor:
     print (i.text+"\n")
     
