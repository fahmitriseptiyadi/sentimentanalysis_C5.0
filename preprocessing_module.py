import pandas as pd
import re
import os
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
# from translate import Translator
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Download stopwords
import nltk
nltk.download('stopwords')
stop_words = stopwords.words('indonesian')

# Preprocessing functions
def cleaning_x_text(text):
    text = re.sub(r'@[A-Za-z0-9_]+', '', text)
    text = re.sub(r'#\w+', '', text)
    text = re.sub(r'RT[\s]+', '', text)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # Emoticons
        u"\U0001F300-\U0001F5FF"  # Symbols & Pictographs
        u"\U0001F680-\U0001F6FF"  # Transport & Map Symbols
        u"\U0001F1E0-\U0001F1FF"  # Flags (iOS)
        "]+",
        flags=re.UNICODE)
    text = emoji_pattern.sub(r'', text)
    text = re.sub(r'[^A-Za-z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def case_folding(text):
    return text.lower() if isinstance(text, str) else text

def normalisasi(str_text, norm_dict):
    for key, value in norm_dict.items():
        str_text = re.sub(r'\b' + re.escape(key) + r'\b', value, str_text)
    return str_text

def tokenize(text):
    return text.split()

def remove_stopwords(tokens):
    return [word for word in tokens if word not in stop_words]

def stem_text(tokens):
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    return [stemmer.stem(word) for word in tokens]

# def convert_english(text):
#     translator = Translator(to_lang="en", from_lang="id")
#     return translator.translate(text)

# Function to run all preprocessing steps
def run_preprocessing_cleanning(file_path):
    df = pd.read_csv(file_path)

    # Dictionary for normalization
    norm_dict_anies = {
    # "anis": " ",
    # "anies": " ",
    "bansos": "bantuan sosial",
    "bpk": "bapak",
    "ganjar": " ",
    "kacian": "kasihan",
    "kalo": "kalau",
    "klo": "kalau",
    "bagibagi": "bagi-bagi",
    "klu": "kalau",
    "jd": "jadi",
    "itung2": "anggap saja",
    "spy": "supaya",
    "aj": "aja",
    "krn": "karena",
    "masalakan": "masalahkan",
    "nga": "tidak",
    "ngga": "tidak",
    "ngurusin": "mengurus",
    "prabowogibran": "prabowo gibran",
    "sdh": "sudah",
    "spt": "seperti",
    "yg": "yang"
}

    df['cleasing'] = df['full_text'].apply(cleaning_x_text)
    df['case_folding'] = df['cleasing'].apply(case_folding)
    df['normalisasi'] = df['case_folding'].apply(lambda x: normalisasi(x, norm_dict_anies))
    df['tokenize'] = df['normalisasi'].apply(tokenize)
    df['filtering/stopword removal'] = df['tokenize'].apply(remove_stopwords)
   
   
   
    df['stemming_data'] = df['filtering/stopword removal'].apply(lambda x: ' '.join(stem_text(x)))


    # Save the preprocessed data (cleaning only)
    cleaning_file_path = 'Process/Hasil-Preprocessing-Data-Cleaning.csv'
    os.makedirs('Process', exist_ok=True)
    df[['full_text', 'cleasing', 'case_folding', 'normalisasi', 'tokenize', 'filtering/stopword removal', 'label']].to_csv(
        cleaning_file_path, encoding='utf-8', index=False
    )

    # Save the preprocessed data (stemming only)
    # Ambil kolom `stemming_data` dan `label`
    df_stemming = df[['stemming_data', 'label']]

    # Ganti nama kolom `stemming_data` menjadi `result-preprocessing`
    df_stemming = df_stemming.rename(columns={'stemming_data': 'result-preprocessing'})

    stemming_file_path = 'Process/Hasil-Preprocessing-Data-Steamming.csv'
    df_stemming.to_csv(stemming_file_path, encoding='utf-8', index=False)


    # Translate to English
    # df['translate'] = df['result-preprocessing'].apply(convert_english)

    # translated_file_path = 'Process/Hasil-Preprocessing-Data-Translated.csv'
    # df.to_csv(translated_file_path, encoding='utf-8', index=False)

    # return translated_file_path


def plot_and_save_label_distribution(df, save_path='Process/label_distribution.png'):
    """
    Fungsi untuk menghitung jumlah label positif, negatif, dan netral, 
    kemudian membuat grafik batang dan menyimpannya di folder Process.
    
    Parameters:
    df (pd.DataFrame): DataFrame yang berisi kolom 'label'.
    save_path (str): Path untuk menyimpan gambar grafik (default: 'Process/label_distribution.png').
    """
    # Hitung jumlah setiap label (positif, negatif, netral)
    label_counts = df['label'].value_counts()

    # Tampilkan hasil jumlah label
    print("Jumlah label positif, negatif, dan netral:")
    print(label_counts)

    # Membuat grafik batang
    plt.figure(figsize=(8, 6))
    sns.barplot(x=label_counts.index, y=label_counts.values, palette='viridis')

    # Menambahkan title dan label
    plt.title('Distribusi Label (Positif, Negatif, Netral)', fontsize=14)
    plt.xlabel('Label', fontsize=12)
    plt.ylabel('Jumlah', fontsize=12)

    # Menampilkan jumlah pada setiap batang
    for i, count in enumerate(label_counts.values):
        plt.text(i, count + 1, str(count), ha='center', fontsize=12)

    # Menyimpan grafik ke file
    os.makedirs('Process', exist_ok=True)
    plt.savefig(save_path, format='png')
    plt.close()  # Menutup figure untuk membebaskan memori

    print(f'Grafik label telah disimpan di {save_path}')

# # Contoh pemanggilan fungsi setelah membaca file CSV
# df = pd.read_csv('Process/Hasil-Preprocessing-Data-Steamming.csv')
# plot_and_save_label_distribution(df)

