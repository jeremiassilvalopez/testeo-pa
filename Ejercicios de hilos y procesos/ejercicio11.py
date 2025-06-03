import threading
import time
import random

class ImpresoraCompartida:
    def __init__(self):
        self.lock = threading.Lock()

    def imprimir(self, usuario, documento):
        print(f"{usuario} está esperando para imprimir {documento}")
        with self.lock:
            print(f"{usuario} está imprimiendo {documento}")
            try:
                duracion = random.uniform(0, 5)  # corregido: random.uniform
                time.sleep(duracion)
                if random.random() < 0.3:
                    raise Exception("Error de impresión")
                print(f"{usuario} terminó de imprimir {documento}")
            except Exception as e:
                print(f"Error al imprimir {documento} de {usuario}: {e}")

def usuario_impresion(impresora, usuario, documento):
    impresora.imprimir(usuario, documento)

if __name__ == "__main__":
    impresora = ImpresoraCompartida()
    usuarios = [("Usuario1", "DocumentoA"),
                ("Usuario2", "DocumentoB"),
                ("Usuario3", "DocumentoC"),
                ("Usuario4", "DocumentoD")]

    hilos = []
    for usuario, documento in usuarios:
        hilo = threading.Thread(target=usuario_impresion, args=(impresora, usuario, documento))
        hilos.append(hilo)
        hilo.start()

    for hilo in hilos:
        hilo.join()
