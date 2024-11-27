import subprocess
import pandas as pd

# Ganti dengan token autentikasi Twitter yang sesuai
twitter_auth_token = '9007cd698b4ef1f1d3eaadb3be0b0618e874c5a2'

# Instal Pandas (hanya diperlukan jika Pandas belum terinstal)
print("Menginstal Pandas...")
subprocess.run(["pip", "install", "pandas"], check=True)

# Instal Node.js (harus dijalankan dengan hak akses yang tepat, seperti sudo di Linux)
print("Menginstal Node.js...")
subprocess.run(["sudo", "apt-get", "update"], check=True)
subprocess.run(["sudo", "apt-get", "install", "-y", "ca-certificates", "curl", "gnupg"], check=True)
subprocess.run(["sudo", "mkdir", "-p", "/etc/apt/keyrings"], check=True)
subprocess.run(["curl", "-fsSL", "https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key", "|", "sudo", "gpg", "--dearmor", "-o", "/etc/apt/keyrings/nodesource.gpg"], shell=True, check=True)
subprocess.run(["echo", "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_20.x nodistro main", "|", "sudo", "tee", "/etc/apt/sources.list.d/nodesource.list"], shell=True, check=True)
subprocess.run(["sudo", "apt-get", "update"], check=True)
subprocess.run(["sudo", "apt-get", "install", "nodejs", "-y"], check=True)

# Cek versi Node.js
print("Versi Node.js:")
subprocess.run(["node", "-v"], check=True)

# Specify the path to your CSV file
file_path = "tweets-data/your_file_name.csv"  # Ganti dengan nama file CSV yang sesuai

# Membaca file CSV ke dalam DataFrame Pandas
print(f"Membaca file CSV: {file_path}...")
df = pd.read_csv(file_path, delimiter=",")

# Pilih kolom 'full_text'
df = df[['full_text']]

# Tampilkan DataFrame
print("DataFrame:")
print(df)

# Cek jumlah tweet dalam DataFrame
num_tweets = len(df)
print(f"Jumlah tweet dalam dataframe adalah {num_tweets}.")
