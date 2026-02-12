"""
DrillCalc - Module 1: Hoisting System & Structure
Author: Antony Picon, Mechanical Engineer
Description: Main entry point for the FastAPI application.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
from backend.routers import module_1

app = FastAPI(
    title="DrillCalc API - Module 1",
    description="API for Drilling Engineering Calculations (Hoisting System & Structure API 4F/9B)",
    version="1.0.0"
)

# CORS Configuration
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. Include API Routers FIRST
app.include_router(module_1.router)

# 2. Serve Frontend Static Files LAST (at root)
frontend_path = os.path.join(os.getcwd(), "frontend")
if os.path.exists(frontend_path):
    app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")
else:
    @app.get("/")
    async def root():
        return {"message": "DrillCalc API is running. Frontend directory not found."}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
