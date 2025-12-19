# Vision Assistant Pro

Vision Assistant Pro adalah add-on canggih untuk NVDA yang menggunakan Google Gemini AI untuk menyediakan deskripsi visual, pengenalan teks (OCR), terjemahan, dan analisis dokumen yang cerdas—langsung dalam pembaca layar Anda.

## 1. Terjemahan Cerdas

- **Terjemahan Kontekstual:** Menggunakan AI untuk memahami nuansa teks.
- **Bahasa:** Atur bahasa Sumber, Target, dan Respons AI.
- **Tukar Cerdas (Smart Swap):** Secara otomatis menukar bahasa jika teks sumber cocok dengan bahasa target.

## 2. Pintasan Global

Untuk memastikan kompatibilitas maksimum dengan tata letak laptop, semua pintasan menggunakan **NVDA + Control + Shift**.

| Pintasan                    | Fungsi                 | Deskripsi                                                                    |
|-----------------------------|------------------------|------------------------------------------------------------------------------|
| NVDA+Ctrl+Shift+T           | Penerjemah Cerdas      | Menerjemahkan teks di bawah kursor navigator. Memprioritaskan seleksi.       |
| NVDA+Ctrl+Shift+Y           | Penerjemah Papan Klip  | Menerjemahkan konten papan klip.                                             |
| NVDA+Ctrl+Shift+S           | Dikte Cerdas           | Mengubah ucapan menjadi teks. Tekan sekali untuk mulai, lagi untuk berhenti. |
| NVDA+Ctrl+Shift+R           | Penyempurna Teks       | Meringkas, Memperbaiki Tata Bahasa, Menjelaskan, atau menjalankan **Prompt Kustom**. |
| NVDA+Ctrl+Shift+C           | Pemecah CAPTCHA        | Menangkap dan memecahkan CAPTCHA secara otomatis.                            |
| NVDA+Ctrl+Shift+V           | Visi Objek             | Mendeskripsikan objek navigator dengan obrolan tindak lanjut.                |
| NVDA+Ctrl+Shift+O           | Visi Layar Penuh       | Menganalisis seluruh tata letak dan konten layar.                            |
| NVDA+Ctrl+Shift+D           | Analisis Dokumen       | Tanya jawab tentang file PDF/TXT/MD/PY.                                         |
| NVDA+Ctrl+Shift+F           | OCR File               | OCR langsung dari file gambar/PDF.                                           |
| NVDA+Ctrl+Shift+A           | Transkripsi Audio      | Mentranskripsikan file MP3/WAV/OGG.                                          |
| NVDA+Ctrl+Shift+L           | Terjemahan Terakhir    | Membaca ulang terjemahan terakhir tanpa API.                                 |
| NVDA+Ctrl+Shift+U           | Cek Pembaruan          | Memeriksa GitHub untuk versi terbaru.                                        |
| NVDA+Ctrl+Shift+I           | Pelaporan Status       | Mengumumkan status saat ini (misalnya, "Mengunggah...", "Idle").             |

## 3. Prompt Kustom & Variabel

Buat perintah di Pengaturan: `Nama:Teks Prompt` (pisahkan dengan `|` atau baris baru).

### Variabel yang Tersedia

| Variabel         | Deskripsi                                        | Tipe Input       |
|------------------|--------------------------------------------------|------------------|
| `[selection]`    | Teks yang dipilih saat ini                       | Teks             |
| `[clipboard]`    | Konten papan klip                                | Teks             |
| `[screen_obj]`   | Tangkapan layar objek navigator                  | Gambar           |
| `[screen_full]`  | Tangkapan layar layar penuh                      | Gambar           |
| `[file_ocr]`     | Pilih gambar/PDF/TIFF (default ke "Ekstrak teks")| Gambar, PDF, TIFF|
| `[file_read]`    | Pilih dokumen teks                               | TXT, Kode, PDF   |
| `[file_audio]`   | Pilih file audio                                 | MP3, WAV, OGG    |

### Contoh Prompt Kustom

- **OCR Cepat:** `OCR Saya:[file_ocr]`
- **Terjemahkan Gambar:** `Terjemahkan Gbr:Ekstrak teks dari gambar ini dan terjemahkan ke bahasa Indonesia. [file_ocr]`
- **Analisis Audio:** `Ringkas Audio:Dengarkan rekaman ini dan ringkas poin-poin utamanya. [file_audio]`
- **Debugger Kode:** `Debug:Temukan bug dalam kode ini dan jelaskan: [selection]`

**Catatan:** Koneksi internet aktif diperlukan untuk semua fitur AI. TIFF multi-halaman diproses secara otomatis.

## Perubahan untuk 3.0

*   **Bahasa Baru:** Menambahkan terjemahan **Persia** dan **Vietnam**.
*   **Model AI yang Diperluas:** Mengatur ulang daftar pemilihan model dengan awalan yang jelas (`[Free]`, `[Pro]`, `[Auto]`) untuk membantu pengguna membedakan antara model gratis dan terbatas tarif (berbayar). Menambahkan dukungan untuk **Gemini 3.0 Pro** dan **Gemini 2.0 Flash Lite**.
*   **Stabilitas Dikte:** Meningkatkan stabilitas Dikte Cerdas secara signifikan. Menambahkan pemeriksaan keamanan untuk mengabaikan klip audio yang lebih pendek dari 1 detik, mencegah halusinasi AI dan kesalahan kosong.
*   **Penanganan File:** Memperbaiki masalah di mana mengunggah file dengan nama non-Inggris akan gagal.
*   **Optimasi Prompt:** Meningkatkan logika Terjemahan dan hasil Visi yang terstruktur.

