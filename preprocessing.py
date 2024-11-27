import pandas as pd
import re
import string
import nltk
import os
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from translate import Translator

from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = stopwords.words('indonesian')

# Specify the path to your CSV file
file_path = r"D:\\Project\\Python\\TA\\SentimentAnalysis\\raw\\gibran.csv"

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path, delimiter=",")

# Select the 'full_text' column
df = df[['full_text']]

# Display the DataFrame
print(df)

# Cek jumlah data yang didapatkan
num_tweets = len(df)
print(f"Jumlah tweet dalam dataframe adalah {num_tweets}.")


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
  if isinstance(text, str):
    lowercase_text = text.lower()
    return lowercase_text

  else:
    return text

 # ->dictionary
norm_dict = {
    "anis": " ",
    "anies": " ",
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
    "supaya": "supaya",
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

def normalisasi(str_text):
    for key, value in norm_dict.items():
        str_text = re.sub(r'\b' + re.escape(key) + r'\b', value, str_text)
    return str_text

def tokenize(text):
  tokens = text.split()
  return tokens

def remove_stopwords(text):
  return [word for word in text if word not in stop_words]


df['cleasing'] = df['full_text'].apply(cleaning_x_text)
df['case_folding'] = df['cleasing'].apply(case_folding)
df['normalisasi'] = df['case_folding'].apply(normalisasi)
df['tokenize'] = df['normalisasi'].apply(tokenize)
df['filtering/stopword removal'] = df['tokenize'].apply(remove_stopwords)
df

file_path = 'Process/Hasil-Preprocessing-Data-batch1.csv'
df.to_csv(file_path, encoding='utf-8', index=False)
print(f'File telah disimpan di {file_path}')


from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

factory = StemmerFactory()
stemmer = factory.create_stemmer()

def stem_text(text):
  return [stemmer.stem(word) for word in text]

df['stemming_data'] = df['filtering/stopword removal'].apply(lambda x: ' '.join(stem_text(x)))
df = df[['stemming_data']]
df = df.rename(columns={'stemming_data': 'result-preprocessing'})


if not os.path.exists("Process"):
    os.makedirs("Process")

file_path = 'Process/Hasil-Preprocessing-Data-batch2.csv'
df.to_csv(file_path, encoding='utf-8', index=False)
print(f'File telah disimpan di {file_path}')
print(df)


file_path = 'Process/Hasil-Preprocessing-Data-batch2.csv'
df = pd.read_csv(file_path)


def convert_english(text):
  translator = Translator(to_lang="en", from_lang="id")
  translation = translator.translate(text)
  return translation

# df['translate'] = df['full_text_preprocessing'].apply(lambda x: convert_english(x))
df['translate'] = df['result-preprocessing'].apply(convert_english)
print(df)

if not os.path.exists("Process"):
    os.makedirs("Process")

file_path = 'Process/Hasil-Preprocessing-Data-batch3.csv'
df.to_csv(file_path, encoding='utf-8', index=False)
print(f'File telah disimpan di {file_path}')
df

