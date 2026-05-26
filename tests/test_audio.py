import pygame
import audio

pygame.init()
audio.init()


def test_init_no_crash():
    audio.init()


def test_play_bgm_no_crash():
    audio.play_bgm()


def test_stop_bgm_no_crash():
    audio.stop_bgm()


def test_play_jumpscare_no_crash():
    audio.play_jumpscare()


def test_play_page_turn_no_crash():
    audio.play_page_turn()


def test_play_spooky_no_crash():
    audio.play_spooky()


def test_all_safe_when_mixer_disabled():
    original = audio._mixer_ok
    audio._mixer_ok = False
    try:
        audio.play_bgm()
        audio.stop_bgm()
        audio.play_jumpscare()
        audio.play_page_turn()
        audio.play_spooky()
    finally:
        audio._mixer_ok = original
