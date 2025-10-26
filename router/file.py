from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
import datetime
import uuid
from pathlib import Path

from config import DIRS
from model.res.file import FileRes
from fastapi.exceptions import HTTPException
import io
import traceback
from PIL import Image, ImageDraw, ImageFont

router = APIRouter()


@router.post('/upload_file', response_model=FileRes)
async def upload_file(file: UploadFile = File(...)) -> FileRes:
    file_type = 'file'
    file_date = f'{datetime.date.today()}'
    file_name = f'{uuid.uuid1()}{Path(file.filename).suffix}'
    file_dir = Path(DIRS.assets_dir) / file_type / file_date
    file_dir.mkdir(parents=True, exist_ok=True)
    file_path = file_dir / file_name

    context = await file.read()
    #5M
    if len(context) > 1 * 1024 * 1024:
        raise HTTPException(400, "已超文件最大限制")

    with open(str(file_path), 'wb') as f:
        f.write(context)

    file_res = FileRes(
        file_type=file_type,
        file_date=file_date,
        file_name=file_name
    )
    return file_res

@router.post('/upload_video', response_model=FileRes)
async def upload_video(file: UploadFile = File(...)) -> FileRes:
    """视频上传，小于5M"""
    file_type = 'file'
    file_date = f'{datetime.date.today()}'
    file_name = f'{uuid.uuid1()}{Path(file.filename).suffix}'
    file_dir = Path(DIRS.assets_dir) / file_type / file_date
    file_dir.mkdir(parents=True, exist_ok=True)
    file_path = file_dir / file_name

    context = await file.read()
    #5M
    if len(context) > 5 * 1024 * 1024:
        raise HTTPException(400, "已超文件最大限制")

    with open(str(file_path), 'wb') as f:
        f.write(context)

    file_res = FileRes(
        file_type=file_type,
        file_date=file_date,
        file_name=file_name
    )
    return file_res

@router.post('/upload_cover_file', response_model=FileRes)
async def upload_cover_file(file: UploadFile = File(...)) -> FileRes:
    file_type = 'image'
    file_date = f'{datetime.date.today()}'
    file_name = f'{uuid.uuid1()}{Path(file.filename).suffix}'
    file_dir = Path(DIRS.assets_dir) / file_type / file_date
    file_dir.mkdir(parents=True, exist_ok=True)
    file_path = file_dir / file_name

    context = await file.read()
    #2M
    if len(context) > 2 * 1024 * 1024:
        raise HTTPException(400, "已超文件最大限制")

    try:
        stream = io.BytesIO(context)
        image_pil = Image.open(stream).convert('RGB').resize((300, 300))
        image_pil.save(str(file_path), format='jpeg', quality=100)
    except OSError:
        traceback.print_exc()
        raise HTTPException(400, "文件错误")

    # with open(str(file_path), 'wb') as f:
    #     f.write(context)

    file_res = FileRes(
        file_type=file_type,
        file_date=file_date,
        file_name=file_name
    )
    return file_res

@router.get('/{file_type}/{file_date}/{file_name}', response_class=FileResponse)
async def get_asset(file_type: str, file_date, file_name) -> str:
    return str(Path(DIRS.assets_dir).absolute() / file_type / file_date / file_name)
