from   fastapi import APIRouter
from utils.fatores import (
    media_exame_por_genero,
    media_exame_por_distancia_da_casa,
    media_exame_por_nivel_de_educacao_parental,
    media_exame_por_horas_estudadas,
    media_exame_por_frequencia,
    media_exame_por_env_parente,
    media_exame_por_acesso_recursos,
    media_exame_por_atividades_extras,
    media_exame_por_horas_sono,
    media_exame_por_notas_anteriores,
    media_exame_por_nivel_motivacao,
    media_exame_por_acesso_internet,
    media_exame_por_sessoes_reforco,
    media_exame_por_renda_familiar,
    media_exame_por_qualidade_professor,
    media_exame_por_tipo_escola,
    media_exame_por_influencia_colegas,
    media_exame_por_atividade_fisica,
    media_exame_por_dificuldades_aprendizado,
)
router = APIRouter(prefix="/fatores", tags=["fatores de performace"])

@router.get("/media-exame-por-genero")
def get_media_exame_genero():
    return media_exame_por_genero()

@router.get("/media-exame-por-distancia-da-casa")
def get_media_exame_por_distancia_da_casa():
    return media_exame_por_distancia_da_casa()

@router.get("/media-exame-por-nivel-de-educacao-parental")
def get_media_exame_por_nivel_de_educacao_parental():
    return media_exame_por_nivel_de_educacao_parental()

@router.get("/media-exame-por-horas-estudadas")
def media_exame_horas_estudadas():
    return media_exame_por_horas_estudadas()

@router.get("/media-exame-por-frequencia")
def media_exame_frequencia():
    return media_exame_por_frequencia()

@router.get("/media-exame-por-envolvimento-parental")
def media_exame_env_parental():
    return media_exame_por_env_parente()

@router.get("/media-exame-por-acesso-recursos")
def media_exame_acesso_recursos():
    return media_exame_por_acesso_recursos()

@router.get("/media-exame-por-atividades-extracurriculares")
def media_exame_atividades_extras():
    return media_exame_por_atividades_extras()

@router.get("/media-exame-por-horas-de-sono")
def media_exame_horas_sono():
    return media_exame_por_horas_sono()

@router.get("/media-exame-por-notas-anteriores")
def media_exame_notas_anteriores():
    return media_exame_por_notas_anteriores()

@router.get("/media-exame-por-nivel-de-motivacao")
def media_exame_nivel_motivacao():
    return media_exame_por_nivel_motivacao()

@router.get("/media-exame-por-acesso-a-internet")
def media_exame_acesso_internet():
    return media_exame_por_acesso_internet()

@router.get("/media-exame-por-sessoes-de-reforco")
def media_exame_sessoes_reforco():
    return media_exame_por_sessoes_reforco()

@router.get("/media-exame-por-renda-familiar")
def media_exame_renda_familiar():
    return media_exame_por_renda_familiar()

@router.get("/media-exame-por-qualidade-do-professor")
def media_exame_qualidade_professor():
    return media_exame_por_qualidade_professor()

@router.get("/media-exame-por-tipo-de-escola")
def media_exame_tipo_escola():
    return media_exame_por_tipo_escola()

@router.get("/media-exame-por-influencia-dos-colegas")
def media_exame_influencia_colegas():
    return media_exame_por_influencia_colegas()

@router.get("/media-exame-por-atividade-fisica")
def media_exame_atividade_fisica():
    return media_exame_por_atividade_fisica()

@router.get("/media-exame-por-dificuldades-de-aprendizado")
def media_exame_dificuldades_aprendizado():
    return media_exame_por_dificuldades_aprendizado()

