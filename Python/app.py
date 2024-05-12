import speech_recognition as sr
import gpt
from gtts import gTTS
import os
import random
import pygame
import subprocess
import requests
from audiotoface_headless_request import call_api
import json

r = sr.Recognizer()
loading_speech_array = ["Let me contemplate that for a moment.", "I need a moment to think about it.", "I'll take a moment to reflect on that.", "I'll need some time to process that.", "Allow me a moment to weigh my options."]
call_gpt_times = 0
player_instance = ""

def play_sound(sound_file):
    pygame.init()
    pygame.mixer.init()
    # Set the mixer frequency to twice the default value.
    pygame.mixer.music.load(sound_file)
    #pygame.mixer.music.set_volume(0)
    pygame.mixer.music.play()

    # Wait for the playback to finish
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.quit()
    pygame.quit()

def init_speech():
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        transcript = r.recognize_google(audio)
        print(transcript)
        call_gpt(transcript)
        # transcript = r.recognize_azure(audio, key="", location="")
        # print(transcript[0])
        # call_gpt(transcript[0])
    except sr.UnknownValueError:
        print('Could not recognize speech')
        init_speech()
    except sr.TranscriptionFailed:
        text = "I am having trouble understanding what you said. Can you repeat the same please."
        text_to_speech(text)
        init_speech()
    except sr.WaitTimeoutError:
        text = "Due to some issue happended from my end, i am unable to understand what you just said. Can you please repeat the same?"
        text_to_speech(text)
        init_speech()
    except sr.RequestError as e:
        print('Could not request results from Speech Recognition service')
        init_speech()

def call_gpt(transcription_string):
    # global call_gpt_times
    # call_gpt_times = call_gpt_times + 1
    # if call_gpt_times > 3:
    #     randint = random.randint(0, len(loading_speech_array) - 1)
    #     text = loading_speech_array[randint]
    #     text_to_speech(text,should_start_listning=True)

    response = gpt.gpt_interface(transcription_string)
    print("\n")
    print(f"GPT: {response}")
    print("\n")
    transcription_array = []
    # Convert text to speech
    text_to_speech(response)

def text_to_speech(text, should_start_listning=True):
    # Initialize gTTS with the text to convert
    speech = gTTS(text, lang="en", slow=False)

    # Save the audio file to a temporary file
    speech_file = os.path.dirname(__file__) + '\speech.mp3'
    speech.save(speech_file)

    # Build the FFmpeg command
    command = ['ffmpeg', '-y', '-i', speech_file, 'output.wav']

    # Run the command using subprocess
    subprocess.call(command)
    
    audio_track = {
        "a2f_player": player_instance,
        "file_name": "output.wav"
    }
    call_api("http://localhost:8011/A2F/Player/SetTrack", "post", audio_track)

    audio_player_play = {
        "a2f_player": player_instance
    }
    call_api("http://localhost:8011/A2F/Player/Play", "post", audio_player_play)
    
    # Playing the converted file 
    play_sound(speech_file)
    print("Audio playback has ended.")
    if should_start_listning:
        init_speech()

def loading_speech():
    randint = random.randint(0, len(loading_speech_array) - 1)
    text = loading_speech_array[randint]
    text_to_speech(text)

def init_app():
    # global player_instance
    # #demo_fullface_claire.usda -> Female
    # #demo_fullface_mark.usda -> male
    audio_stage_data = {
        'file_name': 'D:/Omniverse/ov/pkg/audio2face-2023.1.1/exts/omni.audio2face.wizard/assets/demo_fullface_claire.usda'
    }
    call_api("http://localhost:8011/A2F/USD/Load", "post", audio_stage_data)

    player_instance = call_api("http://localhost:8011/A2F/Player/GetInstances", "get")
    player_instance = player_instance["result"]["regular"][0]
    print(player_instance)


    audio_path = {
        "a2f_player": player_instance,
        "dir_path": "D:/Projects/Python/Whisper/Whisper/"
    }
    call_api("http://localhost:8011/A2F/Player/SetRootPath", "post", audio_path)


    audio_track = {
        "a2f_player": player_instance,
        "file_name": "output.wav"
    }
    call_api("http://localhost:8011/A2F/Player/SetTrack", "post", audio_track)


    text = "Hello, May i know whom i am speaking with"
    text_to_speech(text)
    init_speech()
    print("Start Transcribing...")

if __name__ == "__main__":
    init_app()