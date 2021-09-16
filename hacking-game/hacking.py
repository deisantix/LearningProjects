import pygame
import random
import os
import sys
pygame.init()

punctuation = '!#$%&()/:;<=>?@[]{|}'
chance = (1, 2, 3, 4, 5, 6, 7)

pygame.display.set_caption("Hacking")

# VARIAVEIS DO JOGO
FPS = 60
delay = 1000  # 1000
SIZE = WIDTH, HEIGHT = 640, 480

attempts = 4

password = ''
with open('passwords') as secret_passwords:
    senhas_secretas = []

    for ps in secret_passwords:
        ps = ps.strip()
        senhas_secretas.append(ps)

    password = random.choice(senhas_secretas)

clock = pygame.time.Clock()

# CORES
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# CRIAR JANELA
WINDOW = pygame.display.set_mode(SIZE)

# CRIAR FONTE E RENDERIZAR TEXTOS
font = pygame.font.Font('kongtext.ttf', 12)
header0 = font.render(os.getcwd(), True, GREEN)
header1 = font.render("DEBUG MODE", True, GREEN)
header2 = font.render(f"{attempts} ATTEMPT(S) LEFT", True, GREEN)
password_input = font.render("Enter the password > ", True, GREEN)

# REDENRIZAR TEXTOS DE QUE GANHOU
palavra_certa = font.render(password, True, GREEN)
exiting_debug_mode = font.render("EXITING DEBUG MODE", True, GREEN)
login_successful = font.render("LOGIN SUCCESSFUL - WELCOME BACK", True, GREEN)
press_enter = font.render("PRESS ENTER TO CONTINUE", True, GREEN)

palavra_certa_rect = palavra_certa.get_rect(center=(WIDTH/2, (HEIGHT/2) - 60))
exiting_debug_mode_rect = exiting_debug_mode.get_rect(center=(WIDTH/2, (HEIGHT/2) - 30))
login_successful_rect = login_successful.get_rect(center=(WIDTH/2, (HEIGHT/2) + 0))
press_enter_rect = press_enter.get_rect(center=(WIDTH/2, (HEIGHT/2) + 30))

# REDENRIZAR TEXTOS DE QUE PERDEU
login_failure = font.render("LOGIN FAILURE - TERMINAL LOCKED", True, GREEN)
contact_administrator = font.render("PLEASE CONTACT AN ADMINISTRATOR", True, GREEN)
press_enter_exit = font.render("PRESS ENTER TO EXIT", True, GREEN)

login_failure_rect = login_failure.get_rect(center=(WIDTH/2, (HEIGHT/2) - 30))
contact_administrator_rect = contact_administrator.get_rect(center=(WIDTH/2, (HEIGHT/2) + 0))
press_enter_exit_rect = press_enter_exit.get_rect(center=(WIDTH/2, (HEIGHT/2) + 30))

# USER INPUT E RETANGULO DO TEXTO
user_input = ''
input_rect = pygame.Rect(255, 385, 140, 12)

# VARIAVEIS PARA CONTROLAR AS POSIÇOES DA ENTRADA
password_pos = pw_pos_x, pw_pos_y = 10, 385
draw_pw_input = []
wrong_word = []
wrong_word_pos = {}


# DESENHAR HEADER DO JOGO: FILL BLACK, PATH, "DEBUG MODE" E TENTATIVAS RESTANTES
def draw_header():
    WINDOW.fill(BLACK)
    WINDOW.blit(header0, (10, 10))
    WINDOW.blit(header1, (10, 25))
    WINDOW.blit(header2, (10, 40))


# CRIA LINHAS ALEATORIAS E BAGUNÇADAS DO JOGO
def gerador_linha():
    global password
    # PEGA PALAVRAS DO ARQUIVO
    with open('passwords') as passwords:
        senhas = []

        for p in passwords:
            p = p.strip()
            senhas.append(p)

    # GERAR LINHA
    linha = ''
    senha = random.choice(senhas)

    for tl in range(13):
        pos = random.choice(chance)
        c = random.choice(punctuation)

        linha += c

        if pos == 5 and senha not in linha:
            linha += senha

    if senha not in linha:
        linha += senha

    return linha


# COLOCA AS LINHAS CRIADAS PELA FUNÇÃO DE GERAR LINHAS EM UMA LISTA
esta_nas_linhas = False
while True:
    passwords_line = [gerador_linha() for i in range(20)]

    for ln in passwords_line:
        if password in ln:
            esta_nas_linhas = True
            break

    if not esta_nas_linhas:
        continue
    else:
        break


# CRIA A ANIMAÇÃO DE GERAR LINHAS ALEATORIAS NO JOGO
def gerador_bug_passwords():
    ticks = 0
    while ticks < 150000:
        ticks += pygame.time.get_ticks()

        pos_y = 70

        draw_header()

        for i in range(20):
            linha = gerador_linha()

            pw = font.render(linha, True, GREEN)
            WINDOW.blit(pw, (10, pos_y))

            pos_y += 15

        pygame.display.update()

    pos_y = 70
    draw_header()
    for line in passwords_line:
        pw = font.render(line, True, GREEN)
        WINDOW.blit(pw, (10, pos_y))

        pos_y += 15
    pygame.display.update()

    pygame.time.wait(delay)


