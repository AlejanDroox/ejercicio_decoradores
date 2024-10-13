# ejercicio_decoradores
 Un Ejercicio hecho por mi mismo para aprender un uso practico de los decoradores en python.

## Enunciado
 Desarrolla una API sencilla usando **FastAPI** en la que deberás implementar un decorador que controle la cantidad de veces que se puede ejecutar una función. La idea es simular una restricción de "limite de consultas".

### **Descripción del ejercicio:**

1. **Objetivo:** Crear una API donde una función decorada tenga un límite de ejecuciones permitido (por ejemplo, máximo 5 ejecuciones).
2. **Decorador:** Implementa un decorador llamado `limitar_ejecuciones` que limite la cantidad de veces que una función puede ser llamada.
3. **Librerías externas**: Debes usar **FastAPI** para crear la API. Usa también **asyncio** para simular tiempos de respuesta asíncronos.
4. **Endpoints**:
    - `/consultar`: Endpoint que simula la consulta de datos. Solo debe poder ejecutarse 5 veces.
    - `/reset`: Endpoint para resetear el contador de ejecuciones.

### **Requisitos:**
- El decorador debe ser reutilizable para otras funciones, no solo el endpoint `/consultar`.
- Implementa el manejo de errores (por ejemplo, cuando se alcanza el límite de ejecuciones).
- El código debe ser limpio y seguir buenas prácticas de FastAPI y Python.

### **Puntos a evaluar:**
- Implementación: ¿El decorador se utiliza correctamente y funciona como se espera?
- Limpieza del código: ¿El código es legible y sigue buenas prácticas?
- Lógica general del código: ¿La lógica del decorador y la API tiene sentido?

### **Puntuación:**
- Implementación: 1-100
- Limpieza del código: 1-100
- Lógica general del código: 1-100

