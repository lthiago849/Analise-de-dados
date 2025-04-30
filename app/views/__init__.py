from fastapi import APIRouter
from views.fatores import router as fatores
from views.desempenho import router as desempenho

router= APIRouter()
router.include_router(fatores)
router.include_router(desempenho)