import unittest

from codigo.codigo import EstadoStand, SistemaReservas, Stand

class TestSistemaReservas(unittest.TestCase):
    
    def setUp(self):
        """Esta función se ejecuta antes de cada prueba para preparar un entorno limpio."""
        self.sistema = SistemaReservas()
        
        # Registramos un par de stands para las pruebas
        self.stand_1 = Stand(id_stand="A1", metros_cuadrados=10, costo_por_m2=500)
        self.stand_2 = Stand(id_stand="B1", metros_cuadrados=20, costo_por_m2=450)
        
        self.sistema.registrar_stand(self.stand_1)
        self.sistema.registrar_stand(self.stand_2)

    def test_reserva_falla_por_id_incorrecto(self):
        """Prueba que el sistema lanza un error si se pone un ID que no existe."""
        id_falso = "STAND_INEXISTENTE"
        
        # Validamos que se levante un ValueError al intentar reservar
        with self.assertRaises(ValueError) as contexto:
            self.sistema.reservar_stand(id_falso, "Cliente Prueba")
            
        # Validamos que el mensaje de error sea exactamente el esperado
        self.assertEqual(str(contexto.exception), f"El stand {id_falso} no existe en el sistema.")
        
        # Validamos que no se haya creado ninguna reserva activa
        self.assertEqual(len(self.sistema.reservas_activas), 0)

    def test_reserva_exitosa_por_id_correcto(self):
        """Prueba que el sistema permite escoger y reservar un stand con el ID correcto."""
        id_correcto = "A1"
        cliente = "Empresa Alpha"
        
        # Ejecutamos la reserva
        nueva_reserva = self.sistema.reservar_stand(id_correcto, cliente)
        
        # 1. Validamos que la reserva devuelta contenga los datos correctos
        self.assertIsNotNone(nueva_reserva)
        self.assertEqual(nueva_reserva.stand.id, id_correcto)
        self.assertEqual(nueva_reserva.cliente, cliente)
        
        # 2. Validamos que el estado del stand cambió a RESERVADO
        stand_reservado = self.sistema.stands_registrados[id_correcto]
        self.assertEqual(stand_reservado.estado, EstadoStand.RESERVADO)
        
        # 3. Validamos que la reserva se guardó en la lista del sistema
        self.assertIn(nueva_reserva, self.sistema.reservas_activas)
        self.assertEqual(len(self.sistema.reservas_activas), 1)

    def test_cambiar_estado_stand(self):
        """Prueba que se pueden asignar los cuatro estados a un stand."""
        for estado in EstadoStand:
            with self.subTest(estado=estado):
                stand_actualizado = self.sistema.cambiar_estado_stand("A1", estado)
                self.assertIs(stand_actualizado.estado, estado)

    def test_cambiar_estado_falla_por_id_incorrecto(self):
        """Prueba que no se puede cambiar el estado de un stand inexistente."""
        with self.assertRaisesRegex(
            ValueError, "El stand INEXISTENTE no existe en el sistema."
        ):
            self.sistema.cambiar_estado_stand("INEXISTENTE", EstadoStand.BLOQUEADO)

if __name__ == "__main__":
    # Esto ejecuta las pruebas
    unittest.main()
    