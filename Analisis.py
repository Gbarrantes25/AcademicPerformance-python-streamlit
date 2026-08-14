import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st

st.header("Proyecto Análisis de Datos 💻", width="stretch", text_alignment="center")
st.markdown(
    """<p>El objetivo de este proyecto es elaborar un repositorio estructurado para el análisis del rendimiento académico y posterior visualización de datos.</p> <p>Librerías a usar: numpy, pandas, matplotlib, seaborn y streamlit.</p>
    <p>Cada salida estará acompañada de su código fuente.</p>
    """,
    unsafe_allow_html=True,
)
st.markdown("<h3>1. Tablas de Dimensión y Hechos</h3>", unsafe_allow_html=True)


fechas = np.arange("2024-01-01", "2026-08-01", dtype="<M8[M]")
df_dim_calendario = pd.DataFrame({"Fecha": fechas})
df_dim_calendario["Año"] = df_dim_calendario["Fecha"].dt.year
df_dim_calendario["Mes"] = df_dim_calendario["Fecha"].dt.month
df_dim_calendario["Id_Fecha"] = (
    df_dim_calendario["Año"].astype("str")
    + "-"
    + df_dim_calendario["Mes"].astype("str").str.zfill(2)
)

alumnos = [
    "Luis Quispe",
    "Alan Mercado",
    "Daniel Marquina",
    "Luisa Ramos",
    "Kars Rivera",
    "Elizabeth Flores",
    "Óscar Valdiviezo",
    "Ramón Villar",
    "María Pardo",
    "Verónica Torres",
    "Martha Linares",
    "Carlos Vargas",
    "Diego Ferreyros",
    "Isabel Mazza",
    "Antonia Llanos",
    "Fernando Cisneros",
    "Miguel Urrutia",
    "Ana Bazán",
    "Hugo Torne",
    "Gabriela Noriega",
]
edades = np.random.randint(6, 14, size=20)
df_dim_alumnos = pd.DataFrame(
    {
        "Alumnos": alumnos,
        "Id_Alumno": np.arange(1, len(alumnos) + 1),
        "Edad": edades,
        "Aula": np.random.choice(["101", "102", "201", "202"], size=len(alumnos)),
    }
)

cursos = [
    "Matemáticas",
    "Comunicaciones",
    "Música",
    "Arte y Cultura",
    "Ciencia y Ambiente",
    "Ed. Física",
    "Inglés",
    "Ciencia y Tecnología",
    "Personal Social",
    "Ed. Religiosa",
]
df_dim_cursos = pd.DataFrame(
    {"Curso": cursos, "Id_Curso": np.arange(1, len(cursos) + 1)}
)

df_fact_notas = pd.merge(
    df_dim_calendario["Id_Fecha"].drop_duplicates(),
    df_dim_alumnos["Id_Alumno"],
    how="cross",
)
df_fact_notas = pd.merge(df_fact_notas, df_dim_cursos["Id_Curso"], how="cross")
df_fact_notas["Id_Nota"] = np.arange(1, len(df_fact_notas["Id_Fecha"]) + 1)
df_fact_notas["Nota"] = np.clip(
    np.random.normal(loc=13.2, scale=3.4, size=len(df_fact_notas)), 3, 20
)
df_fact_notas.loc[df_fact_notas["Nota"] < 5, "Nota"] = np.nan
df_fact_notas.rename(columns={"Id_Curso": "IdCurs", "Id_Alumno": "Id_A"}, inplace=True)

with st.expander("Click para ver el contenido"):
    # Dimensión Calendario
    st.markdown("<h4>a. Dimensión Calendario</h4>", unsafe_allow_html=True)
    st.dataframe(df_dim_calendario, width="stretch")

    # Dimensión Alumno
    st.markdown("<h4>b. Dimensión Alumnos</h4>", unsafe_allow_html=True)
    st.dataframe(df_dim_alumnos, width="stretch")

    # Dimensión Cursos
    st.markdown("<h4>c. Dimensión Cursos</h4>", unsafe_allow_html=True)
    st.dataframe(df_dim_cursos, width="stretch")

    st.markdown(
        "<h4>d. Tabla de Hechos (primeros 20 registros)</h4>", unsafe_allow_html=True
    )
    st.dataframe(df_fact_notas, width="stretch")


st.markdown("<h3>2. Limpieza de Datos</h3>", unsafe_allow_html=True)
with st.expander("Click para ver contenido"):
    # Rellenando valores nulos por la nota mínima 5.
    df_fact_notas["Nota"] = df_fact_notas["Nota"].fillna(5)

    # Renombrando nombre de algunas columnas.
    df_fact_notas.rename(
        columns={"Id_A": "Id_Alumno", "IdCurs": "Id_Curso"}, inplace=True
    )

    st.code(
        """
        # Rellenando valores nulos por la nota mínima 5.
        df_fact_notas["Nota"] = df_fact_notas["Nota"].fillna(5)
        
        # Renombrando nombre de algunas columnas.
        df_fact_notas.rename(
            columns={"Id_A": "Id_Alumno", 
            "IdCurs": "Id_Curso"}, 
            inplace=True
        )
        """,
        language="python",
    )


