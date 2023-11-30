import json
from fastapi import FastAPI

app = FastAPI()

@app.get("/member")
def member():
    member_json = open('member.json', 'r')
    member_dict = json.load(member_json)
    return member_dict
