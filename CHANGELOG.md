# Changelog

Semua perubahan besar akan tercatat di bawah ini. Untuk informasi lebih lanjut, silakan merujuk pada dokumentasi lebih lanjut atau laporan bug.

## [Unreleased]

### ✔️ Added

-

### ♻️ Changed

-

### 🐛 Fixed

-

## [1.2.0] - Stability & UX Improvements - 2025-02-22

### ✔️ Added

- Ular langsung bergerak ke kanan saat game dimulai.
- Blokir perubahan arah 180° secara langsung untuk mencegah tabrakan instan.

### ♻️ Changed

- Penyesuaian posisi teks skor & peningkatan visual minor.

### 🐛 Fixed

- Perbaiki bug game over instan saat game dimulai.
- Cegah tabrakan awal antar segmen ular saat spawn.

## [1.1.0] - Gameplay Enhancements - 2025-02-22

### ✔️ Added

- Fitur tembus tembok (warp wall): ular bisa berpindah sisi layar.
- Perbesar layar menjadi 800x600 untuk ruang bermain lebih luas.
- Panjang awal ular ditingkatkan menjadi 5 blok.
- Kurangi kecepatan ular agar lebih mudah dikendalikan.

### ♻️ Changed
- Penyesuaian algoritma gerakan ular agar kompatibel dengan fitur tembus tembok.

## [1.0.0] Initial Release - 2025-02-22

### ✔️ Added

- Implementasi dasar game Snake menggunakan Pygame.
- Ukuran layar standar (600x400).
- Ular mulai dengan 1 blok.
- Makanan muncul secara acak.
- Game over saat ular menabrak dirinya sendiri atau dinding.