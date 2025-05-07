import requests
import os
from utils.helpes import format_date_str, translate


class NasaFetcher:
    def __init__(self, api_key, file_path="infos.txt"):
        self.api_key = api_key
        self.endpoint = f'https://api.nasa.gov/planetary/apod?api_key={self.api_key}'
        self.file_path = file_path

    def fetch_data(self):
        try:
            response = requests.get(self.endpoint)
            return response.json()
        except requests.exceptions.RequestException as err:
            print(f"[ERRO] Problema na requisição HTTP: {err}")
            return None

    def process_data(self, data):
        try:
            date = format_date_str(data['date'])  # Formata data para pt-Br
            # Traduz o titulo para o português
            title = translate(data['title'])
            # Traduz o texto de explicação
            explanation = translate(data['explanation'])

            return f"\nData: {date}\n Título: {title}\n Explicação: {explanation}\n Vídeo Youtube: {data['url']}\n"
        except KeyError as e:
            print(f"[ERRO] Chave ausente no JSON: {e}")
            return None

    def write_to_file(self, content):
        mode = 'a' if os.path.exists(self.file_path) else 'w'
        separator = "\n------------------------------------------------------------\n" if mode == 'a' else ''
        try:
            with open(self.file_path, mode, encoding="utf-8") as f:
                # Se o arquivo já existe, escreve o separador
                if separator:
                    f.write(separator)
                f.write(content)
        except IOError as err:
            print(f'[ERRO] Falha ao escrever no arquivo: {err}')

    def run(self):
        data = self.fetch_data()
        if data:
            content = self.process_data(data)
            if content:
                self.write_to_file(content)


if __name__ == "__main__":
    api_key = "eUbZeVfhkGSMYE4Eiwp0r76TKWz6o3jhyKcDNYsF"
    fetcher = NasaFetcher(api_key)
    fetcher.run()
