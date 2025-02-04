import os
from fastapi import FastAPI
from fastapi import status
from fastapi.responses import RedirectResponse 
from fastapi.responses import FileResponse
app = FastAPI()
@app.get("/hi")
def hello():
    return "hello world!"
@app.get("/not/here")
def redirect():
    response = RedirectResponse(status_code=status.HTTP_301_MOVED_PERMANENTLY,
                                url='https://cnets-teach.gitlab.io/cmich-cps-420/')
    return response
@app.get("/gimme")
def download():
    response = FileResponse(path=os.path.basename(__file__),media_type='text/plain')
    # see https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types/Common_types
    return response
if __name__=="__main__": 
    import uvicorn
    uvicorn.run("Glover_HW1:app", host='127.0.0.1', port=4000, reload=True)