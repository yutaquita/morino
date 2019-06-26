import csv,tweepy,TwitterAPIKey

#
#Developer informations
#
consumer_key = "●"
consumer_secret = "●"
access_token = "●"
access_token_secret = "●"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#
#need to change
#
OUT_FILE="/full-pass/file-name.csv"

api=tweepy.API(auth)

#
# to collect tweet for 100*100
#
ow=csv.writer(open(OUT_FILE,'w',encoding="utf-8"),delimiter="\t")

#
#change keywords whatever you want to
#
keyword="keyword"
search_count=100
repeat_count=100

search_result=[]
last_id=0
for i in range(repeat_count):
    tweets=api.search(q=keyword,count=search_count,max_id=str(last_id-1),wait_on_rate_limit=True,tweet_mode="extended")
    search_result.append(tweets)
    if len(tweets)==0: break
    last_id=tweets[-1].id
    
for tw in search_result:
    ow.writerow(tw)
!osascript -e 'display dialog "Done!!"' 
