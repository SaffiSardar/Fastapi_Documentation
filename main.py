# #----->FIRST STEPS

# from fastapi import FastAPI

# app = FastAPI()

# # @something is decorator
# @app.get("/")
# # why async :-
# async def root():
#     return {"message": "Hello World"}


# # after this run "fastapi dev main.py" on terminal 
# # after opening local machine site add path /docs
# #  to view interactive api docs[swaggerui]
# # fastapi uses openapi schema to mask ur schema/routes uses json schema

# # to view your schema -> json schema, add /openapi.json at end of path

# # Operations:
# # Post::Create /Get::Read /Put::Update /Delete:: Delete //Options/Head/Patch/trace



# #----->PATH PARAMETERS

# from fastapi import FastAPI

# app = FastAPI()

# # parameterized paths
# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}

# # type parameterized paths
# # benificial for editor level error handling(uses pydantic for data validation)
# @app.get("/items1/{item1_id}")
# async def read_item1(item1_id: int):
#     return {"item_id": item1_id}

# # order matters - u will understand later, for now just remember
# @app.get("/users/me")
# async def read_user_me():
#     return {"user_id": "Current User"}

# @app.get("/users/{user_id}")
# async def read_user(user_id:str):
#     return {"user_id":user_id}

# #   always uses first matched path, doesnt duplicated
# @app.get("/users")
# async def read_users():
#     return ["Saffi","Sardar"]

# @app.get("/users")
# async def read_users2():
#     return ["M","Ibrahim"]

# # Enum - bounds to select from limited choice at run time
# from enum import Enum
# class ModelName(str,Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"

# @app.get("/models/{model_name}")
# async def get_models(model_name: ModelName):
#     #method 1 to verify
#     if model_name is ModelName.alexnet:
#         return {"model_name":model_name , "message": "DL FTW"}
#     #method 2 to verify
#     if model_name.value == "lenet":
#         return {"model_name":model_name,"message":"leCNN"}
    
#     return {"model_name":model_name,"message": "have some residuals"}

# # Path Converter - how to send path
# @app.get("/files/{file_path:path}")
# async def read_file(file_path:str):
#     return {"file_path": file_path}


#----->Query PARAMETERS

















