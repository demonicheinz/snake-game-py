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

# Ukuran layar
lebar = 600
tinggi = 400
layar = pygame.display.set_mode((lebar, tinggi))
pygame.display.set_caption('🐍 Snake Game')

# Kecepatan ular
kecepatan = 15

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
    game_over = False
    game_tutup = False

    x1 = lebar / 2
    y1 = tinggi / 2

    x1_ubah = 0
    y1_ubah = 0

    ular = []
    panjang_ular = 1

    makanan_x = round(random.randrange(0, lebar - ukuran_blok) / 20.0) * 20.0
    makanan_y = round(random.randrange(0, tinggi - ukuran_blok) / 20.0) * 20.0

    clock = pygame.time.Clock()

    while not game_over:

        while game_tutup:
            layar.fill(hitam)
            pesan = font_gaya.render("Game Over! Tekan C untuk main lagi atau Q untuk keluar", True, merah)
            layar.blit(pesan, [lebar / 6, tinggi / 3])
            skor(panjang_ular - 1)
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
                if event.key == pygame.K_LEFT:
                    x1_ubah = -ukuran_blok
                    y1_ubah = 0
                elif event.key == pygame.K_RIGHT:
                    x1_ubah = ukuran_blok
                    y1_ubah = 0
                elif event.key == pygame.K_UP:
                    y1_ubah = -ukuran_blok
                    x1_ubah = 0
                elif event.key == pygame.K_DOWN:
                    y1_ubah = ukuran_blok
                    x1_ubah = 0

        if x1 >= lebar or x1 < 0 or y1 >= tinggi or y1 < 0:
            game_tutup = True

        x1 += x1_ubah
        y1 += y1_ubah
        layar.fill(biru)
        pygame.draw.rect(layar, hijau, [makanan_x, makanan_y, ukuran_blok, ukuran_blok])
        ular_kepala = []
        ular_kepala.append(x1)
        ular_kepala.append(y1)
        ular.append(ular_kepala)

        if len(ular) > panjang_ular:
            del ular[0]

        for blok in ular[:-1]:
            if blok == ular_kepala:
                game_tutup = True

        for blok in ular:
            pygame.draw.rect(layar, kuning, [blok[0], blok[1], ukuran_blok, ukuran_blok])

        skor(panjang_ular - 1)
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
