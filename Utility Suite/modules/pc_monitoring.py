import time
import psutil
from pynput import keyboard

stop = False

def display_usage():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    net = psutil.net_io_counters()
    
    sent = net.bytes_sent / (1024**2)
    recv = net.bytes_recv / (1024**2)
    
    print(
        f"\n\rCPU: {cpu}% | RAM: {ram}% | DISK: {disk}% | NET: ↑{sent:.1f}MB ↓{recv:.1f}MB\n".ljust(90),
        end="",
        flush=True)
    
def display_usage_loop():
    print("\nClick 'ctrl' key to exit")
    while not stop:
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent
        disk = psutil.disk_usage("/").percent
        net = psutil.net_io_counters()
        
        sent = net.bytes_sent / (1024**2)
        recv = net.bytes_recv / (1024**2)
        
        print(
        f"\rCPU: {cpu}% | RAM: {ram}% | DISK: {disk}% | NET: ↑{sent:.1f}MB ↓{recv:.1f}MB".ljust(90),
        end="",
        flush=True)
        
        time.sleep(.1)

def key_pressed(key):
    global stop
    stop = False
    if key in (keyboard.Key.ctrl_l, keyboard.Key.ctrl_r):
        print("\nExiting..\n")
        stop = True
        print("---------------------------------------------------\nExited.\n")
        return False

def display_usage_loop_start():
    listener = keyboard.Listener(on_press=key_pressed)
    listener.start()
    display_usage_loop()
    listener.join()
    