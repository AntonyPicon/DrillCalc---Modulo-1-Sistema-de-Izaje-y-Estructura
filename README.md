# DrillCalc - Modulo 1: Sistema de Izaje y Estructura

**Autor:** Antony Picon, Ingeniero Mecánico.
**Normativa:** API Spec 4F / API Spec 9B (RP 9B).
**Documentación Base:** [DESARROLLO DEL MÓDULO 1_ EL SISTEMA DE IZAJE Y LA ESTRUCTURA.pdf](DESARROLLO%20DEL%20MÓDULO%201_%20EL%20SISTEMA%20DE%20IZAJE%20Y%20LA%20ESTRUCTURA.pdf)
**Repositorio:** [https://github.com/AntonyPicon/DrillCalc---Modulo-1-Sistema-de-Izaje-y-Estructura.git](https://github.com/AntonyPicon/DrillCalc---Modulo-1-Sistema-de-Izaje-y-Estructura.git)

## Descripción
DrillCalc es una herramienta modular avanzada diseñada para el cálculo y verificación de parámetros críticos en el Sistema de Izaje y la Estructura de taladros de perforación. Este primer módulo integra el cálculo de eficiencia, tensiones en las líneas, carga en la torre y el cálculo de **Ton-Miles (Toneladas-Milla)**.

## Características
- **Backend Unificado**: Implementado con FastAPI, sirve tanto la lógica de ingeniería como los archivos estáticos de la interfaz.
- **Módulo de Ton-Mile**: Cálculo de trabajo acumulado (TR - Round Trip) basado en la norma API RP 9B.
- **Navegación Intuitiva**: Sidebar lateral para alternar entre el Sistema de Izaje y Ton-Mile.
- **Frontend Industrial**: Interfaz moderna (Dark Mode) con alertas visuales de seguridad (Verde/Amarillo/Rojo).

## Requisitos
- Python 3.10 o superior.
- Navegador web moderno.

## Instalación y Ejecución

### 1. Preparar el Entorno
```bash
# clonar el repositorio
git clone https://github.com/AntonyPicon/DrillCalc---Modulo-1-Sistema-de-Izaje-y-Estructura.git
cd DrillCalc---Modulo-1-Sistema-de-Izaje-y-Estructura

# Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Instalar dependencias
pip install -r requirements.txt
```

### 2. Ejecutar la Aplicación
```bash
python -m backend.main
```
Una vez iniciado el servidor, accede a:
👉 **[http://localhost:8000](http://localhost:8000)**

La documentación de la API está disponible en `http://localhost:8000/docs`.

## Pruebas
```bash
PYTHONPATH=. pytest tests/
```

## Licencia
Este proyecto está bajo la Licencia **MIT**.

