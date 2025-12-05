from fastapi import APIRouter

router=APIRouter(
    prefix="/example"
)

@router.get("/test/{test_id}")
def read(test_id:int):
    return {"Hello World Testing id is {test_id}".format(test_id=test_id)}

@router.get("/sample")
def sample():
    return {"Sample Endpoint"}