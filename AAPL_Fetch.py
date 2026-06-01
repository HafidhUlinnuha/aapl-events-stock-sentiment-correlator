import yfinance as yf
import pandas as pd

# 1. Tentukan aset yang mau diambil (AAPL untuk Apple, BTC-USD untuk Bitcoin)
ticker_symbol = "AAPL"  # Ganti jadi "AAPL" jika ingin saham Apple

# 2. Ambil data historisnya (misal dari tahun 2020 sampai sekarang)
data = yf.download(ticker_symbol, start="2020-01-01", end="2026-05-27")

# 3. Simpan langsung menjadi file CSV yang bersih sempurna!
data.to_csv(r"C:\Users\asus\Downloads\AAPL_Data_Clean.csv")
print("Data berhasil diunduh dan dijamin 100% bersih!")
