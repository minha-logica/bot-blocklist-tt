# BotBlockListTT
## Bot em Python Para Bloquear uma lista de usuários no Twitter

Você fornece uma lista com nomes de usuários e o bot bloqueia todos da lista. Também é 
possível criar uma lista de bloqueio de forma automática e personalizada.

## Como usar?

   Faça o clone do repositório
```
$ git clone https://github.com/minha-logica/bot-blocklist-tt
```
### Etapas:

   **1° passo:** Instale as dependências
```
$ pip install -r requirements.txt
```
Ou
```
$ pip3 install -r requirements.txt
```


   
   **2° passo:** criar uma conta para desenvolvedores no site do Twitter(
[Twitter for Developers](https://developer.twitter.com/en/apply-for-access)). Nessa conta, crie um novo [App](http://dev.twitter.com/apps) e
certifique-se de gerar suas credenciais (chaves de acesso e tokens de acesso ). Também é preciso dar permissão de leitura e escrita para seu App.
Veja este [tutorial para criação das credenciais.](https://medium.com/programadores-ajudando-programadores/api-do-twitter-criando-o-app-e-obtendo-os-tokens-28ef3e2a281c) 
 
   **3° passo:** crie um arquivo chamado `.env` no diretório principal dos arquivos baixados. Em seguida, adicione nele
as seguintes informações preenchendo com suas credenciais:

```
CONSUMER_KEY=your_consumer_key
CONSUMER_SECRET=your_consumer_secret
ACCESS_TOKEN=your_access_token
ACCESS_TOKEN_SECRET=your_access_token_secret 
```
Obs: Não coloque as credenciais entre aspas.

   **4° passo:**  no arquivo `usernames.txt` adicione os nomes de usuários que deseja bloquear(não 
use o caractere @ antes do username).
Exemplo:
```
fulano
siclano
beltrano
```

Enfim, se você executar o arquivo ```blocklist.py``` 
os usuários da lista serão bloqueados.
```
$ python blocklist.py
```
:warning: Atenção: tenha cuidado ao executar o bloqueio
de usuários. Ao bloquear um seguidor ele deixará 
de ser um seguidor, mesmo que depois você o 
desbloquei. Será preciso que ele mesmo siga você 
novamente depois do desbloqueio. Não nos responsabilizamos por qualquer prejuízo 
ou dano.

Obs: só é possível bloquear 50 usuários a cada 15 minutos. 
Esse limite de requisições é definido pela própria API do Twitter.

## Via Código (Nova funcionalidade)
Crie um arquivo chamado `my_blocklist.py` ou com um nome
de sua preferência para usar a função block via código.
### Bloqueio simples
Você pode utilizar o método `block()` da classe
BlockList. 
```python
from blocklist import BlockList
blocklist = BlockList()
blocklist.block(["fulano","siclano","beltrano"])
```
Para desbloquear usuários:
```python
from blocklist import BlockList
blocklist = BlockList()
blocklist.block(
    ["fulano","siclano","beltrano"],
    unblock=True    
)
```
### Lendo arquivo.txt
Você pode ler um arquivo de texto com nomes de usuários
e bloquea-los:
```python
from blocklist import BlockList
blocklist = BlockList(file_path="arquivo.txt")
usernames = blocklist.read()
blocklist.block(usernames)
```
Ou simplesmente,
```python
from blocklist import BlockList
blocklist = BlockList(file_path="usernames.txt")
blocklist.block()
```
### Pesquisar em seus seguidores
É possível pesquisar seguidores pela Bio
por meio de palavras-chave:
```python
from blocklist import BlockList
blocklist = BlockList(filters=["chatonildo"])
results = blocklist.search_in_followers()             
```
O método search_in_followers() retorna uma
lista de usernames de seguidores que foram verificados 
pelo filtro.

### Gravar nomes de usuários em um arquivo.txt
Cria ou atualiza um arquivo de texto com nomes 
de usuários.
```python
from blocklist import BlockList
blocklist = BlockList(file_path="arquivos.txt")
blocklist.update(["fulano","siclano","beltrano"])
```
Assim, podemos gravar a lista de usuarios
que pesquisamos em um arquivo e bloqueá-los:
```python
from blocklist import BlockList
blocklist = BlockList(
   filters = ["chatonildo"],
   file_path = "blocklist.txt"
)
results = blocklist.search_in_followers() 
if len(results) > 0:
    blocklist.update(results) 
    blocklist.block()          
```
:warning: Atenção: a pesquisa pode trazer resultados 
não esperados e você pode bloquear alguém 
por engano. Tenha cuidado ao usar os filtros.
Não nos responsabilizamos por qualquer prejuízo 
ou dano.

# Referências
[Documentação do Tweepy](https://docs.tweepy.org/en/stable/client.html)
[Documentação da API do Twitter](https://developer.twitter.com/en/docs/twitter-api)

Seja feliz! 🙂
