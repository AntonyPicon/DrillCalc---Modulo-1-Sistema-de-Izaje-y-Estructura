"""
DrillCalc - Module 1: Hoisting System & Structure
Author: Antony Picon, Mechanical Engineer
Description: Main entry point for the FastAPI application.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import module_1

app = FastAPI(
    title="DrillCalc API - Module 1",
    description="API for Drilling Engineering Calculations (Hoisting System & Structure API 4F/9B)",
    version="1.0.0"
)

# CORS Configuration
origins = [
    "*", # Allow all for development simplicity as requested ("Full Stack")
    "http://localhost:5500",
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(module_1.router)

@app.get("/")
async def root():
    return {"message": "DrillCalc API is running. Visit /docs for Swagger UI."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
