import multiprocessing
import threading
import time
import random

def cliente(cuenta, lock, log, cliente_id):
    try:
        for _ in range(5):  # Cada cliente realiza 5 operaciones
            operacion = random.choice(['deposito', 'extraccion'])
            monto = random.randint(10, 100)
            with lock:
                saldo_actual = cuenta.value
                if operacion == 'deposito':
                    cuenta.value += monto
                    log.append(f"Cliente {cliente_id}: Depositó ${monto}. Saldo: ${cuenta.value}")
                elif operacion == 'extraccion':
                    if saldo_actual >= monto:
                        cuenta.value -= monto
                        log.append(f"Cliente {cliente_id}: Extrajo ${monto}. Saldo: ${cuenta.value}")
                    else:
                        raise Exception(f"Cliente {cliente_id}: Fondos insuficientes para extraer ${monto}. Saldo: ${saldo_actual}")
            time.sleep(random.uniform(0.1, 0.5))  # Simula tiempo de operación
    except Exception as e:
        log.append(str(e))

def cajero(cuenta, lock, log, cajero_id, num_clientes):
    hilos = []
    for i in range(num_clientes):
        cliente_id = f"{cajero_id}-{i}"
        hilo = threading.Thread(target=cliente, args=(cuenta, lock, log, cliente_id))
        hilos.append(hilo)
        hilo.start()
    for hilo in hilos:
        hilo.join()

if __name__ == "__main__":
    manager = multiprocessing.Manager()
    cuenta = manager.Value('i', 1000)  # Saldo inicial de $1000
    lock = manager.Lock()
    log = manager.list()

    procesos = []
    num_cajeros = 3
    clientes_por_cajero = 5

    for i in range(num_cajeros):
        p = multiprocessing.Process(target=cajero, args=(cuenta, lock, log, i, clientes_por_cajero))
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()

    print("\nRegistro de operaciones:")
    for entrada in log:
        print(entrada)

    print(f"\nSaldo final: ${cuenta.value}")
