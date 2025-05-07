import requests
import os
from utils.helpes import format_date_str, translate

end_point = "https://api.nasa.gov/planetary/apod?api_key=eUbZeVfhkGSMYE4Eiwp0r76TKWz6o3jhyKcDNYsF"

response = requests.get(end_point)

# Função para escrever no arquivo
def write_file(file, new_content):
    # Verifica se arquivo existe
    # Se existe é adicionar conteúdo após o texto já escrito
    if os.path.exists(file):
        mode = 'a' # Abrir o arquivo para escrita
        separator = "\n------------------------------------------------------------\n"
    else: # Se não existe, cria o arquivo
       mode = 'w' # Cria o arquivo
       separator = ''

    # Abre o arquivo no modo 'a' ou 'w'
    with open(file, mode, encoding="utf-8") as f:
        # Se o arquivo já existe, escreve o separador
        if separator:
            f.write(separator)
        f.write(new_content)


def exection():
    # Try Excepet para tratar erros
    try:
        if response.status_code == 200: # Requisição == 200 ? Deu certo ?
            data = response.json()

            date = format_date_str(data['date']) # Formata data para pt-Br
            title = translate(data['title']) # Traduz o titulo para o português
            explanation = translate(data['explanation']) # Traduz o texto de explicação
            # Oque deve ser escrito no arquivo .txt
            new_content = (
                f"\nData: {date}\n"
                f"Título: {title}\n"
                f"Explicação: {explanation}\n"
                f"Vídeo Youtube: {data['url']}\n"
            )
            # Chamada da função para escrever o conteúdo
            write_file("infos.txt", new_content)
        else:
            print(f"Erro na requisição: {response.status_code}")
    except requests.exceptions.RequestException as err:
        print(f'[ERRO] Problema na requisição HTTP: {err}')
    except Exception as err:
        print(f'[ERRO] Problema inesperado: {err}')

exection()
