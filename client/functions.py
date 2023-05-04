from scrap import extract_data_from_amazon,extract_data_from_mundosInfinitos
import pandas as pd

def add(lista):
    headers = ['titulo', 'subtitulo', 'isbn-13', 'link-imagem', 'preco']
    df = pd.DataFrame(columns=headers)
    print('tabela criada')
    for link in lista:
        if 'amazon' in link:
            print('Amazon')
            data = extract_data_from_amazon(link)
        else:
            data = extract_data_from_mundosInfinitos(link)
        if len(data) != len(df.columns):
            raise ValueError("The number of elements in the data returned by extract_data_from_amazon() is different from the number of columns in the DataFrame.")
        
        nova_linha = pd.DataFrame([data], columns=df.columns)
        df = pd.concat([df, nova_linha], ignore_index=True)
        df.to_csv('data.csv', index=False, encoding='utf-8-sig',sep=";")
def delete_data_file():
    import os
    if os.path.exists('data.csv'):
        os.remove('data.csv')
    else:
        print("The file 'data.csv' does not exist.")