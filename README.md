# BotBlockListTT
## Bot em Python Para Bloquear uma lista de usuários no Twitter

Você fornece uma lista com nomes de usuários e o bot bloqueia todos da lista.

## Como usar?
Instale a biblioteca Tweepy
```
$ pip install tweepy
```
#### Etapas:

   **1° passo:** clonar ou baixar repositório
```
$ git clone https://github.com/minha-logica/bot-blocklist-tt
```
   **2° passo:** criar uma conta para desenvolvedores no site do Twitter(
[Twitter for Developers](https://developer.twitter.com/en/apply-for-access)). Nessa conta, crie um novo [App](http://dev.twitter.com/apps) e
certifique-se de gerar suas credenciais (chaves de acesso e tokens de acesso ). Também é preciso dar permissão de leitura e escrita para seu App.
  
 
   **3° passo:** nos arquivos baixados, adicione suas credenciais no arquivo `credentials.py`
```python
consumer_key = "CHAVE DE ACESSO" 
consumer_secret = "CHAVE SECRETA DE ACESSO" 
access_token = "TOKEN DE ACESSO"
access_token_secret = "TOKEN SECRETO DE ACESSO"

```
   **4° passo:**  no arquivo `blocklist.py` adicione os nomes de usuários que deseja bloquear na lista *usernames*.
Exemplo:
```python
usernames = [
    "fulano",
    "siclano",
    "beltrano"
]
```

Finalmente, basta executar o arquivo ```main.py```.
```
$ python main.py
```

Para desfazer os bloqueios substitua `False` por `True` na variável *unblock* no arquivo `blocklist.py`
```python
unblock = True
```

Seja feliz! 🙂
