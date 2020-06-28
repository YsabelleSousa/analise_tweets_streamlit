import streamlit as st
import utils as utils
import datetime as datetime
import config as config


def main():

    #**************************************************
    #**************** SIDEBAR SECTION *****************
    #**************************************************

    search_word = st.sidebar.text_input(
        'Insira a palavra a ser pesquisada:'
    )

    search_language = st.sidebar.selectbox(
        'Selecione o idioma:',
        ['Inglês', 'Português']
    )

    chk_retweet = st.sidebar.checkbox(
        'Incluir Retweets no resultado'
    )

    #date_since = st.sidebar.date_input(
    #    "Escolha a data inicial da captura de tweets:",
    #    datetime.date(2019, 7, 6)
    #)

    # Add a file_uploader to the sidebar:
    add_tweets_slider = st.sidebar.slider(
        'Quantidade de tweets a serem retornados: ',
        1, 500
    )


    # **************************************************
    # **************** MAIN SECTION *****************
    # **************************************************

    #Page's Title and Subtitle
    st.title("Análise de Tweets via Twitter API")
    st.subheader("Por: Ysabelle Sousa")

    api = utils.connect_twitter_api(config.CONSUMER_KEY, config.CONSUMER_SECRET, config.ACCESS_TOKEN,\
                                    config.ACCESS_TOKEN_SECRET)

    if api and search_word != '':

        st.success("Conexão com a API realizada com sucesso!")

        st.write('**Tweets sobre:** ', search_word)


        tweets = utils.searching_tweets(api, search_word, datetime.date(2020, 1, 1), search_language, add_tweets_slider, chk_retweet)

        df_tweets = utils.gathering_tweet_information(tweets)

        st.write('**Média de Seguidores dos Usuários:** ', round(df_tweets['followers_count'].mean(), 2))
        st.write('**Média de Favoritos:** ', round(df_tweets['tweet_favorite_count'].mean(), 2))
        st.write('**Média de Retweets:** ', round(df_tweets['tweet_retweet_count'].mean(), 2))


        #TABELA
        st.subheader('Últimos Tweets:')
        st.table(df_tweets[['tweet', 'tweet_date']].sort_values('tweet_date', ascending=False).head(7))

        #BARCHART
        st.subheader('Localizações dos Usuários:')
        st.bar_chart(df_tweets[df_tweets['location'] != '']['location'].sort_values(ascending=False).unique()[:40])

        #WORDCLOUDS
        st.subheader('Principais palavras:')
        st.pyplot(utils.generating_wordcloud(df_tweets))

        st.subheader('Principais hashtags:')
        st.pyplot(utils.generating_wordcloud_hashtag(df_tweets))

        #HISTOGRAMAS
        st.subheader('Frequência de Seguidores:')
        utils.plot_histogram(df_tweets['followers_count'])

        st.subheader('Frequência de Favoritos:')
        utils.plot_histogram(df_tweets['tweet_favorite_count'])

        st.subheader('Frequência de Retweets:')
        utils.plot_histogram(df_tweets['tweet_retweet_count'])



if __name__ == '__main__':
    main()