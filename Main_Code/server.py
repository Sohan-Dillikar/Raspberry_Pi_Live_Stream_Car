import RPi.GPIO as GPIO
from car import Car
import socket

msg_size = 64
port = 5050
#server_name = socket.gethostbyname(socket.gethostname())
server_name = "192.168.1.120"
addr = (server_name, port)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(addr)

def setup():
	global car
	GPIO.setmode(GPIO.BOARD)
	car = Car(((40, 38, 36), (15, 13, 11)), ((33, 35, 37), (12, 16, 18)))
	car.setup()

def loop():
	print(f"[LISTENING] Address : {server_name} | Port : {port}")
	server.listen()
	client, client_addr = server.accept()
	print(f"[CONNECTED] to {client_addr}")
	try:
		while True:
			msg = client.recv(msg_size).decode()
			if msg == "forward":
				car.forward()
			elif msg == "backward":
				car.backward()
			elif msg == "left":
				car.left()
			elif msg == "right":
				car.right()
			elif msg == "stop":
				car.stop()
	except KeyboardInterrupt:
		print("Quitting Server")
	finally:
		client.close()

if __name__ == "__main__":
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		print("Bye!")
	finally:
		GPIO.cleanup()
