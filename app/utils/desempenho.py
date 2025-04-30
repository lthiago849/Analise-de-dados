import pandas as pd

def media_notas_por_genero():
    df = pd.read_csv("database/PerformanceEstudantil.csv")
    df.columns = df.columns.str.strip()
    medias = df.groupby("gender")[["math score", "reading score", "writing score"]].mean().round(2).reset_index()
    medias.columns=["genero", "media_matematica", "media_leitura", "media_escrita"]
    return {"generos": medias.to_dict(orient="records")}

def media_notas_por_raca_etnia():
    df = pd.read_csv("database/PerformanceEstudantil.csv")
    df.columns = df.columns.str.strip()
    medias = df.groupby("race/ethnicity")[["math score", "reading score", "writing score"]].mean().round(2).reset_index()
    medias.columns = ["raca_etnia", "media_matematica", "media_leitura", "media_escrita"]
    return {"racas_etnias": medias.to_dict(orient="records")}

def media_notas_por_nivel_educacional_parental():
    df = pd.read_csv("database/PerformanceEstudantil.csv")
    df.columns = df.columns.str.strip()
    medias = df.groupby("parental level of education")[["math score", "reading score", "writing score"]].mean().round(2).reset_index()
    medias.columns = ["nivel_educacional_parental", "media_matematica", "media_leitura", "media_escrita"]
    return {"nivel_educacional_parental": medias.to_dict(orient="records")}

def media_notas_por_tipo_alimentacao():
    df = pd.read_csv("database/PerformanceEstudantil.csv")
    df.columns = df.columns.str.strip()
    medias = df.groupby("lunch")[["math score", "reading score", "writing score"]].mean().round(2).reset_index()
    medias.columns = ["tipo_alimentacao", "media_matematica", "media_leitura", "media_escrita"]
    return {"tipos_alimentacao": medias.to_dict(orient="records")}

def media_notas_por_curso_preparacao_teste():
    df = pd.read_csv("database/PerformanceEstudantil.csv")
    df.columns = df.columns.str.strip()
    medias = df.groupby("test preparation course")[["math score", "reading score", "writing score"]].mean().round(2).reset_index()
    medias.columns = ["curso_preparacao_teste", "media_matematica", "media_leitura", "media_escrita"]
    return {"cursos_preparacao_teste": medias.to_dict(orient="records")}
