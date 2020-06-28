import tweepy as tw
import pandas as pd
import streamlit as st
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

def connect_twitter_api(consumer_key,consumer_secret,access_token,access_token_secret):

    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)

    return api


def searching_tweets(api, search_word, date_since, tweet_language, returning_tweets_number, include_retweets=False):

    tweets = tw.Cursor(api.search,
                       q=search_word + '-filter:retweets' if include_retweets is False else search_word,
                       lang='en' if tweet_language == 'Inglês' else 'pt-br',
                       since=date_since).items(returning_tweets_number)
    return tweets

def gathering_tweet_information(tweets):

    if tweets:

        arr_tweets = [[tweet.user.screen_name, tweet.user.location, tweet.user.followers_count, tweet.text,tweet.created_at, tweet.lang, \
                       tweet.favorite_count, tweet.retweet_count, tweet.entities['hashtags']] for tweet in tweets]

        df_tweet = pd.DataFrame(data=arr_tweets,
                                columns=['user', 'location', 'followers_count', 'tweet', 'tweet_date','tweet_language',
                                         'tweet_favorite_count', 'tweet_retweet_count', 'tweet_hashtags'])
        return df_tweet
    else:
        st.warning('Ops. Sua busca não trouxe nenhum resultado. Tente novamente.')


def generating_wordcloud(tweets, max_words=100, background_color='white'):

    #Joining all tweets into a one big string
    text = " ".join(review for review in tweets.tweet)


    #Setting stopwords and adding some portuguese stopwords
    stopwords = set(STOPWORDS)
    stopwords.update(["de", "da", "com", "um", "uma", "sem", "of", "RT", 'and', 'not'])

    #Creating the WordCloud
    wc = WordCloud(width=1800, height=1000, stopwords=stopwords, max_words=max_words, background_color=background_color)

    plt_wc = wc.generate(text)
    plt.figure(figsize=(20, 10))
    plt.imshow(plt_wc, interpolation='bilinear')
    plt.axis("off")


def generating_wordcloud_hashtag(tweets, max_words=100, background_color='white'):

    arr_hash = []
    for x in tweets['tweet_hashtags']:
        for y in x:
            arr_hash.append(y['text'])

    #Joining all tweets into a one big string
    text = " ".join(review for review in arr_hash)

    if text != '':

        #Setting stopwords and adding some portuguese stopwords
        stopwords = list(STOPWORDS) + ["de", "da", "com", "um", "uma", "sem", "of", "RT", "and", "not", "que", "https"]

        #Creating the WordCloud
        wc = WordCloud(width=1800, height=1000, stopwords=stopwords, max_words=max_words, background_color=background_color)

        plt_wc = wc.generate(text)
        plt.figure(figsize=(20, 10))
        plt.imshow(plt_wc, interpolation='bilinear')
        plt.axis("off")

    else:
        st.warning("Não há hashtags")


def plot_histogram(tweets):

    plt.figure(figsize=(20, 10))

    plt.hist(tweets, density=True)

    plt.xlabel('Value')
    plt.ylabel('Frequency')

    st.pyplot()
