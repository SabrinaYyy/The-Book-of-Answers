import pygame

_BGM_PATH       = "assets/sounds/pianotheme04_mp3_loop.mp3"
_JUMPSCARE_PATH = "assets/sounds/ambient_horror.ogg"

_mixer_ok      = False
_jumpscare_snd = None  # pygame.mixer.Sound — independent from music channel


def init():
    global _mixer_ok, _jumpscare_snd
    try:
        pygame.mixer.init()
        _mixer_ok = True
    except pygame.error as exc:
        print(f"Warning: audio unavailable — {exc}")
        return
    try:
        _jumpscare_snd = pygame.mixer.Sound(_JUMPSCARE_PATH)
    except (FileNotFoundError, OSError, pygame.error) as exc:
        print(f"Warning: jumpscare sound not found at {_JUMPSCARE_PATH!r} — {exc}")


def play_bgm():
    if not _mixer_ok:
        return
    pygame.mixer.stop()  # clear any Sound-channel playback (e.g. jumpscare)
    try:
        pygame.mixer.music.load(_BGM_PATH)
        pygame.mixer.music.play(-1)
    except (FileNotFoundError, OSError, pygame.error) as exc:
        print(f"Warning: BGM not found at {_BGM_PATH!r} — {exc}")


def stop_bgm():
    if not _mixer_ok:
        return
    try:
        pygame.mixer.music.stop()
    except pygame.error:
        pass


def play_page_turn():
    pass  # no sfx file yet; add asset and implement when ready


def play_spooky():
    pass  # no sfx file yet; add asset and implement when ready


def play_jumpscare():
    if not _mixer_ok or _jumpscare_snd is None:
        return
    try:
        pygame.mixer.music.stop()   # silence BGM while scare plays
        _jumpscare_snd.play()
    except pygame.error as exc:
        print(f"Warning: could not play jumpscare sound — {exc}")
