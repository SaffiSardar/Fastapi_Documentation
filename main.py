from fastapi import FastAPI

app = FastAPI()

# @something is decorator
@app.get("/")
# why async :-
async def root():
    return {"message": "Hello World"}


# after this run "fastapi dev main.py" on terminal 
# after opening local machine site add path /docs
#  to view interactive api docs[swaggerui]
# fastapi uses openapi schema to mask ur schema/routes uses json schema

# to view your schema -> json schema, add /openapi.json at end of path

# Operations:
# Post::Create /Get::Read /Put::Update /Delete:: Delete //Options/Head/Patch/trace




