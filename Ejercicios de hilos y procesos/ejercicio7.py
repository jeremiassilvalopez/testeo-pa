import threading
import time

def lavar_platos():
    print("Hilo que se encarga de lavar los platos")
    time.sleep(3)  # Simula que tarda 3 segundos
    print("Hilo terminado")

def barrer_piso():
    print("Hilo que se encarga de  barrer el piso")
    time.sleep(2)  # Simula que tarda 2 segundos
    print("Hilo terminado")


def cocinar():
    print("hilo que se encarga de cocinar")
    time.sleep(5)  # Simula que tarda 5 segundos
    print("Hilo terminado")


# Crear los hilos
hilo_lavar = threading.Thread(target=lavar_platos)
hilo_barrer = threading.Thread(target=barrer_piso)
hilo_cocinar = threading.Thread(target=cocinar)

# Iniciar los hilos
hilo_lavar.start()
hilo_barrer.start()
hilo_cocinar.start()

# Esperar a que todos los hilos terminen
hilo_lavar.join()
hilo_barrer.join()
hilo_cocinar.join()

print(" Todas las tareas han sido completadas.")
