from typing import Union, Optional, List

import uvicorn
from fastapi import FastAPI, Cookie, Header, APIRouter, Path, Query, Depends
from pydantic import BaseModel, Field
from enum import Enum

# FastAPI详解,https://cloud.tencent.com/developer/article/2035986
# typing详解,https://www.jianshu.com/p/9b6b9a06cd3e
# pydantic详解,https://blog.csdn.net/codename_cys/article/details/107675748
"""
FastApi:starlette,pydantic
uvicorn,daphne,hypercorn 
"""
user_apirouter = APIRouter()  # 每一个应用对应一个APIRoutert，在run里面导入
app = FastAPI()
app.include_router(user_apirouter, prefix="/user", tags="用户相关接口")


# 使用ApiRouter
@user_apirouter.get("/list")
def user():
    pass


class Item(BaseModel):
    name: str
    price: float
    description: Optional[str] = None
    tax: Optional[bool] = None
    population: int = Field(default=100, title="人口数量", description="国家人口数量")


# 格式化 SQLALchemy定义的模型实例
# Item.from_orm(模型实例)
@app.get("/")
def read_root():
    return {"hello": "world"}


@app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
# 指定类型了,FastAPI会强制检查
# 联合类型Union[x,None]等价于可选类型Optional[x]
def read_item(item_id: int, q: Optional[str] = None):
    # q是url后?q=hello参数且为Optional选填
    return {"item_id": item_id, "q": q}


# 1.pydantic model的叫请求体
@app.post("/itmes/")
# async 改成异步
async def create_item(item: Item):
    return item


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


# 枚举路径
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


# 2.model_name路径参数
@app.get("/models/{model_name}")
# 指定model_name类型,FastAPI会强制检查类型
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "这是alexnet,Deep Learning FTW"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "这是lenet,LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}


# 3.查询参数
# http://127.0.0.1/items2/?skip=0&limit=10
@app.get("/items2/")
async def read_item2(skip: int = 0, limit: int = 10):
    fake_items_db = [{"item_name": "Foo"}, {"item_name": "Boo"}, {"item": "Doo"}]
    return fake_items_db[skip:limit]


# 4.查询参数字符串校验,使用query
@app.get("/queryparams/")
def query_params(
        value1: str = Query(..., min_length=8, max_length=20, regex="^a"),  # 长度在8-20,以a开头
        value2: List[int] = Query(default=["v1", "v2"], alias="别名")
):
    return value1, value2


# 5.路径参数数字校验,使用path来传递路径参数,使用Path来校验
@app.get("files/{file_path:path}")
def filepath(file_path: str = Path(None, title="路径参数", description="描述", ge=1, le=20)):
    return {"path": file_path}


# 6.cookie
@app.get("/cookies/")
async def read_cookie(ads_id: Union[str, None] = Cookie(default=None)):
    return {"ads_id": ads_id}


# 7.Header
@app.get("/headers/")
async def read_header(user_agent: Union[str, None] = Header(default=None)):
    return {"User-agent": user_agent}


# 8.response_model定义返回模型,对函数返回值进行过滤
class Re_model(BaseModel):
    name: str
    description: Union[str, None] = None


@app.post("/response_model/")
async def return_response(re_model: Re_model):
    return re_model


"""Dependencies 依赖的声名,创建,导入"""


# 1.函数作为依赖
async def common_parameters(q: Optional[str] = None, page: int = 1, limit: int = 10):
    return {"q": q, "page": page, "limit": limit}


@app.get("/dependencies01")
def dependencies01(commons: dict = Depends(common_parameters)):
    return commons


# 2.类作为依赖


"""
# 1.安装
pip install fastapi 
pip install "uvicorn[standard]"
# 2.启动
uvicorn fastapi_main:app --reload 
# 3.访问
http://127.0.0.1:8000/items/5?q=somequery
接口文档:http://127.0.0.1:8000/docs
接口文档:http://127.0.0.1:8000/redoc
        
# 4.pydantic,数据验证,用来做模型校验
"""

if __name__ == '__main__':
    uvicorn.run("fastapi_main:app", host="0.0.0.0", port=8000, reload=True, debug=True)
