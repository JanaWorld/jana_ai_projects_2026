# stop_server.ps1
# This script stops the running Customer Churn FastAPI server.

Write-Host "Stopping FastAPI Server..." -ForegroundColor Red

# Find the process running on port 8000 and kill it
$process = Get-NetTCPConnection -LocalPort 8000 -ErrorAction SilentlyContinue | 
           Select-Object -ExpandProperty OwningProcess

if ($process) {
    Stop-Process -Id $process -Force
    Write-Host "✅ Server stopped successfully. Port 8000 is now free." -ForegroundColor Green
} else {
    Write-Host "No server found running on port 8000." -ForegroundColor Yellow
}
