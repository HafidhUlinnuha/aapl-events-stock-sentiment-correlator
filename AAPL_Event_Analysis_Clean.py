import yfinance as yf
import pandas as pd

# 1. AMBIL DATA ASLI DARI YAHOO FINANCE
ticker_symbol = "AAPL"
data = yf.download(ticker_symbol, start="2020-01-01", end="2026-05-27")

# JAMINAN ANTI-ERROR: Ratakan kolom multi-index bawaan yfinance baru
if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.get_level_values(0)

# Reset index agar tanggal bursa menjadi kolom biasa
data = data.reset_index()

# Paksa kolom paling pertama hasil reset untuk bernama 'Date'
data.rename(columns={data.columns[0]: 'Date'}, inplace=True)
data['Date'] = pd.to_datetime(data['Date'])

# 2. DATA MANUAL TANGGAL EVENT APPLE (Akurat)
apple_events = [
    {"Tanggal": "2020-10-13", "Event": "iPhone 12 Announcement"},
    {"Tanggal": "2021-09-14", "Event": "iPhone 13 Announcement"},
    {"Tanggal": "2022-09-07", "Event": "iPhone 14 Announcement"},
    {"Tanggal": "2023-06-05", "Event": "Apple Vision Pro Reveal (WWDC)"},
    {"Tanggal": "2023-09-12", "Event": "iPhone 15 Announcement"},
    {"Tanggal": "2024-09-09", "Event": "iPhone 16 Announcement"},
    {"Tanggal": "2025-09-09", "Event": "iPhone 17 Announcement"}
]
df_events = pd.DataFrame(apple_events)
df_events['Tanggal'] = pd.to_datetime(df_events['Tanggal'])

# 3. LOGIKA KOMPARASI (Menggunakan .iloc agar anti-error indeks)
event_results = []

for index, row in df_events.iterrows():
    event_date = row['Tanggal']
    event_name = row['Event']
    
    # Cari posisi baris di mana tanggal bursa sama atau setelah hari H event
    matching_rows = data[data['Date'] >= event_date]
    
    if not matching_rows.empty:
        # Ambil indeks posisi baris angka pertama (misal baris ke-150 di Excel)
        h_nol_posisi = matching_rows.index[0]
        
        # Ambil harga 'Close' tepat di posisi baris hari H tersebut
        price_h0 = float(data.loc[h_nol_posisi, 'Close'])
        
        # Geser posisi baris sebanyak 7 hari kerja ke depan
        h_tujuh_posisi = h_nol_posisi + 7
        
        if h_tujuh_posisi < len(data):
            # Ambil harga 'Close' di posisi baris H+7
            price_h7 = float(data.loc[h_tujuh_posisi, 'Close'])
            
            # Hitung persentase return saham Apple
            return_7d = ((price_h7 - price_h0) / price_h0) * 100
            
            event_results.append({
                "Event_Name": event_name,
                "Event_Date": event_date.strftime('%Y-%m-%d'),
                "Price_At_Event": round(price_h0, 2),
                "Price_7_Days_After": round(price_h7, 2),
                "Return_7D_Percentage": round(return_7d, 2)
            })

# Transformasi hasil akhir menjadi tabel baru
df_analysis = pd.DataFrame(event_results)
print("\nHasil Analisis Korelasi Event Apple:")
print(df_analysis)

# 4. SIMPAN MENJADI FILE CSV ASLI
df_analysis.to_csv(r"C:\Users\asus\Downloads\AAPL_Event_Analysis_Clean.csv", index=False)
print("\n[SUKSES] File CSV asli data yfinance berhasil dibuat di folder Downloads!")
