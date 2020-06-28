# Análise de Tweets com Streamlit

O app utiliza o framework Streamlit e permite realizar uma análise básica de tweets a partir de uma palavra buscada.


### Gerando Keys de Autenticação no Twitter
Para utilizar a aplicação, é necessário gerar keys de autenticação no Twitter, para isso:

1. Crie uma conta de desenvolvedor no Twitter: https://developer.twitter.com/en
2. Clique em "Apps" no menu do usuário
3. Clique no botão "Create an App" e crie uma nova aplicação.
4. Vá na sessão "Keys and tokens Permissions"
5. Crie no botão "Create" para criar um "Access token" e "access token secret"
6. Após obter todos os tokens necessários, abra o arquivo config.py no diretório e preencha as variáveis 
com suas respectivas chaves de acesso do seu app no Twitter.


### Rodando a aplicação

Para rodar a aplicação basta rodar no seu terminal:

`streamlit run main.py`   

Então ele abrirá automaticamente em seu navegador.    