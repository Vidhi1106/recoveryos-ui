# RecoveryOS — Demo UI

Interactive demo frontend for **RecoveryOS**, an AI-powered post-discharge care coordinator.

Built for the **Gen AI Academy APAC Edition Hackathon** by Google Cloud.

**Participant:** Vidhi Agarwal

---

## Live Links

| | URL |
|---|---|
| 🌐 **Demo UI** | https://recoveryos-ui-e3de5vtq6q-el.a.run.app |
| 📡 **Backend API** | https://recoveryos-api-e3de5vtq6q-el.a.run.app |
| 📖 **API Docs (Swagger)** | https://recoveryos-api-e3de5vtq6q-el.a.run.app/docs |

---

## What is RecoveryOS?

**RecoveryOS (Recovery Operating System)** coordinates a patient's entire post-discharge recovery automatically.
One discharge summary goes in — medications, appointments, caregiver tasks, symptom monitoring and insurance documents come out.

**Problem it solves:** 20% of patients are readmitted within 30 days of discharge — not because their condition worsens,
but because post-discharge coordination fails. Medications are missed, follow-ups are forgotten, red flag symptoms go unnoticed.

---

## Demo — 6 Steps

The UI walks through the complete end-to-end workflow:

| Step | Screen | What it shows |
|---|---|---|
| 1 | Upload Discharge | Drag and drop a PDF or pick a sample patient. 5 AI agents fire in parallel. |
| 2 | Recovery Plan | Medications extracted with schedules, red flag symptoms, restrictions — all from the document. |
| 3 | Appointments | Every follow-up date auto-detected and scheduled in Google Calendar via MCP. |
| 4 | Symptom Check-in | Daily conversational check-in. AI scores severity and monitors for warning signs. |
| 5 | Escalation | Critical symptoms trigger automatic SMS to caregiver + urgent appointment booked. |
| 6 | Insurance Claim | Formal claim letter generated and ready to download — no manual paperwork. |

---

## Project Files

```
recoveryos-ui/
├── index.html                   ← Complete demo UI (single file, no build step needed)
├── sample_discharge_stroke.txt  ← Realistic stroke patient discharge summary for demo
├── firebase.json                ← Firebase Hosting config
├── .firebaserc                  ← Firebase project (cosmic-corgis-multiagent)
├── .gitignore
└── README.md
```

---

## Running Locally

No build step, no npm install. Just open in browser:

```bash
# Option 1 — open directly
open index.html

# Option 2 — serve via Python
python3 -m http.server 3000
# Visit http://localhost:3000
```

---

## Connecting to the Live Backend

1. Open the demo in your browser
2. At the top of Screen 1, paste the backend API URL:
   ```
   https://recoveryos-api-e3de5vtq6q-el.a.run.app
   ```
3. Click **Save & Connect**

All 6 demo steps will now make real API calls to the deployed Gemini-powered backend.
If the backend is unavailable, the UI automatically falls back to realistic mock data — the demo never breaks.

---

## Sample Patient File

`sample_discharge_stroke.txt` is a realistic discharge summary for **Priya Venkataraman**, a 67-year-old
stroke patient discharged from Apollo Hospitals, Chennai. Upload it in Step 1 to show the full AI pipeline
working on a real clinical document.

**Built-in sample patients** (no upload needed — just click):

| Patient | Case | Complexity |
|---|---|---|
| 🧠 Priya Venkataraman | Ischemic Stroke + Diabetes | 5 medications, 5 appointments, aphasia rehab |
| 🤱 Anjali Kapoor | Post C-Section Delivery | 4 medications, 4 appointments, breastfeeding instructions |
| 🎗️ Mohan Pillai | Chemotherapy Recovery | Neutropenia precautions, 4 medications, strict diet protocol |

---

## Deploying to Cloud Run

The UI is deployed as a static server on Cloud Run (no Firebase required):

```bash
cd recoveryos-ui

# Create a simple Python server
cat > main.py << 'PYEOF'
import http.server, socketserver, os
PORT = int(os.environ.get("PORT", 8080))
handler = http.server.SimpleHTTPRequestHandler
handler.extensions_map.update({".html": "text/html"})
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
PYEOF

echo "python-3.11" > runtime.txt

# Deploy
gcloud run deploy recoveryos-ui \
  --source . \
  --region asia-south1 \
  --allow-unauthenticated \
  --port 8080
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| AI model | Gemini 2.5 Flash |
| AI platform | Google Vertex AI (ADC — no API key needed) |
| Backend framework | FastAPI (Python) |
| Backend hosting | Google Cloud Run |
| Database | Google Cloud SQL (PostgreSQL 16) |
| File storage | Google Cloud Storage |
| UI hosting | Google Cloud Run (static server) |
| Background jobs | APScheduler (daily reminders, check-ins) |

---

## Multi-Agent Architecture

```
Discharge PDF
      │
      ▼
Orchestrator Agent (Gemini 2.5 Flash)
      │ fires all 5 in parallel via asyncio.gather()
      ├── 💊 Medication Agent     → extracts drugs, schedules, dose tracking
      ├── 📅 Appointment Agent    → books follow-ups via Google Calendar MCP
      ├── 🩺 Symptom Monitor      → daily check-ins, severity scoring, escalation
      ├── 👥 Caregiver Coordinator → task assignment via Todoist MCP
      └── 📋 Insurance Agent      → generates claim letters, referrals, lab reqs
```

---

## Backend Repository

The full RecoveryOS API backend (FastAPI + all agents + GCP infrastructure scripts) is in a separate repository.

Includes:
- Complete agent source code (`agents/`)
- MCP integrations — Google Calendar, GCS, Todoist, Notion
- Database models (10 tables)
- GCP setup script (`scripts/gcp_setup.sh`)
- Cloud Build CI/CD pipeline (`cloudbuild.yaml`)
- Full test suite (`tests.py`)

---

*RecoveryOS — Reducing preventable hospital readmissions through AI-coordinated post-discharge care.*

*Gen AI Academy APAC Edition · Google Cloud Hackathon 2026*
