import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from googletrans import Translator
# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory


# Excel dosyasını okuma
file_path = './data/simplified_liar_train_dataset.xlsx'
df = pd.read_excel(file_path)

# Translator nesnesi
translator = Translator()

# 2. satırdan sonuna kadar D sütunundaki (Statement) verileri çevirme işlemi
def translate_cell(text):
    try:
        if pd.isnull(text):
            return ""  # Eğer hücre boşsa
        translated = translator.translate(text, src='en', dest='tr')
        return translated.text
    except Exception as e:
        return str(e)  # Hata durumunda hatayı geri döndür

# 2. satırdan itibaren tüm satırların Statement sütunundaki verileri çeviriyoruz
df.loc[0:, 'Türkçe Metin'] = df.loc[0:, 'Statement'].apply(translate_cell)

# Yeni tabloyu kaydedelim
output_path = './output_file/translated_liar_train_dataset.xlsx'
df.to_excel(output_path, index=False)

print(f"Çeviri işlemi tamamlandı. Yeni dosya: {output_path}")