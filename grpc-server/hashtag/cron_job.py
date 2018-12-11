import time
from sentiment import map_hashtags, reduce_hashtags, take_avg
from pyspark import SparkContext

import redis

r = redis.Redis(host='35.227.41.202', port=6379, db=0)
sc = SparkContext()

textfile = sc.textFile("tweets_dump.txt")
result = textfile.flatMap(map_hashtags)\
                 .reduceByKey(reduce_hashtags)\
                 .map(take_avg)

for hashtag, (sentiment_score, sentiment_magnitude) in result.collect():
    r.set("@score@" + hashtag, sentiment_score)
