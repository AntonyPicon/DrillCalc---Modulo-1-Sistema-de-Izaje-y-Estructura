# DrillCalc - Modulo 1: Sistema de Izaje y Estructura

**Autor:** Antony Picon, Ingeniero Mecánico.
**Normativa:** API Spec 4F / API Spec 9B.
**Repositorio:** [https://github.com/AntonyPicon/DrillCalc---Modulo-1-Sistema-de-Izaje-y-Estructura.git](https://github.com/AntonyPicon/DrillCalc---Modulo-1-Sistema-de-Izaje-y-Estructura.git)

## Descripción
DrillCalc es una herramienta modular diseñada para el cálculo y verificación de parámetros críticos en el Sistema de Izaje y la Estructura de taladros de perforación. Este primer módulo se enfoca en la eficiencia del sistema, tensiones en las líneas (rápida/muerta), carga en la torre y factores de diseño.

## Características
- **Backend Robusto**: Implementado en Python con FastAPI, siguiendo patrones de arquitectura limpia y separación de lógica de negocio (Service Layer).
- **Frontend Industrial**: Interfaz web moderna (Dark Mode) con visualización de alertas de seguridad basadas en rangos técnicos (Verde/Amarillo/Rojo).
- **Validación Rigurosa**: Modelos de datos validados con Pydantic y lógica de ingeniería verificada mediante pruebas unitarias.

## Requisitos
- Python 3.10 o superior.
- Navegador web moderno (Chrome, Edge, Firefox).

## Instalación y Ejecución

### 1. Preparar el Entorno
```bash
# Clone the repository
git clone https://github.com/AntonyPicon/DrillCalc---Modulo-1-Sistema-de-Izaje-y-Estructura.git
cd DrillCalc---Modulo-1-Sistema-de-Izaje-y-Estructura

# Crear entorno virtual
python -m venv venv

# Activar (Linux/Mac)
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### 2. Ejecutar el Servidor (Backend)
```bash
uvicorn backend.main:app --reload
```
La API estará disponible en `http://localhost:8000`. Puedes consultar la documentación interactiva en `/docs`.

### 3. Ejecutar la Interfaz (Frontend)
Simplemente abre el archivo `frontend/index.html` en tu navegador o sírvelo con una herramienta como `http.server`.

## Pruebas
Para ejecutar la suite de pruebas unitarias e integración:
```bash
PYTHONPATH=. pytest tests/
```

## Licencia
Este proyecto está bajo la Licencia **MIT**. Consulta el archivo [LICENSE](LICENSE) para más detalles.
