import sys

from camera import Camera

if __name__ == "__main__":
    if len(sys.argv) <= 3:
        print("Ussage: python3 main.py <user> <password> <ip>")
    else:
        print("[q] to quit")
        user = sys.argv[1]
        passwd = sys.argv[2]
        ip = sys.argv[3]
        cam = Camera(user, passwd, ip)
        cam.turnOn()