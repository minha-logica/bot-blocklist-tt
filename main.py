import tweepy
from decouple import config

def get_client():    
    api = tweepy.Client(
        consumer_key = config("CONSUMER_KEY"),
        consumer_secret = config("CONSUMER_SECRET"),
        access_token = config("ACCESS_TOKEN"),
        access_token_secret = config("ACCESS_TOKEN_SECRET")
    )
    return api
    
def block_list(api, usernames,unblock=False):
    try:
        #Busca os usuários pela lista de usernames
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
    from blocklist import usernames, unblock
    #Obtem a API
    api = get_client()    
    #Bloqueia ou desbloqueia usuários da lista
    block_list(api, usernames, unblock=unblock)

