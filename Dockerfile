# ═══════════════════════════════════════════════════════════════════
# ChurnGuard AI — Hugging Face Spaces Dockerfile
# Single container: React (nginx) + FastAPI (uvicorn) + supervisord
# Port 7860 is required by Hugging Face Spaces
# ═══════════════════════════════════════════════════════════════════

# ── Stage 1: Build React frontend ─────────────────────────────────
FROM node:20-alpine AS frontend-builder

WORKDIR /app/frontend
COPY frontend/package.json frontend/package-lock.json ./
RUN npm ci
COPY frontend/ .
RUN npm run build

# ── Stage 2: Final image ───────────────────────────────────────────
FROM python:3.11-slim

# Install nginx and supervisor
RUN apt-get update && apt-get install -y \
    nginx \
    supervisor \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir \
    fastapi==0.115.0 \
    uvicorn[standard]==0.30.6 \
    joblib==1.4.2 \
    pandas==2.2.3 \
    scikit-learn==1.5.2 \
    pydantic==2.9.2

# Copy built React app to nginx html dir
COPY --from=frontend-builder /app/frontend/dist /usr/share/nginx/html

# Copy nginx config
COPY hf_nginx.conf /etc/nginx/conf.d/default.conf

# Remove default nginx config
RUN rm -f /etc/nginx/sites-enabled/default

# Copy FastAPI app and model
WORKDIR /app
COPY api_15.py .
COPY churn_model.joblib .

# Copy supervisord config
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Hugging Face Spaces requires port 7860
EXPOSE 7860

# Start both nginx and uvicorn via supervisord
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
