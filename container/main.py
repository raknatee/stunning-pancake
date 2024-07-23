from typing import TypedDict

from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/webhook")
def listen(request:Request):


    verify_webhook(request)






def verify_webhook(req:Request):
    
    calling_verify_token = req.query_params.get("hub.verify_token")
    print(calling_verify_token)
    fb_verify_token = "<Your Verification Token>"
    if calling_verify_token == fb_verify_token:
        challenge = req.query_params.get("hub.challenge")
        return challenge
    else:
        return "incorrect"