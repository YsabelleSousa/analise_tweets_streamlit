# Análise de Tweets com Streamlit

A aplicação utiliza o framework [Streamlit](https://www.streamlit.io) e permite realizar uma análise básica de tweets a partir de uma palavra buscada.

Para conexão com o Twitter foi utilizada a biblioteca [Tweepy](https://github.com/tweepy/tweepy) , que já possui
funções para análise do JSON retornado pela API do Twitter.    

### Gerando Keys de Autenticação no Twitter
Para utilizar a aplicação, é necessário gerar keys de autenticação no Twitter, para isso:

1. Crie uma conta de [desenvolvedor no Twitter](https://developer.twitter.com/en)
2. Clique em "Apps" no menu do usuário
3. Clique no botão "Create an App" e crie uma nova aplicação.
4. Vá na sessão "Keys and tokens Permissions"
5. Crie no botão "Create" para criar um "Access token" e "access token secret"
6. Após obter todos os tokens necessários, abra o arquivo config.py no diretório e preencha as variáveis 
com suas respectivas chaves de acesso do seu app no Twitter.


### Rodando a aplicação

Para rodar a aplicação basta rodar o seguinte comando no seu terminal:

`streamlit run main.py`   

Então, ela abrirá automaticamente em seu navegador.    