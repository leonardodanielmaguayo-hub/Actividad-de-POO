 Requisitos Funcionales 

Gestión de Stands: El sistema debe permitir registrar stands con su ID, metros cuadrados y costo por metro cuadrado.

Gestión de Estados: Un stand debe transitar entre los estados: DISPONIBLE, RESERVADO, OCUPADO y BLOQUEADO.

Cambio Manual de Estado: Un administrador debe poder seleccionar un stand y cambiar su estado a DISPONIBLE, RESERVADO, OCUPADO o BLOQUEADO.

Reglas de Reserva:

Al reservar, se define un tiempo límite de reserva. Si no se registra el pago mínimo antes de ese tiempo, el stand vuelve a DISPONIBLE.

Se debe definir un porcentaje mínimo de pago para que el stand pase automáticamente de RESERVADO a OCUPADO.

Pagos y Descuentos: El sistema debe registrar pagos. Si el pago total se hace antes de la "fecha de pronto pago", se aplicará un descuento configurado.

Notificaciones (Eventos): El sistema debe emitir alertas cuando:

La reserva está a punto de vencer.

El periodo de pronto pago está por terminar.

La fecha límite del pago total está por vencer