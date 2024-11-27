import pandas as pd


# Muat data dari file CSV dengan encoding yang berbeda
df = pd.read_csv(r'D:\\Project\\Python\\TA\\SentimentAnalysis\\dataset\\NEWEST\\fix all analysis\\ganjar-fix.csv', encoding='ISO-8859-1')

# Tampilkan beberapa baris pertama untuk memastikan data telah dimuat dengan benar
print(df.head())

# Hitung jumlah setiap label di kolom 'Label'
label_counts = df['label_manually'].value_counts()

# Tampilkan hasil perhitungan
print(label_counts)
