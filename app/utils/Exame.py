import pandas as pd
import matplotlib.pyplot as plt
import os

def media_exame_por_genero():
    df=pd.read_csv("database/FatoresDePerformanceEstudantis.csv")
    df.columns = df.columns.str.strip()
    medias= df.groupby("Gender")["Exam_Score"].mean().round(2).reset_index()
    medias.columns=["genero", "media_exame"]
    # criando grafico
    fig, ax = plt.subplots()
    medias.set_index("genero")["media_exame"].plot(kind="bar", color=["skyblue", "salmon"], ax=ax)
    ax.set_title("Média de Exame por Gênero")
    ax.set_ylabel("Média do Exame")
    ax.set_xlabel("Gênero")
    ax.set_ylim(0, 100)
    plt.tight_layout()
    
    # Salvando o grafico em static/
    caminho = "static/grafico_genero.png"
    os.makedirs("static", exist_ok=True)
    plt.savefig(caminho)
    plt.close()

    return {
        "generos": medias.to_dict(orient="records"),
        "grafico_url": caminho
    }
