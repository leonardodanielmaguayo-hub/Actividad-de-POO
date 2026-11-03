Requisitos No Funcionales 

Tecnología Recomendada: Backend en Node.js (Express/Nest), Python (FastAPI/Django) o Java (Spring Boot) con una base de datos relacional (PostgreSQL o MySQL) para garantizar la consistencia en el estado de los pagos y transacciones (ACID).

Arquitectura Limpia y Simple: Separación clara entre Modelos de Datos (Entities) y Lógica de Negocio (Services).

Tareas Programadas (Scheduler): Para un sistema pequeño, no necesitas Kafka o RabbitMQ. Un simple Cron Job (ej. node-cron o Celery/APScheduler en Python) que corra cada hora es suficiente para verificar las fechas y disparar el patrón Observer.

Escalabilidad del Código: El uso del Patrón Observer permite agregar nuevos canales de notificación (Email, SMS, WhatsApp) en el futuro sin modificar la lógica principal.