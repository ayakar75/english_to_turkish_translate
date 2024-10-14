import numpy as np
import pandas as pd
from googletrans import Translator

# Excel dosyasını okuma
file_path = './data/simplified_liar_train_dataset.xlsx'
df = pd.read_excel(file_path)

# Translator nesnesi
translator = Translator()


# 2. satırdan sonuna kadar D sütunundaki (Statement) verileri çevirme işlemi
def translate_cell(text, index):
    try:
        if pd.isnull(text):
            print(f"{index}. satır boş, atlanıyor.")
            return ""  # Eğer hücre boşsa boş döndür
        translated = translator.translate(text, src='en', dest='tr')
        print(f"{index}. satır başarıyla çevrildi.")
        return translated.text
    except Exception as e:
        print(f"{index}. satır çevirilirken hata oluştu: {str(e)}")
        return str(e)  # Hata durumunda hatayı geri döndür


# 2. satırdan itibaren tüm satırların Statement sütunundaki verileri çeviriyoruz
for index, row in df.iterrows():
    df.at[index, 'Türkçe Metin'] = translate_cell(row['Statement'], index)

# Yeni tabloyu kaydedelim
output_path = './output_file/translated_liar_train_dataset.xlsx'
df.to_excel(output_path, index=False)

print(f"Çeviri işlemi tamamlandı. Yeni dosya: {output_path}")
