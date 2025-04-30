import pandas as pd
import matplotlib.pyplot as plt
import os

def gerar_grafico(df, x_col, y_col, titulo, nome_arquivo, cor=None):
    fig, ax = plt.subplots()
    df.set_index(x_col)[y_col].plot(kind="bar", color=cor, ax=ax)
    ax.set_title(titulo)
    ax.set_ylabel("Média do Exame")
    ax.set_xlabel(x_col.replace("_", " ").capitalize())
    ax.set_ylim(0, 100)
    plt.tight_layout()
    os.makedirs("static", exist_ok=True)
    caminho = f"static/{nome_arquivo}.png"
    plt.savefig(caminho)
    plt.close()
    return caminho

def media_exame_por_genero():
    df = pd.read_csv("database/FatoresDePerformanceEstudantis.csv")
    df.columns = df.columns.str.strip()
    medias = df.groupby("Gender")["Exam_Score"].mean().round(2).reset_index()
    medias.columns = ["genero", "media_exame"]
    caminho = gerar_grafico(medias, "genero", "media_exame", "Média de Exame por Gênero", "grafico_genero", ["skyblue", "salmon"])
    return {
        "generos": medias.to_dict(orient="records"),
        "grafico_url": caminho
    }

def media_exame_por_distancia_da_casa():
    df = pd.read_csv("database/FatoresDePerformanceEstudantis.csv")
    df.columns = df.columns.str.strip()
    medias = df.groupby("Distance_from_Home")["Exam_Score"].mean().round(2).reset_index()
    medias.columns = ["distancia_da_casa", "media_exame"]
    caminho = gerar_grafico(medias, "distancia_da_casa", "media_exame", "Média por Distância de Casa", "grafico_distancia")
    return {
        "distancia_da_casa": medias.to_dict(orient="records"),
        "grafico_url": caminho
    }

def media_exame_por_nivel_de_educacao_parental():
    df = pd.read_csv("database/FatoresDePerformanceEstudantis.csv")
    df.columns = df.columns.str.strip()
    medias = df.groupby("Parental_Education_Level")["Exam_Score"].mean().round(2).reset_index()
    medias.columns = ["nivel_educacao_parental", "media_exame"]
    caminho = gerar_grafico(medias, "nivel_educacao_parental", "media_exame", "Média por Nível de Educação Parental", "grafico_educacao_parental")
    return {
        "nivel_educacao_parental": medias.to_dict(orient="records"),
        "grafico_url": caminho
    }

def media_exame_por_horas_estudadas():
    df = pd.read_csv("database/FatoresDePerformanceEstudantis.csv")
    df.columns = df.columns.str.strip()
    medias = df.groupby("Hours_Studied")["Exam_Score"].mean().round(2).reset_index()
    medias.columns = ["horas_estudadas", "media_exame"]
    caminho = gerar_grafico(medias, "horas_estudadas", "media_exame", "Média por Horas Estudadas", "grafico_horas_estudo")
    return {
        "horas_estudadas": medias.to_dict(orient="records"),
        "grafico_url": caminho
    }

def media_exame_por_frequencia():
    df = pd.read_csv("database/FatoresDePerformanceEstudantis.csv")
    df.columns = df.columns.str.strip()
    medias = df.groupby("Attendance")["Exam_Score"].mean().round(2).reset_index()
    medias.columns = ["frequencia", "media_exame"]
    caminho = gerar_grafico(medias, "frequencia", "media_exame", "Média por Frequência", "grafico_frequencia")
    return {
        "frequencia": medias.to_dict(orient="records"),
        "grafico_url": caminho
    }

def media_exame_por_env_parente():
    df = pd.read_csv("database/FatoresDePerformanceEstudantis.csv")
    df.columns = df.columns.str.strip()
    medias = df.groupby("Parental_Involvement")["Exam_Score"].mean().round(2).reset_index()
    medias.columns = ["envolvimento_parental", "media_exame"]
    caminho = gerar_grafico(medias, "envolvimento_parental", "media_exame", "Média por Envolvimento Parental", "grafico_env_parental")
    return {
        "envolvimento_parental": medias.to_dict(orient="records"),
        "grafico_url": caminho
    }

