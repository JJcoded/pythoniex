import os
import time
import random
import ctypes
import winsound
import webbrowser
import pyautogui

# Wait 10 seconds before starting (suspense)
time.sleep(10)

# Scary sound effects (whispers, beeps, eerie tones)
def play_sounds():
    sound_options = [
        lambda: winsound.Beep(random.randint(200, 800), random.randint(500, 2000)),  # Creepy low-frequency beeps
        lambda: os.system('start /min mshta vbscript:Execute("CreateObject(\"SAPI.SpVoice\").Speak \"Can you hear me?\"(window.close)")'),  # Whispering voice
        lambda: os.system('start /min mshta vbscript:Execute("CreateObject(\"SAPI.SpVoice\").Speak \"Why are you still here?\"(window.close)")'),  # More creepy whispers
        lambda: os.system('start /min mshta vbscript:Execute("CreateObject(\"SAPI.SpVoice\").Speak \"I see you.\"(window.close)")'),  # Horror movie vibes
    ]
    random.choice(sound_options)()

# Fake system failure popups
def fake_errors():
    messages = [
        "Unknown Process Detected: Cannot Terminate.",
        "Warning: Memory Integrity Compromised.",
        "Critical System Error: Instability Detected.",
        "A Fatal Error Has Occurred. Press OK to Continue.",
        "Unexpected I/O Exception: Please Check Your Disk."
    ]
    ctypes.windll.user32.MessageBoxW(0, random.choice(messages), "SYSTEM FAILURE", 0x10)

# Open random horrifying websites
def open_horror_sites():
    sites = [
        "https://www.youtube.com/watch?v=2v_0AEP9iX0",  # Distorted creepy video
        "https://en.wikipedia.org/wiki/List_of_unexplained_sounds",  # Unexplained noises from space
        "https://www.reddit.com/r/LetsNotMeet/",  # True horror encounters
        "https://www.reddit.com/r/UnresolvedMysteries/",  # Unexplained disappearances
        "https://www.scpwiki.com/random:random-tale",  # SCP horror stories
    ]
    webbrowser.open(random.choice(sites))

# Keyboard and mouse glitches
def keyboard_mouse_glitch():
    actions = [
        lambda: pyautogui.moveRel(random.randint(-300, 300), random.randint(-300, 300), duration=1),  # Mouse drifts randomly
        lambda: pyautogui.press(random.choice(['esc', 'tab', 'capslock', 'f12'])),  # Random keypress
        lambda: pyautogui.write("Hello?", interval=0.1),  # Mysterious typing effect
    ]
    random.choice(actions)()

# Screen flashing effect
def screen_glitch():
    os.system("powershell -Command \"(Get-Process -Id $PID).MainWindowHandle | ForEach-Object {Add-Type -TypeDefinition 'using System; using System.Runtime.InteropServices; public class WinAPI { [DllImport(\\\"user32.dll\\\")] public static extern int FlashWindowEx(IntPtr hwnd, ref FLASHWINFO pwfi); } public struct FLASHWINFO { public uint cbSize; public IntPtr hwnd; public uint dwFlags; public uint uCount; public uint dwTimeout; }' -Language CSharp; $fw = New-Object FLASHWINFO; $fw.cbSize = [System.Runtime.InteropServices.Marshal]::SizeOf($fw); $fw.hwnd = $_; $fw.dwFlags = 3; $fw.uCount = 10; $fw.dwTimeout = 0; [WinAPI]::FlashWindowEx([ref]$fw)}\"")

# Loop the horror effects at random times
while True:
    time.sleep(random.randint(20, 60))  # Random intervals between 20s-60s
    random.choice([
        play_sounds,
        fake_errors,
        open_horror_sites,
        keyboard_mouse_glitch,
        screen_glitch
    ])()
