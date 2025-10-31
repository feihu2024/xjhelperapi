from fastapi import APIRouter
from .user import router as user_router
from .member import router as member_router

router = APIRouter()
router.include_router(user_router)
router.include_router(member_router)  #会员管理