import tweepy

def block(api, usernames,unblock=False):
    try:
        #Busca os usuarios pela lista de usernames
        users = api.get_users(usernames=usernames, user_auth=True)[0]
        #Verifica bloqueio ou desbloqueio
        func_block = api.unblock if unblock else api.block
        for user in users:
            user_id = user.data["id"]
            username = user.data["username"]
            res = func_block(target_user_id = user_id)
            is_blocked = res[0]["blocking"]
            #Confirmação
            if is_blocked:
                print(f"@{username} está bloquedo")
            else:
                print(f"@{username} não está mais bloquedo")		
    except Exception as erro:
        print("Erro:", erro)

if __name__ == "__main__":
    from credentials import *
    from blocklist import usernames,unblock
    #Criando um Cliente para a API 
    api = tweepy.Client(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token= access_token ,
        access_token_secret=access_token_secret)
    #Bloqueia ou desbloqueia usuários da lista
    block(api, usernames, unblock=unblock)
