# Web Scraper para Livros

Este projeto é um web scraper para livros em dois sites: Amazon e Mundos Infinitos. O objetivo do scraper é extrair informações sobre os livros, incluindo o título, o subtitulo, o ISBN-13, a imagem de capa e o preço.

## Configurando o driver do Chrome

Este projeto utiliza o navegador Chrome para fazer o scraping. Portanto, é necessário ter o chromedriver instalado na sua máquina. Você pode baixar o chromedriver a partir do [site oficial](https://chromedriver.chromium.org/downloads). Certifique-se de baixar a versão compatível com a sua versão do Chrome.

Após baixar o chromedriver, adicione o arquivo executável à variável PATH do sistema operacional. Isso permitirá que o Python encontre o chromedriver no caminho correto. Se você não souber como adicionar arquivos ao PATH, consulte a documentação do seu sistema operacional.

## Como utilizar
Para utilizar este web scraper, é necessário ter o Python 3 instalado na sua máquina. Além disso, é necessário instalar algumas bibliotecas de Python:

`pip install -r requirements.txt`

`py /app.py`

1. Abra seu navegador e acesse **https://localhost:80**
2. Insira na lista as *URLS*
3. Ele ira gerar um loop de raspagem dos links
4. Ao final ele ira gerar um arquivo *lista.csv* com os dados coletados