st.markdown("<h3>3. Agrupaciones</h3>", unsafe_allow_html=True)
with st.expander("Click para ver el contenido"):
    st.markdown(
        "<h4>a. Agrupando y Promediando por Id_Curso</h4>", unsafe_allow_html=True
    )
    df_cursos_ag = df_fact_notas.groupby("Id_Curso").agg({"Nota": "mean"})
    st.code(
        """
        df_cursos_ag = df_fact_notas.groupby("Id_Curso")
                        .agg({"Nota": "mean"})
        """,
        language="python",
    )
    st.dataframe(df_cursos_ag)
    st.markdown(
        "<h4>b. Agrupando y Promediando por Id_Alumno e Id_Curso</h4>",
        unsafe_allow_html=True,
    )
    df_cursosalumnos_ag = df_fact_notas.groupby(["Id_Alumno", "Id_Curso"]).agg(
        {"Nota": "mean"}
    )
    st.code(
        """
        df_cursosalumnos_ag = df_fact_notas
                                .groupby(["Id_Alumno", "Id_Curso"])
                                .agg({"Nota": "mean"}
                            )
        """
    )
    st.dataframe(df_cursosalumnos_ag)

st.markdown("<h3>4. Join</h3>", unsafe_allow_html=True)
with st.expander("Click para ver el contenido"):
    df_merge = pd.merge(df_fact_notas, df_dim_alumnos, how="left").merge(
        df_dim_cursos, how="left"
    )
    st.code(
        """
        df_merge = pd.merge(df_fact_notas,df_dim_alumnos,how="left")
                            .merge(df_dim_cursos,how="left")
        """,
        language="python",
    )
    st.dataframe(df_merge)

st.markdown("<h3>5. Pivotando Datos</h3>", unsafe_allow_html=True)
with st.expander("Click para ver el contenido"):
    df_pivot = df_merge.pivot_table(
        index="Alumnos", columns=["Curso"], values="Nota", aggfunc="mean"
    )
    st.code(
        """
        df_pivot = df_merge.pivot_table(
                index="Alumnos", 
                columns=["Curso"], 
                values="Nota", 
                aggfunc="mean"
            )
        """,
        language="python",
    )
    st.dataframe(df_pivot)

st.markdown("<h3>6. Distribución de Notas (Histplot)</h3>", unsafe_allow_html=True)
with st.expander("Click para ver el contenido"):
    st.code(
        """
        aulas = sorted(df_merge["Aula"].unique().tolist())
        aulas_seleccionadas = st.multiselect(
            label="Selecciona Aula",
            options=aulas,
            default=aulas,
            key="Filtro_aulas_historgrama",
        )
        if aulas_seleccionadas:
            df_hist_filtrado = df_merge.loc[df_merge["Aula"]
                                .isin(aulas_seleccionadas)]
            fig, ax = plt.subplots(figsize=(8, 5))
            sns.histplot(df_hist_filtrado, 
                        x="Nota", 
                        bins=10, 
                        ax=ax, 
                        kde=True, 
                        color="blue")
            ax.set_title(
                "Distribución de Notas", 
                fontdict={"fontsize": 16, "fontweight": 600}
            )
            ax.set_ylabel("Cantidad", fontweight=600)
            ax.set_xlabel("Notas", fontweight=600)
            plt.tight_layout()
            st.pyplot(fig)
        else:
            st.warning("Selecciona al menos una opción")
        """,
        language="python",
    )
    aulas = sorted(df_merge["Aula"].unique().tolist())
    aulas_seleccionadas = st.multiselect(
        label="Selecciona Aula",
        options=aulas,
        default=aulas,
        key="Filtro_aulas_historgrama",
    )
    if aulas_seleccionadas:
        df_hist_filtrado = df_merge.loc[df_merge["Aula"].isin(aulas_seleccionadas)]
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.histplot(df_hist_filtrado, x="Nota", bins=10, ax=ax, kde=True, color="blue")
        ax.set_title(
            "Distribución de Notas", fontdict={"fontsize": 16, "fontweight": 800}
        )
        ax.set_ylabel("Cantidad", fontweight=700)
        ax.set_xlabel("Notas", fontweight=700)
        plt.tight_layout()
        st.pyplot(fig)
    else:
        st.warning("Selecciona al menos una opción")

