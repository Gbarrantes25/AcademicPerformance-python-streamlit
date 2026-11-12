# 🎓 Academic Performance Dashboard

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-1.0-blue.svg)]()

---

## 📋 Tabla de Contenidos

- [Descripción General](#-descripción-general)
- [Características Principales](#-características-principales)
- [Contenido del Proyecto](#-contenido-del-proyecto)
- [Herramientas y Tecnologías](#️-herramientas-y-tecnologías-utilizadas)
- [Configuración del Entorno](#️-configuración-del-entorno)
- [Estructura del Repositorio](#-estructura-del-repositorio)
- [Funcionalidades y Código Clave](#-funcionalidades-y-código-clave)
- [Vistas Previas](#️-vistas-previas-del-proyecto)
- [Autor](#-autor)
- [Licencia](#-licencia)

---

## 📃 Descripción General

Proyecto de análisis y visualización de **Rendimiento Académico** desarrollado en **Python** con **Streamlit**, diseñado para explorar el desempeño de alumnos por curso, aula y periodo de manera interactiva. Este proyecto transforma un modelo de datos dimensional (calendario, alumnos, cursos y notas) en un dashboard visual y estadístico mediante:

- 📊 **Modelo Dimensional:** Tablas de dimensión y hechos generadas y relacionadas por claves foráneas.
- 🧹 **Limpieza de Datos:** Tratamiento automático de valores nulos y normalización de columnas.
- 📈 **Agrupaciones y Pivotes:** Cálculo de promedios por curso, por alumno y generación de tablas pivote.
- 🎨 **Visualizaciones Estadísticas:** Histograma, boxplot, violinplot, heatmap, lineplot, barplot, regplot y countplot.
- 🖱️ **Filtros Interactivos Optimizados:** Multiselectores por aula con actualización aislada de componentes mediante `st.fragment`.

---

## ✨ Características Principales

### 🔄 Procesamiento de Datos con Pandas
- Generación de datos sintéticos reproducibles utilizando semilla fija (`np.random.seed`).
- Creación de un modelo estrella (Star Schema) con tablas de Calendario, Alumnos, Cursos y Hechos (Notas).
- Operaciones avanzadas de `merge`, `groupby` y `pivot_table` para el análisis agregado.

### 🚀 Optimización de Rendimiento en Streamlit
- Uso de `@st.cache_data` para evitar recalcular la generación y combinación de datos en cada interacción del usuario.
- Implementación de `@st.fragment` para que los gráficos con filtros se actualicen de forma aislada, sin recargar todo el dashboard, mejorando la experiencia de usuario (UX).

### 🎨 Diseño Interactivo y Documentado
- Navegación fluida entre secciones de análisis.
- Documentación embebida: cada sección del dashboard muestra su propio código fuente en tiempo real utilizando `inspect.getsource()`, ideal para fines educativos.

---

## 📊 Contenido del Proyecto

| Sección | Descripción | Contenido Principal |
|--------|-------------|---------------------|
| **Modelo de Datos** | Estructura base | Tablas de dimensión (Calendario, Alumnos, Cursos) y tabla de hechos (Notas) relacionadas por ID. |
| **Limpieza de Datos** | Preprocesamiento | Imputación de valores nulos, tipado de datos y renombrado de columnas para estandarización. |
| **Agrupaciones y Pivotes** | Análisis agregado | Promedios de notas por curso, por alumno y tabla pivote cruzada Alumno x Curso. |
| **Visualizaciones (6-12)** | Gráficos estadísticos | Distribución de notas, comparativos por curso, mapa de calor, evolución temporal, ranking, relación nota-edad y tasa de aprobados vs. desaprobados. |

---

## 🛠️ Herramientas y Tecnologías Utilizadas

### Software y Lenguajes
- **Python 3.10+** - Lenguaje de programación principal.
- **Streamlit** - Framework para el desarrollo del dashboard interactivo web.

### Librerías Principales
- 🐼 **Pandas** y **NumPy** - Manipulación, transformación y generación de datos sintéticos.
- 📊 **Matplotlib** y **Seaborn** - Visualización estadística avanzada y gráficos estéticos.

### Fuente de Datos
- 📄 **Datos Sintéticos:** Generados internamente mediante scripts de Python con `np.random.seed` para garantizar la reproducibilidad del análisis sin depender de archivos externos.

---

## ⚙️ Configuración del Entorno

### Prerequisitos
1. Tener instalado **Python 3.10** o superior.
2. Tener instalado `pip` o el gestor de paquetes `uv`.

### Paso 1: Clonar el Repositorio
```bash
git clone https://github.com/Gbarrantes25/AcademicPerformance-python-streamlit.git
cd AcademicPerformance-python-streamlit
```

### Paso 2: Instalar Dependencias
Opción A: Usando pip tradicional

```bash
pip install streamlit pandas numpy matplotlib seaborn
```

Opción B: Usando uv (recomendado por velocidad)

```bash
uv sync
```

### Paso 3: Ejecutar el Proyecto
Inicia el servidor local de Streamlit ejecutando el siguiente comando en la terminal:

```bash
streamlit run Analisis.py
```

El dashboard se abrirá automáticamente en tu navegador predeterminado en http://localhost:8501.

## 📂 Estructura del Repositorio

```
.
├── Analisis.py                # Script principal del dashboard en Streamlit
├── src/
│   └── mi_proyecto/
│       └── __init__.py        # Puerta de entrada y módulos del proyecto
├── .python-version            # Especificación de la versión de Python
├── pyproject.toml             # Configuración y gestión de dependencias del proyecto
├── uv.lock                    # Archivo de lock del gestor de paquetes uv
├── .gitignore                 # Archivo de configuración Git
└── README.md                  # Este archivo de documentación
```

## 💻 Funcionalidades y Código Clave
El proyecto aprovecha las características modernas de Streamlit para optimizar el rendimiento y la mantenibilidad.

###🚀 Caché de Datos (st.cache_data)

<details>
<summary>Ver implementación de caché</summary>

Evita que la generación y combinación de datos se ejecute en cada interacción, reduciendo drásticamente el tiempo de carga.

```python
import streamlit as st
import pandas as pd
import numpy as np

@st.cache_data
def cargar_y_procesar_datos():
    np.random.seed(42) # Reproducibilidad
    # ... lógica de generación de tablas dimensionales y de hechos ...
    df_notas = pd.merge(df_alumnos, df_cursos, on='id_curso')
    return df_notas

df = cargar_y_procesar_datos()
```

</details>

### ⚡ Actualización Aislada (st.fragment)

<details>
<summary>Ver implementación de fragmentos</summary>

Permite que un gráfico específico se actualice al cambiar su filtro (ej. aula), sin recargar el resto del dashboard.

```python
@st.fragment
def mostrar_grafico_aula(df):
    aulas = df['aula'].unique()
    aula_seleccionada = st.multiselect("Seleccionar Aula", aulas, default=[aulas[0]])
    
    df_filtrado = df[df['aula'].isin(aula_seleccionada)]
    
    # El gráfico solo se rerenderiza al cambiar el multiselect
    st.barplot(data=df_filtrado, x='curso', y='nota_promedio')
```
</details>

📖 Documentación Embebida (inspect.getsource)
<details>
<summary>Ver implementación de documentación</summary>

Muestra el código fuente de cada función directamente en la interfaz para fines educativos y de transparencia.

```python
import inspect

st.expander("Ver código fuente de esta sección").code(
    inspect.getsource(mostrar_grafico_aula)
)
```

</details>

## 🖼️ Vistas Previas del Proyecto
<details>
<summary>📸 Ver Capturas de Pantalla</summary>

<img width="1300" height="958" alt="image" src="https://github.com/user-attachments/assets/96720cad-fe68-40bf-ab9d-2361c6f01d62" />
<img width="1368" height="1079" alt="image" src="https://github.com/user-attachments/assets/6d58778a-c468-4f77-b680-8ee42cd5a99c" />
</details>

<details>
<summary>🎥 Ver Video Demostrativo</summary>

   
   Ver en YouTube: -
</details>

## 👤 Autor
Giancarlo Barrantes

Business Intelligence Developer | Power BI Specialist


<a href="https://www.linkedin.com/in/gb25"><img width="70" height="20" alt="image" src="https://github.com/user-attachments/assets/e0d69586-c6f9-4f66-9a3d-bc8dfa146463" /></a>
<a href="https://www.instagram.com/gbarrantes25"><img width="70" height="20" alt="image" src="https://github.com/user-attachments/assets/68773029-5e0f-49da-92e9-fb93a223dd09" />
</a>
<a href="https://www.tiktok.com/@gbarrantes25"><img width="65" height="20" alt="image" src="https://github.com/user-attachments/assets/349c87c0-1f3a-4368-8517-64a6012565c0" /></a>
<a href="https://www.youtube.com/@gbarrantes25"><img width="70" height="20" alt="image" src="https://github.com/user-attachments/assets/d9e2cb69-29ec-47fc-93ae-30896a7b533d" />
</a>

## 📝 Licencia
Este proyecto está bajo la Licencia MIT - ver el archivo <a href="https://mit-license.org/">LICENSE</a> para más detalles.
