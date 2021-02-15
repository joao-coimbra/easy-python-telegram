<h1 align="center">Easy Python Telegram</h1>
<p align="center">Uma forma fácil de usar o <a title='documentação' href="https://github.com/python-telegram-bot/python-telegram-bot">python-telegram-bot</p>

## Atalho
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Funções](#funções)
- [Demonstração](#demonstração)

## Pré-requisitos

Tenha uma conversa com o <a href="https://t.me/botfather">BotFather</a> do telegram para dar vida ao seu Chat Bot!

Inicie a conversa com um <span style="color:purple">/start</span>.

Vamos começar a criar seu robô chat? Digite <span style="color:purple">/newbot</span>.

Escolha um nome para sua criação, escolherei <span style="color:purple">Alexander</span>. Diga olá ao Alexander!

Por fim escolha um username para ele com terminação _bot, dê o nome de sua empresa ou algo pessoal. Colocarei para exemplo <span style="color:purple">SampleTelegram_bot</span>

Clique no link enviado, algo como <span style="color:purple !important">t.me/(username)</span>.

Será redirecionado para o chat já com <span style="color:purple">/start</span> e estará ligado para seu trabalho.

Copie todo o <code style="color:#c7254e;background-color: #f9f2f4;padding: 2px 4px;font-size: 90%;border-radius: 4px;">TOKEN</code> enviado que será utilizado futuramente no código como a variável <span style="color:ORANGE">TELEGRAM_TOKEN</span>

Crie um novo grupo no telegram e adicione seu robô.

Capture a url da página, exemplo: https://web.telegram.org/#/im?p=g123456789, e copie os números finais adicionando um sinal negativo no início <code style="color:#c7254e;background-color: #f9f2f4;padding: 2px 4px;font-size: 90%;border-radius: 4px;"><strong>-123456789</strong></code>, futuramente será utilizada como a variável <span style="color:ORANGE">CHAT_ID</span> 

## Instalação

Para começar clone os arquivos em seu diretório:

```shell
$ git clone https://github.com/joao-coimbra/easy-python-telegram.git
```

ou faça o download <a title="download" href="https://">clicando aqui</a>

Instale a API do telegram

```shell
> pip install python-telegram-bot --upgrade
```

## Como usar

No arquivo <span style='color:#0cb7f0;'>telegram_chat/keys.py</span> insira respectivamente sua <span style="color:orange">TELEGRAM_TOKEN</span> e <span style="color:orange">CHAT_ID</span>

importe em seus arquivos:

<code><i style="color:#e046e0">import</i> telegram_chat.bot <i style="color:#e046e0">as</i> telegram</code>

## Funções

Para enviar uma mensagem no chat do telegram utilize a função <code>telegram.<span style='color:#0cb7f0;'>sendMessage()</span></code>.
Caso queira enviar uma imagem utilize a função <code>telegram.<span style='color:#0cb7f0;'>sendImage()</span></code>

#### Parâmetros

<code><span style='color:#0cb7f0;'>sendMessage(<span style='color:#e34f4f;'><i>text</i></span>)</span></code>
<br>
<i><span style='color:#e34f4f;'>text</span> → type: string</i>, recebe o texto que será enviado.

<code><span style='color:#0cb7f0;'>sendImage(<span style='color:#e34f4f;'><i>img</i></span>, <span style='color:#e34f4f;'><i>local</i></span>)</span></code>
<br>
<i><span style='color:#e34f4f;'>img</span> → type: string</i>, recebe uma url destinada a imagem.
<br>
<i><span style='color:#e34f4f;'>local</span> → type: boolean</i>, recebe um valor booleano para identificar se é uma imagem local ou externa, por padrão recebe <span style="color:orange">True</span>

## Demonstração

```python
import telegram_chat.bot as telegram

telegram.sendMessage('Hello World!')
telegram.sendImage('src/img/sample.jpg')
```

No código acima possui um exemplo de uso do código, encontrado no arquivo <span style='color:grey'>sample.py</span>
Ao executar, será impresso no grupo do telegram uma mensagem do Alexander, dizendo: <span style='color:grey'>Hello World!</span> e uma imagem encontrada na pasta <span style='color:grey'>src/img/sample.jpg</span>

<img style='width:30%; border-radius: 20px' src="src/img/result.png">

Para uma mensagem maior com quebra de linha, apenas utilize a quebra de linha <span style='color:teal'>\n</span> ou <span style='color:teal'>```</span>

## License
[MIT](https://choosealicense.com/licenses/mit/)
