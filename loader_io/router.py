from fastapi import APIRouter

router = APIRouter()


@router.get('/loaderio-b870ca900bf56f434c0db90bf2f6961a/')
def loader_io():
    return 'loaderio-b870ca900bf56f434c0db90bf2f6961a'