## Perubahan untuk 2.9

*   **Menambahkan terjemahan Prancis dan Turki.**
*   **Tampilan Terformat:** Menambahkan tombol "Lihat Terformat" dalam dialog obrolan untuk melihat percakapan dengan gaya yang tepat (Judul, Tebal, Kode) di jendela yang dapat diakses standar.
*   **Pengaturan Markdown:** Menambahkan opsi baru "Bersihkan Markdown di Obrolan" di Pengaturan. Menghapus centang ini memungkinkan pengguna melihat sintaks Markdown mentah (misalnya, `**`, `#`) di jendela obrolan.
*   **Manajemen Dialog:** Memperbaiki masalah di mana jendela "Perbaiki Teks" atau obrolan akan terbuka berkali-kali atau gagal fokus dengan benar.
*   **Peningkatan UX:** Menstandarkan judul dialog file menjadi "Open" dan menghapus pengumuman ucapan yang berlebihan (misalnya, "Opening menu...") untuk pengalaman yang lebih lancar.

## Perubahan untuk 2.8
* Menambahkan terjemahan bahasa Italia.
* **Pelaporan Status:** Menambahkan perintah baru (NVDA+Control+Shift+I) untuk mengumumkan status add-on saat ini (misalnya, "Mengunggah...", "Menganalisis...").
* **Ekspor HTML:** Tombol "Save Content" dalam dialog hasil sekarang menyimpan output sebagai file HTML terformat, mempertahankan gaya seperti judul dan teks tebal.
* **UI Pengaturan:** Meningkatkan tata letak panel Pengaturan dengan pengelompokan yang dapat diakses.
* **Model Baru:** Menambahkan dukungan untuk gemini-flash-latest dan gemini-flash-lite-latest.
* **Bahasa:** Menambahkan bahasa Nepal ke bahasa yang didukung.
* **Logika Menu Perbaiki:** Memperbaiki bug kritis di mana perintah "Perbaiki Teks" akan gagal jika bahasa antarmuka NVDA bukan bahasa Inggris.
* **Dikte:** Peningkatan deteksi keheningan untuk mencegah output teks yang salah ketika tidak ada input ucapan.
* **Pengaturan Pembaruan:** "Periksa pembaruan saat startup" sekarang dinonaktifkan secara default untuk mematuhi kebijakan Toko Add-on.
* Pembersihan Kode.

## Perubahan untuk 2.7
* Migrasi struktur proyek ke Templat Add-on NV Access resmi untuk kepatuhan standar yang lebih baik.
* Menerapkan logika coba lagi otomatis untuk kesalahan HTTP 429 (Batas Tarif) untuk memastikan keandalan selama lalu lintas tinggi.
* Prompt terjemahan dioptimalkan untuk akurasi yang lebih tinggi dan penanganan logika "Smart Swap" yang lebih baik.
* Memperbarui terjemahan bahasa Rusia.

## Perubahan untuk 2.6
* Menambahkan dukungan terjemahan bahasa Rusia (Terima kasih kepada nvda-ru).
* Memperbarui pesan kesalahan untuk memberikan umpan balik yang lebih deskriptif mengenai konektivitas.
* Mengubah bahasa target default menjadi bahasa Inggris.

## Perubahan untuk 2.5
* Menambahkan Perintah OCR File Asli (NVDA+Control+Shift+F).
* Menambahkan tombol "Simpan Obrolan" ke dialog hasil.
* Menerapkan dukungan lokalisasi penuh (i18n).
* Memigrasikan umpan balik audio ke modul nada asli NVDA.
* Beralih ke Gemini File API untuk penanganan file PDF dan audio yang lebih baik.
* Memperbaiki kerusakan saat menerjemahkan teks yang berisi kurung kurawal.

## Perubahan untuk 2.1.1
* Memperbaiki masalah di mana variabel [file_ocr] tidak berfungsi dengan benar dalam Prompt Kustom.

## Perubahan untuk 2.1
* Menstandarkan semua pintasan untuk menggunakan NVDA+Control+Shift untuk menghilangkan konflik dengan tata letak Laptop NVDA dan hotkey sistem.

## Perubahan untuk 2.0
* Menerapkan sistem Pembaruan Otomatis bawaan.
* Menambahkan Cache Terjemahan Cerdas untuk pengambilan instan teks yang diterjemahkan sebelumnya.
* Menambahkan Memori Percakapan untuk menyempurnakan hasil secara kontekstual dalam dialog obrolan.
* Menambahkan perintah Terjemahan Papan Klip Khusus (NVDA+Control+Shift+Y).
* Mengoptimalkan prompt AI untuk secara ketat menegakkan output bahasa target.
* Memperbaiki kerusakan yang disebabkan oleh karakter khusus dalam teks input.

## Perubahan untuk 1.5
* Menambahkan dukungan untuk lebih dari 20 bahasa baru.
* Menerapkan Dialog Perbaiki Interaktif untuk pertanyaan tindak lanjut.
* Menambahkan fitur Dikte Cerdas Asli.
* Menambahkan kategori "Vision Assistant" ke dialog Input Gestures NVDA.
* Memperbaiki kerusakan COMError di aplikasi tertentu seperti Firefox dan Word.
* Menambahkan mekanisme coba lagi otomatis untuk kesalahan server.

## Perubahan untuk 1.0
* Rilis awal.
