import csv,tweepy,TwitterAPIKey

consumer_key = "●"
consumer_secret = "●"
access_token = "●"
access_token_secret = "●"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

OUT_FILE="/Users/mocchino/Downloads/沖縄補選/屋良（フルネーム）/屋良朝博7.csv"

api=tweepy.API(auth)

ow=csv.writer(open(OUT_FILE,'w',encoding="utf-8"),delimiter="\t")
keyword="屋良朝博"
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
!osascript -e 'display dialog "終わったよ！"' 
