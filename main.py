from fastapi import FastAPI, Request, Form, status, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
import random

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory="templates")

@app.get('/')
async def index(request: Request):
    return templates.TemplateResponse("tp.html", {"request":request, 'number': random.randint(1,1001)})

@app.post('/api/retrieve-chat')
async def retreive_chats(request : Request):
    query = "select "
    try:
        # cursor.execute(query, [request.session['user_id']])
        # rows = cursor.fetchall()
        rows = (4, 'hfshs', 'higihdhedh'), (4, 'hfshs', 'higihdhedh'), (4, 'hfshs', 'higihdhedh')
        return JSONResponse(
            status_code=200,
            content= rows
        )
    except Exception as e:
        print(f"Error Occured {e}")
    # finally:
    #     conn.commit()
    #     conn.close()
    #     cursor.close()