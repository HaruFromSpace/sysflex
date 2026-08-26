#!/usr/bin/env python3
# sysflex - because neofetch is too mainstream
# grabs basic system info and prints it with some art

import platform
import psutil
import argparse
import time
import os

# ascii art logo (keep it simple)
LOGO = [
    "   \\   /   ",
    "    .-.    ",
    " ― (   ) ― ",
    "    '-'    ",
    "   /   \\   "
]

# ansi color codes 
colors = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "magenta": "\033[95m",
    "cyan": "\033[96m",
    "reset": "\033[0m"
}

def get_size(bytes, suffix="B"):
    # convert bytes to something readable
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.1f} {unit}{suffix}"
        bytes /= factor

def fetch_info():
    # grab os info
    uname = platform.uname()
    os_name = f"{uname.system} {uname.release}"
    
    # cpu stuff
    # kinda hacky way to just get the processor name but whatever
    cpu = uname.processor
    
    # memory
    mem = psutil.virtual_memory()
    total_mem = get_size(mem.total)
    used_mem = get_size(mem.used)
    
    # disk
    try:
        disk = psutil.disk_usage('/')
        total_disk = get_size(disk.total)
        used_disk = get_size(disk.used)
    except:
        total_disk = "Unknown"
        used_disk = "Unknown"

    # uptime
    boot_time = psutil.boot_time()
    uptime_seconds = time.time() - boot_time
    hours = int(uptime_seconds // 3600)
    minutes = int((uptime_seconds % 3600) // 60)
    
    return [
        f"OS: {os_name}",
        f"CPU: {cpu}",
        f"RAM: {used_mem} / {total_mem}",
        f"Disk: {used_disk} / {total_disk}",
        f"Uptime: {hours}h {minutes}m"
    ]

def main():
    parser = argparse.ArgumentParser(description="fast minimal system info fetcher")
    parser.add_argument("-c", "--color", choices=["green", "blue", "cyan", "magenta", "yellow"], default="cyan", help="change output color")
    parser.add_argument("--no-art", action="store_true", help="run in stealth mode without ascii art")
    
    args = parser.parse_args()
    
    # windows needs this to run colors sometimes
    os.system('') 
    
    col = colors.get(args.color, colors["cyan"])
    res = colors["reset"]
    
    info = fetch_info()
    
    print("") # empty line for padding
    
    if args.no_art:
        # just print the info
        for line in info:
            print(f"{col}{line}{res}")
    else:
        # print logo alongside info
        for i in range(max(len(LOGO), len(info))):
            logo_line = LOGO[i] if i < len(LOGO) else " " * len(LOGO[0])
            info_line = info[i] if i < len(info) else ""
            
            # format it nice
            print(f"{col}{logo_line}    {res}{info_line}")
            
    print("")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nquit.")