st.markdown(
    "<h3>7. Comparativo de Notas por Curso (Boxplot & Violinplot)</h3>",
    unsafe_allow_html=True,
)
with st.expander("Click para ver el contenido"):
    st.code(
        """
        # Boxplot
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.boxplot(df_merge, 
                    x="Curso", 
                    y="Nota", 
                    ax=ax, 
                    color="steelblue")
        plt.xticks(rotation=60)
        ax.set_ylabel("Notas",fontweight=600)
        ax.set_xlabel("Cursos",fontweight=600)
        ax.set_title("Análisis de Notas por Curso", 
                    fontweight=600, 
                    fontsize=16)
        plt.tight_layout()
        st.pyplot(fig)

        # Violinplot
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.violinplot(df_merge, x="Curso", y="Nota", inner="quartile", color="steelblue")
        plt.xticks(rotation=60)
        ax.set_ylabel("Notas", fontweight=700)
        ax.set_xlabel("Cursos", fontweight=700)
        plt.tight_layout()
        st.pyplot(fig)
        """,
        language="python",
    )

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(df_merge, x="Curso", y="Nota", ax=ax, color="steelblue")
    plt.xticks(rotation=60)
    ax.set_ylabel("Notas", fontweight=700)
    ax.set_xlabel("Cursos", fontweight=700)
    ax.set_title("Análisis de Notas por Curso", fontweight=800, fontsize=16)
    plt.tight_layout()
    st.pyplot(fig)

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.violinplot(df_merge, x="Curso", y="Nota", inner="quartile", color="steelblue")
    plt.xticks(rotation=60)
    ax.set_ylabel("Notas", fontweight=700)
    ax.set_xlabel("Cursos", fontweight=700)
    plt.tight_layout()
    st.pyplot(fig)

st.markdown(
    "<h3>8. Mapa de Calor Alumno por Curso (Heatmap)</h3>", unsafe_allow_html=True
)
with st.expander("Click para ver el contenido"):
    st.code(
        """
        fig, ax = plt.subplots(figsize=(8, 8))
        sns.heatmap(df_pivot, 
                    ax=ax, 
                    cmap="RdYlGn", 
                    fmt=".1f", 
                    annot=True)
        ax.set_title("Mapa de calor (Alumnos por Curso)", 
                    fontweight=600, 
                    fontsize=16)
        ax.set_xlabel("Cursos",fontweight=600)
        ax.set_ylabel("Alumnos",fontweight=600)
        plt.tight_layout()
        st.pyplot(fig)
        """,
        language="python",
    )

    fig, ax = plt.subplots(figsize=(8, 8))
    sns.heatmap(df_pivot, ax=ax, cmap="RdYlGn", fmt=".1f", annot=True)
    ax.set_title("Mapa de calor (Alumnos por Curso)", fontweight=800, fontsize=16)
    ax.set_xlabel("Cursos", fontweight=700)
    ax.set_ylabel("Alumnos", fontweight=700)
    plt.tight_layout()
    st.pyplot(fig)

st.markdown("<h3>9. Evolución Temporal (Lineplot)</h3>", unsafe_allow_html=True)
with st.expander("Click para ver el contenido"):
    st.code(
        """
        aulas2 = sorted(df_merge["Aula"].unique().tolist())
        aulas_selecionadas2 = st.multiselect(
            "Seleciona Aula", 
            options=aulas2, 
            default=aulas2, 
            key="Filtro_aulas_line"
        )
        if aulas_selecionadas2:
            df_merge_filtrado = df_merge.loc[df_merge["Aula"]
                                .isin(aulas_selecionadas2)]
            df_tiempo = (
                df_merge_filtrado.groupby("Id_Fecha")
                                .agg({"Nota": "mean"})
                                .reset_index()
            )
            fig, ax = plt.subplots(figsize=(8, 5))
            sns.lineplot(df_tiempo, 
                        x="Id_Fecha", 
                        y="Nota")
            plt.xticks(rotation=90)
            ax.set_title("Tendencia de Notas", 
                        fontsize=16, 
                        fontweight=600)
            ax.set_xlabel("Fechas", 
                        fontweight=600)
            ax.set_ylabel("Notas", 
                        fontweight=600)
            plt.tight_layout()
            st.pyplot(fig)
        else:
            st.warning("Selecciona al menos una opción")
        """
    )
    aulas2 = sorted(df_merge["Aula"].unique().tolist())
    aulas_selecionadas2 = st.multiselect(
        "Seleciona Aula", options=aulas2, default=aulas2, key="Filtro_aulas_line"
    )
    if aulas_selecionadas2:
        df_merge_filtrado = df_merge.loc[df_merge["Aula"].isin(aulas_selecionadas2)]
        df_tiempo = (
            df_merge_filtrado.groupby("Id_Fecha").agg({"Nota": "mean"}).reset_index()
        )
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.lineplot(df_tiempo, x="Id_Fecha", y="Nota", ax=ax)
        plt.xticks(rotation=90)
        ax.set_title("Tendencia de Notas", fontsize=16, fontweight=800)
        ax.set_xlabel("Fechas", fontweight=700)
        ax.set_ylabel("Notas", fontweight=700)
        plt.tight_layout()
        st.pyplot(fig)
    else:
        st.warning("Selecciona al menos una opción")

