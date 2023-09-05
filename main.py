from fastapi import FastAPI
import uvicorn
from blog import models
from blog.database import engine
from blog.routers import blog, user, authentication

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
