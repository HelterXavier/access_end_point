from datetime import datetime
from deep_translator import GoogleTranslator

def format_date_str(date):
    date_obj = datetime.strptime(date, "%Y-%m-%d")  # Coverte para datetime

    format_date = date_obj.strftime("%d/%m/%Y")  # Coverte para strig

    return format_date


def translate(text: str) -> str:
    translated = GoogleTranslator(source='en', target='pt').translate(text)

    return translated