st.markdown("<h3>10. Ranking (Barplot)</h3>", unsafe_allow_html=True)
with st.expander("Click para ver el contenido"):
    st.code(
        """
        df_ranking = (
            df_merge.groupby("Alumnos", sort=True)
                    .agg({"Nota": "mean"})
                    .sort_values(by="Nota", ascending=False)
                    .head(10)
                    )
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.barplot(df_ranking, 
                    orient="h", 
                    y="Alumnos", 
                    x="Nota", 
                    ax=ax, 
                    color="steelblue")
        ax.set_title("Top 10 Promedio Ponderado", 
                    fontsize=16, 
                    fontweight=800)
        x.set_xlabel("Notas", 
                    fontweight=700)
        ax.set_ylabel("Alumnos", 
                    fontweight=700)
        plt.tight_layout()
        st.pyplot(fig)
        """
    )
    df_ranking = (
        df_merge.groupby("Alumnos", sort=True)
        .agg({"Nota": "mean"})
        .sort_values(by="Nota", ascending=False)
        .head(10)
    )
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(df_ranking, orient="h", y="Alumnos", x="Nota", ax=ax, color="steelblue")
    ax.set_title("Top 10 Promedio Ponderado", fontsize=16, fontweight=800)
    ax.set_xlabel("Notas", fontweight=700)
    ax.set_ylabel("Alumnos", fontweight=700)
    plt.tight_layout()
    st.pyplot(fig)

st.markdown("<h3>11. Relación Nota vs Edad (Regplot)</h3>", unsafe_allow_html=True)
with st.expander("Click para ver el contenido"):
    st.code(
        """
        fig, ax = plt.subplots(figsize=(8, 5))
        df_regplot = (
            df_merge.groupby(["Alumnos", "Edad"])
                    .agg({"Nota": "mean"})
                    .reset_index()
        )

        sns.regplot(df_regplot, 
                    x="Nota", 
                    y="Edad", 
                    ax=ax, 
                    logx=True, 
                    color="steelblue")
        ax.set_title("Edad vs Nota", 
                    fontsize=16, 
                    fontweight=800)
        ax.set_xlabel("Notas", fontweight=700)
        ax.set_ylabel("Edad", fontweight=700)
        plt.tight_layout()
        st.pyplot(fig)
        """
    )
    fig, ax = plt.subplots(figsize=(8, 5))
    df_regplot = (
        df_merge.groupby(["Alumnos", "Edad"]).agg({"Nota": "mean"}).reset_index()
    )

    sns.regplot(df_regplot, x="Nota", y="Edad", ax=ax, logx=True, color="steelblue")
    ax.set_title("Edad vs Nota", fontsize=16, fontweight=800)
    ax.set_xlabel("Notas", fontweight=700)
    ax.set_ylabel("Edad", fontweight=700)
    plt.tight_layout()
    st.pyplot(fig)

st.markdown(
    "<h3>12. Aprobados vs Desaprobados (Countplot)</h3>", unsafe_allow_html=True
)
with st.expander("Click para ver el contenido"):
    st.code(
        """
        df_merge["Estado"] = np.where(df_merge["Nota"] >= 13, 
                        "Aprobado", 
                        "Desaprobado")
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.countplot(df_merge, 
                        x="Curso", 
                        hue="Estado", 
                        ax=ax)
        plt.xticks(rotation=60)
        plt.tight_layout()
        ax.set_title("Aprobados vs Desaprobados", 
                        fontsize=16, 
                        fontweight=800)
        ax.set_xlabel("Cursos", 
                        fontweight=700)
        ax.set_ylabel("Conteo", 
                        fontweight=700)
        st.pyplot(fig)
        """
    )
    df_merge["Estado"] = np.where(df_merge["Nota"] >= 13, "Aprobado", "Desaprobado")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.countplot(df_merge, x="Curso", hue="Estado", ax=ax)
    plt.xticks(rotation=60)
    plt.tight_layout()
    ax.set_title("Aprobados vs Desaprobados", fontsize=16, fontweight=800)
    ax.set_xlabel("Cursos", fontweight=700)
    ax.set_ylabel("Conteo", fontweight=700)
    st.pyplot(fig)