# DESENHA NA TELA
def draw_screen():
    draw_header()

    # DESENHA AS LINHAS DE SENHAS ─
    pos_y = 70
    for line in passwords_line:
        pw = font.render(line, True, GREEN)
        WINDOW.blit(pw, (10, pos_y))

        pos_y += 15

    # DESENHA O INPUT PARA ADIVINHAR A SENHA ─
    WINDOW.blit(password_input, (pw_pos_x, pw_pos_y))

    # DESENHA O INPUT DO USUARIO ─
    # pygame.draw.rect(WINDOW, GREEN, input_rect, 1)
    text_surface = font.render(user_input, True, GREEN)
    WINDOW.blit(text_surface, (input_rect.x, input_rect.y))

    draw_errors()

    pygame.display.update()


# DESENHA O TEXTO COM DELAY
def draw_delayed(txt, pos):
    WINDOW.blit(txt, pos)
    pygame.display.update()
    pygame.time.wait(delay)


def draw_errors():
    # DESENHA O INPUT FALHO ─
    for pos_x, pos_y in draw_pw_input:
        WINDOW.blit(password_input, (pos_x, pos_y))

    # DESENHA A PALAVRA ERRADA JUNTO DO INPUT ─
    for word in wrong_word_pos:
        WINDOW.blit(word, wrong_word_pos[word])

    # DESENHA PALAVRA INCORRETA DO OUTRO LADO DA JANELA ─
    pos_palavra_errada = 25
    for word in wrong_word:
        palavra_errada = font.render(f'{word} INCORRECT', True, GREEN)
        WINDOW.blit(palavra_errada, (WIDTH//2, pos_palavra_errada))

        hint = verificar_user_input(word)
        hint_message = font.render(hint, True, GREEN)
        WINDOW.blit(hint_message, (WIDTH//2, pos_palavra_errada + 15))

        pos_palavra_errada += 30


    pygame.display.update()


def verificar_user_input(entrada):
    tam = len(entrada)

    letras_comum = 0
    for l in entrada:
        if l in password:
            letras_comum += 1

    return f'{letras_comum}/{tam} IN MATCHING POSITION'


def drawing_win():
    WINDOW.fill(BLACK)
    WINDOW.blit(palavra_certa, palavra_certa_rect)
    WINDOW.blit(exiting_debug_mode, exiting_debug_mode_rect)
    WINDOW.blit(login_successful, login_successful_rect)
    WINDOW.blit(press_enter, press_enter_rect)

    pygame.display.update()


def win_message():
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    run = False



        drawing_win()


def drawing_loss():
    WINDOW.fill(BLACK)
    WINDOW.blit(palavra_certa, palavra_certa_rect)
    WINDOW.blit(login_failure, login_failure_rect)
    WINDOW.blit(contact_administrator, contact_administrator_rect)
    WINDOW.blit(press_enter_exit, press_enter_exit_rect)

    pygame.display.update()


def loss_message():
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    run = False

        drawing_loss()


# PROGRAMA PRINCIPAL
def main():
    global user_input, pw_pos_x, pw_pos_y, attempts, header2

    typing_active = True
    run = True
    win = False

    draw_delayed(header0, (10, 10))
    draw_delayed(header1, (10, 25))
    draw_delayed(header2, (10, 40))

    gerador_bug_passwords()

    draw_delayed(password_input, (10, 385))

    # ──────────────────────────────────────────────────────
    # GAME LOOP ────────────────────────────────────────────
    # ──────────────────────────────────────────────────────
    while run and attempts:
        header2 = font.render(f"{attempts} ATTEMPT(S) LEFT", True, GREEN)

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            if typing_active:
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        typing_active = False

                    elif event.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1]

                    else:
                        user_input += event.unicode

        draw_screen()

        # CASO O USUARIO TENHA APERTADO ENTER ─ O QUE SIGNIFICARIA QUE TERIA ESCRITO A SENHA
        if not typing_active:
            # CASO A SENHA FOR CERTA ──
            if user_input == password:
                win = True
                run = False

            # CASO A SENHA FOR ERRADA ── REINICIAR O INPUT
            else:
                verificar_user_input(user_input)

                attempts -= 1
                wrong_word.append(user_input)

                draw_pw_input.append((pw_pos_x, pw_pos_y))
                wrong_w = font.render(user_input, True, GREEN)
                wrong_word_pos[wrong_w] = (input_rect.x, input_rect.y)

                pw_pos_y += 15
                input_rect.y += 15

                user_input = ''
                typing_active = True

    if win:
        WINDOW.fill(BLACK)
        draw_delayed(palavra_certa, palavra_certa_rect)
        draw_delayed(exiting_debug_mode, exiting_debug_mode_rect)
        draw_delayed(login_successful, login_successful_rect)
        draw_delayed(press_enter, press_enter_rect)

        win_message()

    else:
        WINDOW.fill(BLACK)
        draw_delayed(palavra_certa, palavra_certa_rect)
        draw_delayed(login_failure, login_failure_rect)
        draw_delayed(contact_administrator, contact_administrator_rect)
        draw_delayed(press_enter_exit, press_enter_exit_rect)

        loss_message()

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
