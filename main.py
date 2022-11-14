import tweepy
from credentials import *
#Criando um Cliente para a API 
api = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token= access_token ,
    access_token_secret=access_token_secret)
try:
    #Username de cada usuário que será bloqueado
    usernames = ["USERNAME"]
    for username in usernames:
        #Pesquisa o usuário
        user = api.get_user(username=username, user_auth=True)   
        #Pega o ID do usuário
        user_id = user[0].data["id"]
        #Bloqueia o usuário  	
        res = api.block(target_user_id=user_id)       
        is_blocked = res[0]["blocking"]
        #Confirmação
        if is_blocked:
            print(f"@{username} está bloquedo")
        else:
            print(f"@{username} não está bloquedo")		
except Exception as erro:
    print("Erro:", erro)