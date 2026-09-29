from fastapi import FastAPI, HTTPException, Depends, Query
from pydantic import BaseModel, Field
from typing import Optional
import time

app = FastAPI(
    title="用户管理系统",
    description="用户 CRUD RESTful API",
    version="1.0.0",
)

# ===== 模拟数据库 =====
fake_db: dict[int, dict] = {}
next_id = 1


# ===== Pydantic 模型 =====
class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: str
    age: int = Field(..., ge=1, le=150)
    department: Optional[str] = None


class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=50)
    email: Optional[str] = None
    age: Optional[int] = Field(None, ge=1, le=150)
    department: Optional[str] = None


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    age: int
    department: Optional[str]


class PageResponse(BaseModel):
    total: int
    page: int
    size: int
    items: list[UserResponse]


# ===== 中间件：记录请求耗时 =====
@app.middleware("http")
async def add_timing_header(request, call_next):
    start = time.time()
    response = await call_next(request)
    response.headers["X-Process-Time"] = f"{time.time() - start:.4f}"
    return response


# ===== CRUD 接口 =====

@app.get("/")
def root():
    return {"message": "用户管理 API 运行中", "docs": "/docs"}


# C - Create 创建
@app.post("/api/users", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate):
    global next_id

    # 检查邮箱唯一性
    for u in fake_db.values():
        if u["email"] == user.email:
            raise HTTPException(status_code=409, detail="邮箱已存在")

    new_user = {"id": next_id, **user.model_dump()}
    fake_db[next_id] = new_user
    next_id += 1
    return new_user


# R - Read 查询列表（分页 + 筛选）
@app.get("/api/users", response_model=PageResponse)
def list_users(
        page: int = Query(1, ge=1, description="页码"),
        size: int = Query(10, ge=1, le=100, description="每页条数"),
        department: Optional[str] = Query(None, description="部门筛选"),
        keyword: Optional[str] = Query(None, description="关键词搜索"),
):
    users = list(fake_db.values())

    # 筛选
    if department:
        users = [u for u in users if u.get("department") == department]
    if keyword:
        users = [u for u in users if keyword.lower() in u["name"].lower()]

    # 分页
    total = len(users)
    start = (page - 1) * size
    items = users[start:start + size]

    return PageResponse(total=total, page=page, size=size, items=items)


# R - Read 查询单个
@app.get("/api/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="用户不存在")
    return fake_db[user_id]


# U - Update 更新
@app.put("/api/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate):
    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="用户不存在")

    update_data = user.model_dump(exclude_unset=True)  # 只取传了的字段
    fake_db[user_id].update(update_data)
    return fake_db[user_id]


# D - Delete 删除
@app.delete("/api/users/{user_id}", status_code=204)
def delete_user(user_id: int):
    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="用户不存在")
    del fake_db[user_id]
    return None  # 204 无返回体


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8100)
