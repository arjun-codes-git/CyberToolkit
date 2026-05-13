# ULTIMATE CYBER TOOLKIT v2 (Safe + Educational)
# Features:
# - IP Lookup
# - Port Scanner
# - Password Strength Checker
# - Website Header Grabber
# - WHOIS Lookup
# - DNS Lookup
# - Ping Test
# - System Info
# - Hash Generator
# - File Encryptor
#
# Install:
# pip install requests colorama psutil cryptography pyfiglet python-whois

import socket
import requests
import hashlib
import platform
import os
import subprocess
import psutil
import whois
from cryptography.fernet import Fernet
from colorama import Fore, init
import pyfiglet

init(autoreset=True)

# =========================
# BANNER
# =========================
def banner():
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.CYAN + pyfiglet.figlet_format("CYBER TOOLKIT"))

# =========================
# IP LOOKUP
# =========================
def ip_lookup():
    target = input("Enter IP/Domain: ")

    try:
        data = requests.get(f"https://ipapi.co/{target}/json/").json()

        print(Fore.GREEN + "\n[ IP INFORMATION ]\n")

        for k, v in data.items():
            print(f"{k}: {v}")

    except:
        print(Fore.RED + "Lookup failed.")

# =========================
# PORT SCANNER
# =========================
def port_scanner():
    target = input("Target IP/Domain: ")

    print(Fore.YELLOW + "\nScanning ports...\n")

    ports = [20,21,22,23,25,53,80,110,135,139,143,443,445,8080]

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((target, port))

        if result == 0:
            print(Fore.GREEN + f"[OPEN] Port {port}")

        s.close()

# =========================
# PASSWORD CHECKER
# =========================
def password_checker():
    pwd = input("Enter password: ")

    score = 0

    if len(pwd) >= 8:
        score += 1

    if any(c.isupper() for c in pwd):
        score += 1

    if any(c.isdigit() for c in pwd):
        score += 1

    if any(c in "!@#$%^&*" for c in pwd):
        score += 1

    print("\nPassword Strength:")

    if score == 4:
        print(Fore.GREEN + "VERY STRONG")

    elif score == 3:
        print(Fore.YELLOW + "STRONG")

    elif score == 2:
        print(Fore.MAGENTA + "MEDIUM")

    else:
        print(Fore.RED + "WEAK")

# =========================
# WEBSITE HEADERS
# =========================
def headers():
    url = input("Enter URL: ")

    try:
        r = requests.get(url)

        print(Fore.CYAN + "\n[ HEADERS ]\n")

        for k, v in r.headers.items():
            print(f"{k}: {v}")

    except:
        print(Fore.RED + "Could not fetch headers.")

# =========================
# WHOIS LOOKUP
# =========================
def whois_lookup():
    domain = input("Enter domain: ")

    try:
        info = whois.whois(domain)

        print(Fore.GREEN + "\n[ WHOIS INFO ]\n")

        print(info)

    except:
        print(Fore.RED + "WHOIS lookup failed.")

# =========================
# DNS LOOKUP
# =========================
def dns_lookup():
    domain = input("Enter domain: ")

    try:
        ip = socket.gethostbyname(domain)

        print(Fore.GREEN + f"\nIP Address: {ip}")

    except:
        print(Fore.RED + "DNS lookup failed.")

# =========================
# PING TEST
# =========================
def ping_test():
    target = input("Enter IP/Domain: ")

    param = "-n" if os.name == "nt" else "-c"

    command = ["ping", param, "4", target]

    subprocess.call(command)

# =========================
# SYSTEM INFO
# =========================
def system_info():
    print(Fore.CYAN + "\n[ SYSTEM INFO ]\n")

    print("OS:", platform.system())
    print("Release:", platform.release())
    print("CPU Cores:", psutil.cpu_count())
    print("RAM:", round(psutil.virtual_memory().total / (1024**3), 2), "GB")

# =========================
# HASH GENERATOR
# =========================
def hash_generator():
    text = input("Enter text: ")

    md5 = hashlib.md5(text.encode()).hexdigest()
    sha256 = hashlib.sha256(text.encode()).hexdigest()

    print(Fore.GREEN + "\nMD5 :", md5)
    print("SHA256 :", sha256)

# =========================
# FILE ENCRYPTOR
# =========================
def encrypt_file():
    file = input("Enter file path: ")

    try:
        key = Fernet.generate_key()

        with open("secret.key", "wb") as k:
            k.write(key)

        fernet = Fernet(key)

        with open(file, "rb") as f:
            data = f.read()

        encrypted = fernet.encrypt(data)

        with open(file + ".enc", "wb") as ef:
            ef.write(encrypted)

        print(Fore.GREEN + "\nFile encrypted.")
        print("Key saved as secret.key")

    except:
        print(Fore.RED + "Encryption failed.")

# =========================
# MENU
# =========================
def menu():

    while True:

        print(Fore.BLUE + """
[1] IP Lookup
[2] Port Scanner
[3] Password Checker
[4] Website Headers
[5] WHOIS Lookup
[6] DNS Lookup
[7] Ping Test
[8] System Info
[9] Hash Generator
[10] File Encryptor
[11] Exit
""")

        choice = input("Select: ")

        if choice == "1":
            ip_lookup()

        elif choice == "2":
            port_scanner()

        elif choice == "3":
            password_checker()

        elif choice == "4":
            headers()

        elif choice == "5":
            whois_lookup()

        elif choice == "6":
            dns_lookup()

        elif choice == "7":
            ping_test()

        elif choice == "8":
            system_info()

        elif choice == "9":
            hash_generator()

        elif choice == "10":
            encrypt_file()

        elif choice == "11":
            print(Fore.RED + "Goodbye.")
            break

        else:
            print(Fore.RED + "Invalid option.")

banner()
menu()