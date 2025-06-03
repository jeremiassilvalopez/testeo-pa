import threading
import time
from queue import Queue

# Crear una cola compartida
cola = Queue()

def productor():
    for i in range(1, 6):
        print(f"Productor: produciendo producto {i}")
        cola.put(i)#El productor coloca un producto en la cola.
        time.sleep(0.2)  # Simula el tiempo de producción
    cola.put(None)  # Señal de finalización
    print("Productor: producción finalizada")

def consumidor():
    while True:
        producto = cola.get()#El consumidor toma un producto de la cola. Si la cola está vacía, 
        #el hilo se bloquea hasta que haya un elemento disponible.
        if producto is None:
            print("Consumidor: no hay más productos. Finalizando.")
            break
        print(f"Consumidor: procesando producto {producto}")
        time.sleep(0.5)  # Simula el tiempo de procesamiento

# Crear y iniciar los hilos
hilo_productor = threading.Thread(target=productor)
hilo_consumidor = threading.Thread(target=consumidor)

hilo_productor.start()
hilo_consumidor.start()

hilo_productor.join()
hilo_consumidor.join()
