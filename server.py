from fastapi import FastAPI
from datetime import datetime
from dateutil.relativedelta import relativedelta
from fastapi.responses import HTMLResponse

app = FastAPI()

START_TIME = datetime(2019, 9, 10, 12, 0, 0)  # 10 Sep 2019 12:00 PM

@app.get("/")
def get_time_elapsed():
    now = datetime.now()
    delta = relativedelta(now, START_TIME)

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Time Elapsed Since 10 Sep 2019</title>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #f5f7fa;
                color: #333;
                text-align: center;
                padding-top: 50px;
            }}
            .container {{
                background-color: #fff;
                padding: 40px;
                margin: auto;
                width: 400px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                border-radius: 10px;
            }}
            .heading {{
                font-size: 2rem;
                font-weight: bold;
                color: #007acc;
            }}

            .time-box {{
                font-size: 1.2em;
                line-height: 1.8;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <p class="heading">Arrow is now</p>
            <p class="time-box">
                <strong>{delta.years}</strong> years
                <strong>{delta.months}</strong> months
                <strong>{delta.days}</strong> days
                <strong>{delta.hours}</strong> hours
                <strong>{delta.minutes}</strong> minutes
                <strong>{delta.seconds}</strong> seconds
            </p>
            <p class="heading">old.</p>
            <p style="font-size: 0.9em; color: #777;">(Since 10 September 2019, 12:00 PM)</p>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)
