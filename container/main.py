from typing import TypedDict

from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/webhook")
def listen(request:Request):
    verify_webhook(request)


class FacebookToken(TypedDict):
    "hub.mode"
    "hub.verify"
    "hub.challenge"


def verify_webhook(hub_mode:str, hub_verify:str, hub_challenge):
    
    calling_verify_token = req.query_params
    
    fb_verify_token = "<Your Verification Token>"
    if calling_verify_token == fb_verify_token:
        challenge = req.args.get("hub.challenge")
        return challenge
    else:
        return "incorrect"