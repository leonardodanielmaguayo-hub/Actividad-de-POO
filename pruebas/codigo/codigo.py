from enum import Enum
from datetime import datetime, timedelta

class EstadoStand(Enum):
    DISPONIBLE = "DISPONIBLE"
    RESERVADO = "RESERVADO"
    OCUPADO = "OCUPADO"
    BLOQUEADO = "BLOQUEADO"

class Stand:
    def __init__(self, id_stand: str, metros_cuadrados: float, costo_por_m2: float):
        self.id = id_stand
        self.metros_cuadrados = metros_cuadrados
        self.costo_por_m2 = costo_por_m2
        self.costo_total = metros_cuadrados * costo_por_m2
        self.estado = EstadoStand.DISPONIBLE

class Reserva:
    def __init__(self, stand: Stand, nombre_cliente: str, horas_limite: int = 24):
        self.stand = stand
        self.cliente = nombre_cliente
        self.fecha_reserva = datetime.now()
        self.fecha_limite = self.fecha_reserva + timedelta(hours=horas_limite)

class SistemaReservas:
    def __init__(self):
        # Diccionario para buscar stands rápidamente por su ID
        self.stands_registrados: dict[str, Stand] = {}
        self.reservas_activas: list[Reserva] = []

    def registrar_stand(self, stand: Stand):
        """Añade un stand al catálogo del sistema."""
        self.stands_registrados[stand.id] = stand

    def cambiar_estado_stand(self, id_stand: str, nuevo_estado: EstadoStand) -> Stand:
        """Cambia manualmente el estado de un stand registrado."""
        stand = self.stands_registrados.get(id_stand)

        if stand is None:
            raise ValueError(f"El stand {id_stand} no existe en el sistema.")

        stand.estado = nuevo_estado
        return stand

    def reservar_stand(self, id_stand: str, cliente: str, horas_limite: int = 24) -> Reserva:
        """Intenta reservar un stand específico validando su disponibilidad."""
        stand = self.stands_registrados.get(id_stand)

        if not stand:
            raise ValueError(f"El stand {id_stand} no existe en el sistema.")

        if stand.estado != EstadoStand.DISPONIBLE:
            raise ValueError(f"El stand {id_stand} ya se encuentra {stand.estado.value}.")

        # Cambiar el estado y generar la reserva
        stand.estado = EstadoStand.RESERVADO
        nueva_reserva = Reserva(stand, cliente, horas_limite)
        self.reservas_activas.append(nueva_reserva)
        
        print(f"Éxito: Stand {id_stand} reservado para {cliente}. Vence el {nueva_reserva.fecha_limite.strftime('%Y-%m-%d %H:%M:%S')}")
        return nueva_reserva


def mostrar_stands(sistema: SistemaReservas):
    """Muestra los stands registrados y su estado actual."""
    print("\nStands registrados:")
    for stand in sistema.stands_registrados.values():
        print(
            f"{stand.id}: {stand.metros_cuadrados} m², "
            f"${stand.costo_total:.2f}, estado: {stand.estado.value}"
        )


def iniciar_menu(sistema: SistemaReservas):
    """Permite consultar los stands y cambiar sus estados."""
    while True:
        print("\n--- Sistema de stands ---")
        print("1. Ver stands")
        print("2. Cambiar estado de un stand")
        print("3. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            mostrar_stands(sistema)
        elif opcion == "2":
            mostrar_stands(sistema)
            id_stand = input("\nEscribe el ID del stand que quieres cambiar: ").strip()
            estados = list(EstadoStand)

            print("\nElige el nuevo estado:")
            for numero, estado in enumerate(estados, start=1):
                print(f"{numero}. {estado.value}")

            seleccion = input("Opción: ").strip()
            if not seleccion.isdigit() or not 1 <= int(seleccion) <= len(estados):
                print("Opción de estado no válida.")
                continue

            nuevo_estado = estados[int(seleccion) - 1]
            try:
                sistema.cambiar_estado_stand(id_stand, nuevo_estado)
            except ValueError as error:
                print(error)
            else:
                print(f"El stand {id_stand} ahora está {nuevo_estado.value}.")
        elif opcion == "3":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida. Elige 1, 2 o 3.")


# --- Ejemplo de Uso ---
if __name__ == "__main__":
    sistema = SistemaReservas()

    # Tres stands de ejemplo, inicialmente disponibles
    sistema.registrar_stand(Stand(id_stand="A1", metros_cuadrados=10, costo_por_m2=500))
    sistema.registrar_stand(Stand(id_stand="A2", metros_cuadrados=15, costo_por_m2=500))
    sistema.registrar_stand(Stand(id_stand="B1", metros_cuadrados=20, costo_por_m2=450))

    iniciar_menu(sistema)
       