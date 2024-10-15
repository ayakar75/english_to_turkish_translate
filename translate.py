import numpy as np
import pandas as pd
import time
from googletrans import Translator

# Excel dosyasını okuma
file_path = './data/simplified_liar_test_dataset.xlsx'
df = pd.read_excel(file_path)

# Translator nesnesi
translator = Translator()


# 2. satırdan sonuna kadar D sütunundaki (Statement) verileri çevirme işlemi
def translate_cell(text, index):
    try:
        # Hücreyi NoneType olup olmadığını kontrol ederek string'e çevirme işlemi
        if text is None or pd.isnull(text):
            print(f"{index}. satır boş, atlanıyor.")
            return ""  # Eğer hücre boşsa boş döndür

        text = str(text).strip()  # Hücreyi string'e çevir ve boşlukları kaldır
        if text == "":
            print(f"{index}. satır boş, atlanıyor.")
            return ""  # Eğer hücre sadece boşluksa boş döndür

        # Çeviri işlemi
        translated = translator.translate(text, src='en', dest='tr')

        if translated is None or translated.text is None:
            print(f"{index}. satır çevirisi başarısız oldu, None değeri döndü.")
            return ""  # Hata durumunda boş döndür

        print(f"{index}. satır başarıyla çevrildi.")
        return translated.text

    except Exception as e:
        print(f"{index}. satır çevirilirken hata oluştu: {str(e)}")
        return ""  # Hata durumunda boş döndür


# 2. satırdan itibaren tüm satırların Statement sütunundaki verileri çeviriyoruz
for index, row in df.iterrows():
    df.at[index, 'Türkçe Metin'] = translate_cell(row['Statement'], index)

    # Her çeviri işleminden sonra kısa bir süre bekleme ekleyelim
    time.sleep(0 )  # 1 saniye bekleme, gerekirse artırabilirsiniz

# Yeni tabloyu kaydedelim
output_path = './output_file/translated_liar_test_ dataset.xlsx'
df.to_excel(output_path, index=False)

print(f"Çeviri işlemi tamamlandı. Yeni dosya: {output_path}")
