#import package
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

#create FastAPI app
app = FastAPI(
  title="FastAPI Example",
  description="""
    This is my FastAPI application
  """,
  version="1.0"
)

# add CORS middleware
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

#ProjectName = ""
ProjectName = "/MyWebAPI"

@app.get(ProjectName + "/", response_class=HTMLResponse)
async def Hello():
  return '<h1>Hello, My FastAPI</h1>'  #hello response

@app.post(ProjectName + "/ResponseData")
async def ResponseData(request: Request):
  try:
    requestData = await request.json()  #get request data from client
    receivedData = requestData["SendData"]  #get JSON data
    responseMsg = {"ReturnMsg": receivedData}  #compose response message
    return responseMsg  #return response message
  except Exception as err:
    responseMsg = {"ReturnMsg": str(err)}  #exception message
    return responseMsg  #return response message

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")  #run uvicorn server
  