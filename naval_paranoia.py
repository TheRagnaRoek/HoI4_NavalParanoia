"""Hearts of Iron 4 - Naval Paranoia

This is a simple script for those HoI4 players that don't feel like they're
hearing the ear-caressing harmony of the naval invasion sound enough in
their games.

3rd party dependencies: PyAudio 0.2.14 by Hubert Pham

Hearts of Iron 4 and its associated trademarks are protected property of
Paradox Interactive AB, Sweden. This includes the sound file used
in this program, which is not used with the intention to infringe on
said copyright.

Credits to Reddit user u/Markilgrande for the idea.

Script by TheRagnaRoek aka Dennis Ragnar van Reem"""

import sys
import time
import wave
import random

import pyaudio


def random_time_intervall(min_time=5, max_time=120) -> int:
    """Randomizes a number between a given (min)imum and (max)imum.
    
    Used to randomly generate the intervalls between audio plays."""
    return random.randint(min_time, max_time)


def play_sound(file):
    """Plays a sound from the file of a given filepath (file)."""
    with wave.open(file, "rb") as wf:
        player = pyaudio.PyAudio()

        # open audio stream
        stream = player.open(
                    format=player.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True
                    )

        while len(data := wf.readframes(1024)):
            stream.write(data)

        stream.close()

        player.terminate()


if __name__ == "__main__":
    if len(sys.argv) < 2:  # without filepath, play naval invasion sound
        while True:
            play_sound("naval_invasion.wav")
            interval = random_time_intervall()
            time.sleep(interval)
    
    elif len(sys.argv) == 2:  # given filepath
        try:
            while True:
                play_sound(str(sys.argv[1]))
                interval = random_time_intervall()
                time.sleep(interval)
        except FileNotFoundError as fnf:
            print(f"Error: File not found.\n {fnf}")

    else:
        print(f"Too many arguments on command line. Usage in command line:\n \
              'python {sys.argv[0]} filepath'")
