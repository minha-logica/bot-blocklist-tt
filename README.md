# BotBlockListTT
## Bot em Python Para Bloquear uma lista de usuários no Twitter

Você fornece uma lista com nomes de usuários e o bot bloqueia todos da lista.

## Como usar?
Instale as dependências
```
$ pip install -r requeriments.txt
```
Ou
```
$ pip3 install -r requeriments.txt
```
#### Etapas:

   **1° passo:** clonar ou baixar repositório
```
$ git clone https://github.com/minha-logica/bot-blocklist-tt
```
   **2° passo:** criar uma conta para desenvolvedores no site do Twitter(
[Twitter for Developers](https://developer.twitter.com/en/apply-for-access)). Nessa conta, crie um novo [App](http://dev.twitter.com/apps) e
certifique-se de gerar suas credenciais (chaves de acesso e tokens de acesso ). Também é preciso dar permissão de leitura e escrita para seu App.
  
 
   **3° passo:** crie um arquivo chamado `.env` no diretório principal dos arquivos baixados. Em seguida, adicione nele
as seguintes informações preenchendo com suas credenciais:

```
CONSUMER_KEY=your_consumer_key
CONSUMER_SECRET=your_consumer_secret
ACCESS_TOKEN=your_access_token
ACCESS_TOKEN_SECRET=your_access_token_secret 
```
Obs: Não coloque as credenciais entre aspas.

   **4° passo:**  no arquivo `blocklist.py` adicione os nomes de usuários que deseja bloquear na lista *usernames*.
Exemplo:
```python
usernames = [
    "fulano",
    "siclano",
    "beltrano"
]
```

Enfim, execute o arquivo ```main.py```.
```
$ python main.py
```

Para desfazer os bloqueios substitua `False` por `True` na variável *unblock* no arquivo `blocklist.py`
```python
unblock = True
```

Seja feliz! 🙂
