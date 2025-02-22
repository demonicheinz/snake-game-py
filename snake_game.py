import pygame
import time
import random

pygame.init()

# Warna
putih = (255, 255, 255)
kuning = (255, 255, 102)
hitam = (0, 0, 0)
merah = (213, 50, 80)
hijau = (0, 255, 0)
biru = (50, 153, 213)

# Ukuran layar diperbesar
lebar = 800
tinggi = 600
layar = pygame.display.set_mode((lebar, tinggi), pygame.RESIZABLE)
pygame.display.set_caption('🐍 Snake Game')

# Kecepatan ular
tingkat_kecepatan = {
    "easy": 8,
    "medium": 12,
    "hard": 18
}

mode = "medium"
kecepatan = tingkat_kecepatan[mode]

# Ukuran blok ular
ukuran_blok = 20

# Font
font_gaya = pygame.font.SysFont("bahnschrift", 25)

# Skor
def skor(nilai):
    skor_teks = font_gaya.render("Skor: " + str(nilai), True, putih)
    layar.blit(skor_teks, [0, 0])

# Game loop
def game_loop():
    global layar, kecepatan, lebar, tinggi

    game_over = False
    game_tutup = False
    pause = False
    full_screen = False

    x1 = lebar / 2
    y1 = tinggi / 2

    x1_ubah = ukuran_blok
    y1_ubah = 0

    ular = []
    panjang_ular = 5

    for i in range(panjang_ular):
        ular.append([x1 - i * ukuran_blok, y1])

    makanan_x = round(random.randrange(0, lebar - ukuran_blok) / 20.0) * 20.0
    makanan_y = round(random.randrange(0, tinggi - ukuran_blok) / 20.0) * 20.0

    clock = pygame.time.Clock()

    while not game_over:

        while game_tutup:
            layar.fill(hitam)
            pesan = font_gaya.render("Game Over! Tekan C untuk main lagi atau Q untuk keluar", True, merah)
            layar.blit(pesan, [lebar / 6, tinggi / 3])
            skor(panjang_ular - 5)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_tutup = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_ubah != ukuran_blok:
                    x1_ubah = -ukuran_blok
                    y1_ubah = 0
                elif event.key == pygame.K_RIGHT and x1_ubah != -ukuran_blok:
                    x1_ubah = ukuran_blok
                    y1_ubah = 0
                elif event.key == pygame.K_UP and y1_ubah != ukuran_blok:
                    y1_ubah = -ukuran_blok
                    x1_ubah = 0
                elif event.key == pygame.K_DOWN and y1_ubah != -ukuran_blok:
                    y1_ubah = ukuran_blok
                    x1_ubah = 0
                elif event.key == pygame.K_p:
                    pause = not pause
                elif event.key == pygame.K_r:
                    game_loop()
                elif event.key == pygame.K_f:
                    full_screen = not full_screen
                    if full_screen:
                        info_layar = pygame.display.Info()
                        lebar, tinggi = info_layar.current_w, info_layar.current_h
                        layar = pygame.display.set_mode((lebar, tinggi), pygame.FULLSCREEN)
                    else:
                        lebar, tinggi = 800, 600
                        layar = pygame.display.set_mode((lebar, tinggi), pygame.RESIZABLE)
                elif event.key == pygame.K_1:
                    mode = "easy"
                    kecepatan = tingkat_kecepatan[mode]
                elif event.key == pygame.K_2:
                    mode = "medium"
                    kecepatan = tingkat_kecepatan[mode]
                elif event.key == pygame.K_3:
                    mode = "hard"
                    kecepatan = tingkat_kecepatan[mode]

        if pause:
            pause_teks = font_gaya.render("Game Paused - Tekan P untuk lanjut", True, kuning)
            layar.blit(pause_teks, [lebar / 4, tinggi / 2])
            pygame.display.update()
            continue

        x1 += x1_ubah
        y1 += y1_ubah

        # Melewati tembok
        if x1 >= lebar:
            x1 = 0
        elif x1 < 0:
            x1 = lebar - ukuran_blok
        if y1 >= tinggi:
            y1 = 0
        elif y1 < 0:
            y1 = tinggi - ukuran_blok

        layar.fill(biru)
        pygame.draw.rect(layar, hijau, [makanan_x, makanan_y, ukuran_blok, ukuran_blok])
        ular_kepala = [x1, y1]
        ular.append(ular_kepala)

        if len(ular) > panjang_ular:
            del ular[0]

        for blok in ular[:-1]:
            if blok == ular_kepala:
                game_tutup = True

        for blok in ular:
            pygame.draw.rect(layar, kuning, [blok[0], blok[1], ukuran_blok, ukuran_blok])

        skor(panjang_ular - 5)
        pygame.display.update()

        if x1 == makanan_x and y1 == makanan_y:
            makanan_x = round(random.randrange(0, lebar - ukuran_blok) / 20.0) * 20.0
            makanan_y = round(random.randrange(0, tinggi - ukuran_blok) / 20.0) * 20.0
            panjang_ular += 1

        clock.tick(kecepatan)

    pygame.quit()
    quit()

if __name__ == "__main__":
    game_loop()
