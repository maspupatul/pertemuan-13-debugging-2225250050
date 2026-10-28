# Pertemuan 13 — Debugging, Tracing, Testing, dan Test Case Python

## Identitas
**Nama:** Maspupatul Hasanah
**NIM:** 2225250050
**Kelas:** 3A

## Kasus
Praktik 4 membahas debugging pada tiga fungsi Python, yaitu fungsi menghitung rata-rata, menentukan status kelulusan, dan menentukan nilai tertinggi.

Program awal mengandung tiga bug yang perlu ditemukan dan diperbaiki melalui pengujian.

## Test Case

| ID | Pengujian | Data masukan | Hasil yang diharapkan |
|---|---|---|---|
| T1 | Rata-rata empat nilai | `[80, 60, 90, 70]` | `75.0` |
| T2 | Rata-rata dua nilai | `[100, 80]` | `90.0` |
| T3 | Status nilai 60 | `60` | `Lulus` |
| T4 | Status nilai 59 | `59` | `Tidak lulus` |
| T5 | Nilai tertinggi | `[80, 60, 90, 70]` | `90` |

## Bug Report

### Bug 1 — Perhitungan rata-rata
- **Masalah:** Program awal selalu membagi jumlah nilai dengan angka 5.
- **Akar penyebab:** Pembagi tidak disesuaikan dengan jumlah data.
- **Perbaikan:** Menggunakan `len(nilai)` sebagai pembagi dan menangani daftar kosong.

### Bug 2 — Status kelulusan
- **Masalah:** Nilai 60 menghasilkan status `Tidak lulus`.
- **Akar penyebab:** Kondisi menggunakan `nilai > 60`.
- **Perbaikan:** Mengubah kondisi menjadi `nilai >= 60`.

### Bug 3 — Penentuan nilai tertinggi
- **Masalah:** Program awal menghasilkan nilai tertinggi 0.
- **Akar penyebab:** Kondisi perbandingan menggunakan `x < tertinggi`, sehingga logikanya terbalik.
- **Perbaikan:** Menggunakan `x > tertinggi` dan menginisialisasi nilai tertinggi dari elemen pertama. Daftar kosong ditangani dengan mengembalikan `None`.

## Retest

Setelah ketiga bug diperbaiki, jalankan kembali seluruh test case.

| ID | Hasil yang diharapkan | Hasil aktual setelah perbaikan | Status |
|---|---|---|---|
| T1 | `75.0` | `75.0` | PASS |
| T2 | `90.0` | `90.0` | PASS |
| T3 | `Lulus` | `Lulus` | PASS |
| T4 | `Tidak lulus` | `Tidak lulus` | PASS |
| T5 | `90` | `90` | PASS |

## Cara Menjalankan

Buka terminal pada folder utama proyek, kemudian jalankan:

```bash
python praktik/praktik_4_debugging.py
```

## Refleksi

Melalui praktik ini, saya belajar bahwa kesalahan program tidak selalu menyebabkan program berhenti berjalan. Program juga dapat menghasilkan keluaran yang salah meskipun tidak menampilkan pesan error. Test case membantu menemukan kesalahan tersebut, sedangkan retest memastikan bahwa perbaikan menghasilkan keluaran sesuai harapan.


