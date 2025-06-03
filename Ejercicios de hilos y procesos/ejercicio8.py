import threading
import time

# Saldo inicial de la cuenta
saldo = 100
# Lock para sincronizar el acceso al saldo
lock = threading.Lock()

def retirar_dinero(nombre_cajero):
    global saldo
    print(f"{nombre_cajero} intentando retirar $50...")
    with lock:
        print(f"{nombre_cajero} accede a la cuenta.")
        if saldo >= 50:
            print(f"{nombre_cajero} está procesando el retiro...")
            time.sleep(1)  # Simula el tiempo de procesamiento
            saldo -= 50
            print(f"{nombre_cajero} retiro exitoso. Saldo restante: ${saldo}")
        else:
            print(f"{nombre_cajero} fondos insuficientes. Saldo actual: ${saldo}")

# Crear hilos para los cajeros
cajeros = []
for i in range(1, 4):
    nombre = f"Cajero-{i}"
    hilo = threading.Thread(target=retirar_dinero, args=(nombre,))
    cajeros.append(hilo)
    hilo.start()

# Esperar a que todos los hilos terminen
for hilo in cajeros:
    hilo.join()
