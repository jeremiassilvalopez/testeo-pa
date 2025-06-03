import threading
import time
import os
import random

saldo = 100
lock = threading.Lock()

def retirar(cantidad):
    global saldo
    with lock:
        if saldo >= cantidad:
            print(f"retirando {cantidad}")
            saldo -= cantidad
        print("saldo insuficiente")

hilos = []
for i in hilos: 
    hilo= threading.Thread(target=retirar, args=(15,))
    hilo.start()

for hilo in hilos:
    hilo.join()
   

print("Saldo final: ", saldo)
