from fastapi import FastAPI, Request
from datetime import datetime
from dateutil.relativedelta import relativedelta
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

START_TIME = datetime(2019, 9, 10, 12, 0, 0)  # 10 Sep 2019 12:00 PM

@app.get("/", response_class=HTMLResponse)
def get_time_elapsed(request: Request):
    now = datetime.now()
    delta = relativedelta(now, START_TIME)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "delta": delta
    })
