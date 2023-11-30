import hashlib
import json
from fastapi import HTTPException, status, Security, FastAPI
from fastapi.security import APIKeyHeader, APIKeyQuery

API_KEYS = [
            "API_KEY"
           ]

api_key_query = APIKeyQuery(name="api-key", auto_error=False)


def get_api_key(api_key_query: str = Security(api_key_query)):
    """Retrieve & validate an API key from the query parameters"""
    if api_key_query is None:
        return api_key_query
    query_sha256 = hashlib.sha256(api_key_query.encode()).hexdigest()

    if query_sha256 in API_KEYS:
        return query_sha256

    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="Invalid or missing API Key",
                       )

app = FastAPI(title="MIHARI API")

@app.get("/member")
def member(api_key: str = Security(get_api_key)):
    member_json = open('member.json', 'r')
    member_dict = json.load(member_json)
    return member_dict
