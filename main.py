import sys

from camara import Camara

if __name__ == "__main__":
    if len(sys.argv) <= 3:
        print("Ussage: python3 main.py <user> <password> <camera>")
        print("Cameras: ")
        print("1. Balcony")
        print("2. Garage")
        
    else:
        if sys.argv[3] == "Balcony" or sys.argv[3] == "Garage":
            print("[q] to quit")
            user = sys.argv[1]
            passwd = sys.argv[2]
            option = sys.argv[3]
            cam = Camara(user, passwd, option)
            cam.activarCamara()
        else:
            print("Bad option")
            print("Ussage: python3 main.py <option>")
            print("Cameras: ")
            print("1. Balcony")
            print("2. Garage")