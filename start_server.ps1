# start_server.ps1
# This script starts the Customer Churn FastAPI server.

# 1. Activate the virtual environment
if (Test-Path ".\kalki\Scripts\Activate.ps1") {
    Write-Host "Activating virtual environment (kalki)..." -ForegroundColor Green
    . .\kalki\Scripts\Activate.ps1
} else {
    Write-Host "Warning: Could not find kalki virtual environment. Make sure you are running this from the churn folder." -ForegroundColor Yellow
}

# 2. Start the Uvicorn server
Write-Host "Starting FastAPI Server on http://127.0.0.1:8000 ..." -ForegroundColor Cyan
Write-Host "Swagger UI documentation available at: http://127.0.0.1:8000/docs" -ForegroundColor Cyan

# --reload automatically restarts the server if you change the Python code
# --host 0.0.0.0 exposes it so it can be accessed on your local network
uvicorn api_15:app --reload --host 0.0.0.0 --port 8000
