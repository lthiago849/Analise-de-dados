from fastapi import APIRouter
from utils.desempenho import (
    media_notas_por_genero,
    media_notas_por_raca_etnia,
    media_notas_por_nivel_educacional_parental,
    media_notas_por_tipo_alimentacao,
    media_notas_por_curso_preparacao_teste
)

router = APIRouter(prefix="/desempenho", tags=["desempenho dos alunos"])

@router.get("/desempenho-aluno-por-genero")
def get_media_notas_por_genero():
    return media_notas_por_genero()

@router.get("/desempenho-aluno-por-raca-etnia")
def get_media_notas_por_raca_etnia():
    return media_notas_por_raca_etnia()

@router.get("/desempenho-aluno-por-nivel-educacional-parental")
def get_media_notas_por_nivel_educacional_parental():
    return media_notas_por_nivel_educacional_parental()

@router.get("/desempenho-aluno-por-tipo-alimentacao")
def get_media_notas_por_tipo_alimentacao():
    return media_notas_por_tipo_alimentacao()

@router.get("/desempenho-aluno-por-curso-preparacao-teste")
def get_media_notas_por_curso_preparacao_teste():
    return media_notas_por_curso_preparacao_teste()