def media_exame_por_acesso_recursos():
    df = pd.read_csv("database/FatoresDePerformanceEstudantis.csv")
    df.columns = df.columns.str.strip()
    medias = df.groupby("Access_to_Resources")["Exam_Score"].mean().round(2).reset_index()
    medias.columns = ["acesso_recursos", "media_exame"]
    caminho = gerar_grafico(medias, "acesso_recursos", "media_exame", "Média por Acesso a Recursos", "grafico_acesso_recursos")
    return {
        "acesso_recursos": medias.to_dict(orient="records"),
        "grafico_url": caminho
    }

def media_exame_por_atividades_extras():
    df = pd.read_csv("database/FatoresDePerformanceEstudantis.csv")
    df.columns = df.columns.str.strip()
    medias = df.groupby("Extracurricular_Activities")["Exam_Score"].mean().round(2).reset_index()
    medias.columns = ["atividades_extracurriculares", "media_exame"]
    caminho = gerar_grafico(medias, "atividades_extracurriculares", "media_exame", "Média por Atividades Extracurriculares", "grafico_atividades")
    return {
        "atividades_extracurriculares": medias.to_dict(orient="records"),
        "grafico_url": caminho
    }

def media_exame_por_horas_sono():
    df = pd.read_csv("database/FatoresDePerformanceEstudantis.csv")
    df.columns = df.columns.str.strip()
    medias = df.groupby("Sleep_Hours")["Exam_Score"].mean().round(2).reset_index()
    medias.columns = ["horas_sono", "media_exame"]
    caminho = gerar_grafico(medias, "horas_sono", "media_exame", "Média por Horas de Sono", "grafico_sono")
    return {
        "horas_sono": medias.to_dict(orient="records"),
        "grafico_url": caminho
    }

def media_exame_por_notas_anteriores():
    df = pd.read_csv("database/FatoresDePerformanceEstudantis.csv")
    df.columns = df.columns.str.strip()
    medias = df.groupby("Previous_Scores")["Exam_Score"].mean().round(2).reset_index()
    medias.columns = ["notas_anteriores", "media_exame"]
    caminho = gerar_grafico(medias, "notas_anteriores", "media_exame", "Média por Notas Anteriores", "grafico_notas_anteriores")
    return {
        "notas_anteriores": medias.to_dict(orient="records"),
        "grafico_url": caminho
    }

def media_exame_por_nivel_motivacao():
    df = pd.read_csv("database/FatoresDePerformanceEstudantis.csv")
    df.columns = df.columns.str.strip()
    medias = df.groupby("Motivation_Level")["Exam_Score"].mean().round(2).reset_index()
    medias.columns = ["nivel_motivacao", "media_exame"]
    caminho = gerar_grafico(medias, "nivel_motivacao", "media_exame", "Média por Nível de Motivação", "grafico_motivacao")
    return {
        "nivel_motivacao": medias.to_dict(orient="records"),
        "grafico_url": caminho
    }

def media_exame_por_acesso_internet():
    df = pd.read_csv("database/FatoresDePerformanceEstudantis.csv")
    df.columns = df.columns.str.strip()
    medias = df.groupby("Internet_Access")["Exam_Score"].mean().round(2).reset_index()
    medias.columns = ["acesso_internet", "media_exame"]
    caminho = gerar_grafico(medias, "acesso_internet", "media_exame", "Média por Acesso à Internet", "grafico_internet")
    return {
        "acesso_internet": medias.to_dict(orient="records"),
        "grafico_url": caminho
    }

