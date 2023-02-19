
# BATCH-MP3-SYNC

Projeto de Download e Conversão de Vídeos do YouTube para MP3


## Apêndice

Este projeto em Python tem como objetivo baixar vídeos do YouTube e convertê-los para MP3. Além disso, ele também verifica se há um dispositivo conectado ao computador e move automaticamente os arquivos convertidos para a pasta correspondente do dispositivo.


## Stack utilizada
**Back-end:** Python 3.10 ou acima


## Deploy

Para utilizar este projeto, é necessário instalar as seguintes bibliotecas:

pytube: utilizada para fazer o download dos vídeos do YouTube;
moviepy: utilizada para converter os vídeos para MP3 e manipular arquivos de áudio e vídeo;
psutil: utilizada para verificar se um dispositivo está conectado ao computador;
pywin32: utilizada para interagir com o sistema operacional Windows e manipular dispositivos conectados.

As bibliotecas podem ser instaladas utilizando o gerenciador de pacotes pip. 

Abra o terminal ou prompt de comando e digite os seguintes comandos:

```bash
    pip install pytube
    pip install moviepy
    pip install psutil
    pip install pywin32
```

Com as bibliotecas instaladas, é possível utilizar as funções do projeto.

### O próximo passo é configurar o projeto para executar corretamente!

A classe configs é responsável por armazenar os parâmetros de configuração utilizados pelo script. A documentação indica que para o funcionamento correto do script, é importante que os parâmetros sejam informados corretamente, incluindo o caminho dos diretórios.

A classe possui os seguintes atributos:

- playlist_id: uma string que armazena a ID da playlist do YouTube que será baixada.
- folder: uma string que armazena o caminho completo do diretório onde serão armazenados os arquivos baixados.
- download_folder: uma string que armazena o caminho completo do diretório onde serão armazenados os arquivos baixados temporariamente, antes de serem convertidos para MP3.
- mp3_folder_path: uma string que armazena o caminho completo do diretório para onde os arquivos MP3 serão movidos após a conversão.
- create_playlist_cache: um valor booleano que indica se o script deve criar um arquivo de cache para a playlist. Se o valor for True, o script não tentará baixar novamente arquivos que já foram baixados anteriormente.

Portanto, a classe configs fornece uma maneira de armazenar os parâmetros de configuração utilizados pelo script de download de vídeos do YouTube e conversão para MP3.



## Autores

- [@MarlonDantas](https://www.github.com/marlondantas)


## Funcionalidades

- Você pode utilizar esse projeto livremente.
- Uma forma de uso, se tiver um servidor ou computador pessoal, pode agendar a execução desse Scrpit varias vezes por dia, assim suas músicas sempre serão baixadas e atualizadas para o dispositivo conectado.


