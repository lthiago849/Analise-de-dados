import pandas as pd

def media_exame_por_genero():
    df=pd.read_csv("database/FatoresDePerformanceEstudantis.csv")
    df.columns = df.columns.str.strip()
    medias= df.groupby("Gender")["Exam_Score"].mean().round(2).reset_index()
    medias.columns=["genero", "media_exame"]
    return{"generos":medias.to_dict(orient="records")}

def media_exame_por_distancia_da_casa():
    df=pd.read_csv("database/FatoresDePerformanceEstudantis.csv")
    df.columns = df.columns.str.strip()
    medias= df.groupby("Distance_from_Home")["Exam_Score"].mean().round(2).reset_index()
    medias.columns=["distancia_da_casa", "media_exame"]
    return{"distancia_da_casa":medias.to_dict(orient="records")}

def media_exame_por_nivel_de_educacao_parental():
    df=pd.read_csv("database/FatoresDePerformanceEstudantis.csv")
    df.columns = df.columns.str.strip()
    medias= df.groupby("Parental_Education_Level")["Exam_Score"].mean().round(2).reset_index()
    medias.columns=["Parental_Education_Level", "media_exame"]
    return{"Nível de educação parental":medias.to_dict(orient="records")}

def media_exame_por_horas_estudadas():
    df = pd.read_csv("database/FatoresDePerformanceEstudantis.csv")
    df.columns = df.columns.str.strip()
    medias = df.groupby("Hours_Studied")["Exam_Score"].mean().round(2).reset_index()
    medias.columns = ["horas_estudadas", "media_exame"]
    return {"Horas estudadas": medias.to_dict(orient="records")}

def media_exame_por_frequencia():
    df = pd.read_csv("database/FatoresDePerformanceEstudantis.csv")
    df.columns = df.columns.str.strip()
    medias = df.groupby("Attendance")["Exam_Score"].mean().round(2).reset_index()
    medias.columns = ["frequencia", "media_exame"]
    return {"Frequência": medias.to_dict(orient="records")}

def media_exame_por_env_parente():
    df = pd.read_csv("database/FatoresDePerformanceEstudantis.csv")
    df.columns = df.columns.str.strip()
    medias = df.groupby("Parental_Involvement")["Exam_Score"].mean().round(2).reset_index()
    medias.columns = ["envolvimento_parental", "media_exame"]
    return {"Envolvimento parental": medias.to_dict(orient="records")}

def media_exame_por_acesso_recursos():
    df = pd.read_csv("database/FatoresDePerformanceEstudantis.csv")
    df.columns = df.columns.str.strip()
    medias = df.groupby("Access_to_Resources")["Exam_Score"].mean().round(2).reset_index()
    medias.columns = ["acesso_recursos", "media_exame"]
    return {"Acesso a recursos": medias.to_dict(orient="records")}

def media_exame_por_atividades_extras():
    df = pd.read_csv("database/FatoresDePerformanceEstudantis.csv")
    df.columns = df.columns.str.strip()
    medias = df.groupby("Extracurricular_Activities")["Exam_Score"].mean().round(2).reset_index()
    medias.columns = ["atividades_extracurriculares", "media_exame"]
    return {"Atividades extracurriculares": medias.to_dict(orient="records")}

def media_exame_por_horas_sono():
    df = pd.read_csv("database/FatoresDePerformanceEstudantis.csv")
    df.columns = df.columns.str.strip()
    medias = df.groupby("Sleep_Hours")["Exam_Score"].mean().round(2).reset_index()
    medias.columns = ["horas_sono", "media_exame"]
    return {"Horas de sono": medias.to_dict(orient="records")}

def media_exame_por_notas_anteriores():
    df = pd.read_csv("database/FatoresDePerformanceEstudantis.csv")
    df.columns = df.columns.str.strip()
    medias = df.groupby("Previous_Scores")["Exam_Score"].mean().round(2).reset_index()
    medias.columns = ["notas_anteriores", "media_exame"]
    return {"Notas anteriores": medias.to_dict(orient="records")}

def media_exame_por_nivel_motivacao():
    df = pd.read_csv("database/FatoresDePerformanceEstudantis.csv")
    df.columns = df.columns.str.strip()
    medias = df.groupby("Motivation_Level")["Exam_Score"].mean().round(2).reset_index()
    medias.columns = ["nivel_motivacao", "media_exame"]
    return {"Nível de motivação": medias.to_dict(orient="records")}

def media_exame_por_acesso_internet():
    df = pd.read_csv("database/FatoresDePerformanceEstudantis.csv")
    df.columns = df.columns.str.strip()
    medias = df.groupby("Internet_Access")["Exam_Score"].mean().round(2).reset_index()
    medias.columns = ["acesso_internet", "media_exame"]
    return {"Acesso à internet": medias.to_dict(orient="records")}

def media_exame_por_sessoes_reforco():
    df = pd.read_csv("database/FatoresDePerformanceEstudantis.csv")
    df.columns = df.columns.str.strip()
    medias = df.groupby("Tutoring_Sessions")["Exam_Score"].mean().round(2).reset_index()
    medias.columns = ["sessoes_reforco", "media_exame"]
    return {"Sessões de reforço": medias.to_dict(orient="records")}

def media_exame_por_renda_familiar():
    df = pd.read_csv("database/FatoresDePerformanceEstudantis.csv")
    df.columns = df.columns.str.strip()
    medias = df.groupby("Family_Income")["Exam_Score"].mean().round(2).reset_index()
    medias.columns = ["renda_familiar", "media_exame"]
    return {"Renda familiar": medias.to_dict(orient="records")}

def media_exame_por_qualidade_professor():
    df = pd.read_csv("database/FatoresDePerformanceEstudantis.csv")
    df.columns = df.columns.str.strip()
    medias = df.groupby("Teacher_Quality")["Exam_Score"].mean().round(2).reset_index()
    medias.columns = ["qualidade_professor", "media_exame"]
    return {"Qualidade do professor": medias.to_dict(orient="records")}

def media_exame_por_tipo_escola():
    df = pd.read_csv("database/FatoresDePerformanceEstudantis.csv")
    df.columns = df.columns.str.strip()
    medias = df.groupby("School_Type")["Exam_Score"].mean().round(2).reset_index()
    medias.columns = ["tipo_escola", "media_exame"]
    return {"Tipo de escola": medias.to_dict(orient="records")}

def media_exame_por_influencia_colegas():
    df = pd.read_csv("database/FatoresDePerformanceEstudantis.csv")
    df.columns = df.columns.str.strip()
    medias = df.groupby("Peer_Influence")["Exam_Score"].mean().round(2).reset_index()
    medias.columns = ["influencia_colegas", "media_exame"]
    return {"Influência dos colegas": medias.to_dict(orient="records")}

def media_exame_por_atividade_fisica():
    df = pd.read_csv("database/FatoresDePerformanceEstudantis.csv")
    df.columns = df.columns.str.strip()
    medias = df.groupby("Physical_Activity")["Exam_Score"].mean().round(2).reset_index()
    medias.columns = ["atividade_fisica", "media_exame"]
    return {"Atividade física": medias.to_dict(orient="records")}

def media_exame_por_dificuldades_aprendizado():
    df = pd.read_csv("database/FatoresDePerformanceEstudantis.csv")
    df.columns = df.columns.str.strip()
    medias = df.groupby("Learning_Disabilities")["Exam_Score"].mean().round(2).reset_index()
    medias.columns = ["dificuldades_aprendizado", "media_exame"]
    return {"Dificuldades de aprendizado": medias.to_dict(orient="records")}

