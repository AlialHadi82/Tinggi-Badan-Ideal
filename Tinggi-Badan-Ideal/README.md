   # 🔍 Cek Tinggi Ideal Berdasarkan Berat Badan

Aplikasi edukatif untuk mengecek estimasi tinggi badan ideal remaja berdasarkan berat badan dan jenis kelamin. Berguna dalam pelajaran Biologi atau Pendidikan Jasmani.

📸 Demo Highlights


![Screenshot 2025-06-01 211739](https://github.com/user-attachments/assets/6c4da584-d2a9-445e-bcdf-98020c12f059)

## 🧠 Logika
Menggunakan rumus Broca terbalik untuk estimasi tinggi:
- Laki-laki: tinggi = (berat + 100) - 10%
- Perempuan: tinggi = (berat + 100) - 15%

## 📋 Cara Menjalankan
1. Pastikan Python dan library berikut sudah diinstall:
   ```bash
   pip install ttkbootstrap Pillow
   ```
2. Jalankan dengan:
   ```bash
   python cek_tinggi_ideal.py
   ```

## 📁 Struktur Folder
```
cek-tinggi-ideal/
├── img/
│   ├── Laki.png
│   └── Perempuan.png
├── cek_tinggi_ideal.py
└── README.md
```
