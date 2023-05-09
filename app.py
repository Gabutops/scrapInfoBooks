from pywebio.input import textarea,actions
from pywebio import start_server
from pywebio.output import put_text, put_file, toast
from functions import add, delete_data_file

def submit_urls(urls):
    urls = urls.split(',')
    print(urls)
    try:
        add(urls)
        with open('data.csv', 'r', encoding='utf-8') as f:
            csv_data = f.read()
        put_file('lista.csv', csv_data.encode(), 'CSV')
        toast('Arquivo CSV salvo com sucesso!')
        delete_data_file()
    except Exception as e:
        put_text(f'Erro ao processar as URLs: {str(e)}')

def process_urls():
    urls = textarea(label='Insira as URLs, separadas por vírgulas:', rows=5)
    submit_urls(urls)
if __name__ == '__main__':
    start_server(process_urls, host="0.0.0.0", port=8000)