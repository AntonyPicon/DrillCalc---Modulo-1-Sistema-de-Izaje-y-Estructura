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

## Detalle de las Herramientas

### 1. Sistema de Izaje (Hoisting System)
Esta herramienta permite evaluar la capacidad del cable de perforación y la estructura (torre) basándose en las cargas operativas.

**Parámetros de Entrada:**
- **Whook:** Carga total en el gancho (libras).
- **N:** Número de líneas instaladas entre el bloque corona y el bloque viajero.
- **S:** Número total de poleas en el sistema.
- **K:** Factor de fricción por polea (típicamente 1.04).
- **LBnom:** Resistencia nominal a la ruptura del cable seleccionado.

**Cálculos Realizados:**
- **Eficiencia ($\eta$):** Determina la pérdida de energía por fricción en las poleas.
  $$\eta = \frac{K^N - 1}{K^S \cdot N \cdot (K - 1)}$$
- **Tensión Línea Rápida ($F_{fast}$):** Tensión que soporta el cable en el malacate.
- **Carga en la Torre ($F_{derrick}$):** Carga total que soporta la subestructura y torre.
  $$F_{derrick} = W_{hook} + F_{fast} + F_{dead}$$
- **Factor de Diseño (FD):** Margen de seguridad del cable. Se recomienda $FD \ge 3.0$ para operaciones seguras.

---

### 2. Ton-Mile (Tonelada-Milla)
Calcula el trabajo mecánico acumulado realizado por el cable durante un viaje redondo (Round Trip) para determinar el momento óptimo de realizar el corte y corrimiento (Slip & Cut).

**Parámetros de Entrada:**
- **D (Profundidad):** Profundidad máxima alcanzada (pies).
- **L (Longitud Parada):** Longitud promedio de una parada (ej. 90 ft).
- **Wm (Peso Tubería):** Peso de la tubería de perforación ajustado por flotación (lbs/ft).
- **M (Peso Bloque):** Peso del bloque viajero y accesorios (lbs).
- **Wcm (Peso Lastrabarrenas):** Peso de los drill collars en lodo (lbs/ft).
- **Lc (Longitud Lastrabarrenas):** Longitud de la sección de drill collars (pies).

**Fórmula API RP 9B:**
$$T_R = \frac{D(L + D)W_m + 4D(M + 0.5C)}{10,560,000}$$
*Donde $C$ es el peso excedente de los lastrabarrenas sobre la tubería de perforación ($L_c \cdot (W_{cm} - W_m)$).*

---

## Pruebas
```bash
PYTHONPATH=. pytest tests/
```

## Licencia
Este proyecto está bajo la Licencia **MIT**.


