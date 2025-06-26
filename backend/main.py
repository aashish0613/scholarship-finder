from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from rag.query_rag import get_answer

app = FastAPI()

# Allow frontend access (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input schema for POST request
class QueryRequest(BaseModel):
    query: str

# POST endpoint to receive query and return answer
@app.post("/query")
async def query_endpoint(req: QueryRequest):
    try:
        answer = get_answer(req.query)
        return {"answer": answer}
    except Exception as e:
        return {
            "answer": "Something went wrong. Please try again.",
            "error": str(e)
        }
