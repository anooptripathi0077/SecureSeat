# CrickEco (SecureSeat) - Deployment Ready

This project is now structured for easy deployment on **Vercel** (Frontend) and **Render** (Backend & AI Service).

## 📂 Project Structure
- **[/frontend](file:///frontend)**: React + Three.js + Vite (Deploy to Vercel)
- **[/backend](file:///backend)**: Node.js + Express + PostgreSQL (Deploy to Render)
- **[/ai-service](file:///ai-service)**: Python + FastAPI + OpenCV (Deploy to Render)
- **[/data](file:///data)**: CSV files for database seeding.
- **[/docs](file:///docs)**: Detailed project documentation and guides.
- **[/scripts](file:///scripts)**: Miscellaneous utility scripts.

## 🚀 Deployment Instructions

### 1. Backend (Render)
- **Repo**: This repository.
- **Root Directory**: `backend`
- **Build Command**: `npm install`
- **Start Command**: `npm start`
- **Environment Variables**: Copy from `backend/.env.example`.

### 2. AI Service (Render)
- **Repo**: This repository.
- **Root Directory**: `ai-service`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app`
- **Environment Variables**: `PORT=10000`.

### 3. Frontend (Vercel)
- **Repo**: This repository.
- **Root Directory**: `frontend`
- **Framework Preset**: Vite
- **Environment Variables**: Copy from `frontend/.env.example`.

## 🛠️ Local Setup
1. Install dependencies in each folder.
2. Set up local `.env` files using the provided `.env.example` templates.
3. Use `npm run dev` in frontend/backend and `uvicorn app.main:app` in ai-service.

---
*For original project details, see [docs/PROJECT_README.md](file:///docs/PROJECT_README.md)*