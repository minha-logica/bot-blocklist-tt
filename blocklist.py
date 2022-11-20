import tweepy
import time
from decouple import config
import re

class ClientAPI:
    def __init__(self):
        self.client = tweepy.Client(
                          consumer_key = config("CONSUMER_KEY"),
                          consumer_secret = config("CONSUMER_SECRET"),
                          access_token = config("ACCESS_TOKEN"),
                          access_token_secret = config("ACCESS_TOKEN_SECRET")
                      )  
    def get_me(self):
        me, includes, errors, meta = self.client.get_me(user_fields=[ "description","public_metrics"])
        return me
    def get_client(self):
        return self.client

                                                  	                      
class BlockList(ClientAPI):
    def __init__(self, filters: list = None, file_path: str = "blocklist.txt"):
        super().__init__()
        self.__me = self.get_me()
        self.__client = self.get_client()
        self.__client_id = self.__me["id"]
        self.__followers_count = self.__me["public_metrics"]["followers_count"]                                
        self.__pagination_tokens = []
        self.__page_counter = 0   
        self.filters = filters
        self.file_path = file_path
        self.usernames = []
        self.user_auth = True             
        self.RATE_LIMIT_GET_USERS=50
        self.RATE_LIMIT_GET_USERS_FOLLOWERS=1000
        self.RATE_LIMIT_TIME = 15*60 #15 minutos
        self.RATE_LIMIT_MESSAGE = "Limite da API atingido. Isso pode levar até 15 minutos. Aguarde..."
        
    def block(self, usernames=None, unblock=False, prev=0, count=0):
        if usernames == None:
            usernames = self.read()
            if len(usernames) == 0:
                return False
        rate_limit = self.RATE_LIMIT_GET_USERS
        pages, last = divmod(len(usernames),rate_limit)        
        prev = prev
        next = 0
        page_counter = count        
        block_function = self.__client.unblock if unblock else self.__client.block
        blocking_number = prev + 1
        
        while page_counter <= pages:            
            next = prev + rate_limit
            if count == pages:
                next = prev + last
            try:                                                       
                users = self.__client.get_users(
            	            usernames=usernames[prev:next], 
            	            user_auth=True)[0]                       
                for user in users:                                   
                    user_id = user.data["id"]
                    username = user.data["username"]
                    #Bloqueia usuários da lista
                    res = block_function(target_user_id = user_id)
                    is_blocked = res[0]["blocking"]                    
                    if is_blocked:
                        print(f"@{username} está bloquedo")                       
                    else:
                        print(f"@{username} não está mais bloquedo")		                                                             
                    print(blocking_number)
                    blocking_number += 1
                prev = next 
                page_counter += 1
                self.__page_counter = page_counter
                print("Quantidade de usuários (des)bloqueados:", prev)    
                if blocking_number == len(usernames):
                    break      
            except tweepy.errors.TooManyRequests:
                print(self.RATE_LIMIT_MESSAGE)
                time.sleep(self.RATE_LIMIT_TIME)
                self.block(usernames, unblock=unblock, prev=prev, count=self.__page_counter)                                                                 	                          
        return True 
           
    def check_bio(self, description):
        checked = True
        description = description
        for key in self.filters:
            if key == " ":
                continue
            expr = "\\b{}\\b".format(key)
            if re.search(expr, description, re.IGNORECASE):            
                checked = False
                break
        return checked
        
    def read(self):
        with open(self.file_path, "r", encoding="utf-8") as f:
            for username in f:
                self.usernames.append(username.replace("\n",""))
            f.close()
        return self.usernames
        
    def update(self, usernames): 
        f = open(self.file_path, "r+")
        blocklist = f.readlines()
        blocklist = [i.replace("\n", "") for i in blocklist]
        for username in usernames:
            if not username in blocklist:
                f.update(username+"\n")
        f.close()
            
    def search_in_followers(self, next=None):
        pages = tweepy.Paginator(
    	             self.__client.get_users_followers, 
    	             id=self.__client_id, 
    	             user_auth=self.user_auth, 
    	             max_results=self.RATE_LIMIT_GET_USERS_FOLLOWERS, 
    	             user_fields=["description"], 
    	             pagination_token=next, 
    	             limit=self.__followers_count)
        try:
            for followers in pages:
                next_token = None
                if "next_token" in followers.meta:
                    next_token = followers.meta["next_token"]
                self.__pagination_tokens.append(next_token)
                usernames = []
                for user in followers.data:
                    name = user["name"]
                    username = user["username"]
                    description = user["description"]                   			
                    print(f"Nome: {name}")
                    print(f"Username: @{username}")                          
                    print(f"Bio: {description}", end =" ")

                    if self.check_bio(description):                        
                        print("(\u001b[32;1mOK\u001b[0m)")                        
                    else:
                        usernames.append(username)
                        print("(\u001b[31;1mFiltered\u001b[0m)")
                    print("-"*50)	                  
                self.usernames.extend(usernames)          			
        except tweepy.errors.TooManyRequests:
            print(self.RATE_LIMIT_MESSAGE)
            time.sleep(self.RATE_LIMIT_TIME)        
            self.search_in_followers(self.__pagination_tokens[-1])        		
       
        return self.usernames           		
 
if __name__ == "__main__":    

    blocklist = BlockList(file_path="usernames.txt")
    usernames = blocklist.read()
    blocklist.block(usernames)
    """
    blocklist = BlockList(
    	               filters=[
    	                   "chatonildo",
    	               ],
    	               file_path="blocklist.txt"
    	           )
    
    result = blocklist.search_in_followers()             
    if len(result)>0:
        blocklist.update(result)        
    usernames = blocklist.read()            
    blocklist.block(usernames, unblock=True)
    """


#:sparkles: feat: Added BlockList and ClientAPI classes.  In this version there is also a method to search and filter followers by profile description.



           