def media_exame_por_sessoes_reforco():
    df = pd.read_csv("database/FatoresDePerformanceEstudantis.csv")
    df.columns = df.columns.str.strip()
    medias = df.groupby("Tutoring_Sessions")["Exam_Score"].mean().round(2).reset_index()
    medias.columns = ["sessoes_reforco", "media_exame"]
    caminho = gerar_grafico(medias, "sessoes_reforco", "media_exame", "Média por Sessões de Reforço", "grafico_reforco")
    return {
        "sessoes_reforco": medias.to_dict(orient="records"),
        "grafico_url": caminho
    }

def media_exame_por_renda_familiar():
    df = pd.read_csv("database/FatoresDePerformanceEstudantis.csv")
    df.columns = df.columns.str.strip()
    medias = df.groupby("Family_Income")["Exam_Score"].mean().round(2).reset_index()
    medias.columns = ["renda_familiar", "media_exame"]
    caminho = gerar_grafico(medias, "renda_familiar", "media_exame", "Média por Renda Familiar", "grafico_renda")
    return {
        "renda_familiar": medias.to_dict(orient="records"),
        "grafico_url": caminho
    }

def media_exame_por_qualidade_professor():
    df = pd.read_csv("database/FatoresDePerformanceEstudantis.csv")
    df.columns = df.columns.str.strip()
    medias = df.groupby("Teacher_Quality")["Exam_Score"].mean().round(2).reset_index()
    medias.columns = ["qualidade_professor", "media_exame"]
    caminho = gerar_grafico(medias, "qualidade_professor", "media_exame", "Média por Qualidade do Professor", "grafico_professor")
    return {
        "qualidade_professor": medias.to_dict(orient="records"),
        "grafico_url": caminho
    }

def media_exame_por_tipo_escola():
    df = pd.read_csv("database/FatoresDePerformanceEstudantis.csv")
    df.columns = df.columns.str.strip()
    medias = df.groupby("School_Type")["Exam_Score"].mean().round(2).reset_index()
    medias.columns = ["tipo_escola", "media_exame"]
    caminho = gerar_grafico(medias, "tipo_escola", "media_exame", "Média por Tipo de Escola", "grafico_tipo_escola")
    return {
        "tipo_escola": medias.to_dict(orient="records"),
        "grafico_url": caminho
    }

def media_exame_por_influencia_colegas():
    df = pd.read_csv("database/FatoresDePerformanceEstudantis.csv")
    df.columns = df.columns.str.strip()
    medias = df.groupby("Peer_Influence")["Exam_Score"].mean().round(2).reset_index()
    medias.columns = ["influencia_colegas", "media_exame"]
    caminho = gerar_grafico(medias, "influencia_colegas", "media_exame", "Média por Influência dos Colegas", "grafico_colegas")
    return {
        "influencia_colegas": medias.to_dict(orient="records"),
        "grafico_url": caminho
    }

def media_exame_por_atividade_fisica():
    df = pd.read_csv("database/FatoresDePerformanceEstudantis.csv")
    df.columns = df.columns.str.strip()
    medias = df.groupby("Physical_Activity")["Exam_Score"].mean().round(2).reset_index()
    medias.columns = ["atividade_fisica", "media_exame"]
    caminho = gerar_grafico(medias, "atividade_fisica", "media_exame", "Média por Atividade Física", "grafico_fisica")
    return {
        "atividade_fisica": medias.to_dict(orient="records"),
        "grafico_url": caminho
    }

def media_exame_por_dificuldades_aprendizado():
    df = pd.read_csv("database/FatoresDePerformanceEstudantis.csv")
    df.columns = df.columns.str.strip()
    medias = df.groupby("Learning_Disabilities")["Exam_Score"].mean().round(2).reset_index()
    medias.columns = ["dificuldades_aprendizado", "media_exame"]
    caminho = gerar_grafico(medias, "dificuldades_aprendizado", "media_exame", "Média por Dificuldades de Aprendizado", "grafico_aprendizado")
    return {
        "dificuldades_aprendizado": medias.to_dict(orient="records"),
        "grafico_url": caminho
    }
