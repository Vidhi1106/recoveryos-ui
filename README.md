# RecoveryOS — Demo UI

Interactive demo frontend for **RecoveryOS**, an AI-powered post-discharge care coordinator.

Built for the Google Cloud Hackathon 2026.

**Live Demo:** [https://cosmic-corgis-multiagent.web.app](https://cosmic-corgis-multiagent.web.app)

**Backend API:** Deployed on Google Cloud Run · Powered by Gemini 2.5 Flash on Vertex AI

---

## What it covers

The demo walks through all 6 key capabilities in sequence:

| Step | Feature |
|---|---|
| 1 | Upload a discharge summary PDF — any patient |
| 2 | View the AI-generated recovery plan — medications, red flags, restrictions |
| 3 | See appointments auto-booked via Google Calendar MCP |
| 4 | Submit a daily symptom check-in via conversational AI |
| 5 | Trigger escalation — critical symptoms detected, care team notified |
| 6 | View auto-generated insurance claim letter |

---

## Files

```
recoveryos-ui/
├── index.html                   ← Complete demo (single file, no build needed)
├── sample_discharge_stroke.txt  ← Sample patient file to upload in demo
├── firebase.json                ← Firebase Hosting config
├── .firebaserc                  ← Firebase project config
├── .gitignore
└── README.md
```

---

## Running locally

No build step needed. Just open in browser:

```bash
# Option 1 — open directly
open index.html

# Option 2 — serve locally
python3 -m http.server 3000
# then visit http://localhost:3000
```

---

## Connecting to the live backend

1. Open the demo in your browser
2. Paste your Cloud Run API URL in the field at the top of Screen 1
3. Click **Save & Connect**

The URL looks like:
```
https://recoveryos-api-xxxx-el.a.run.app
```

Once connected, all 6 demo steps make real API calls to the deployed backend.
If the backend is unavailable, the UI falls back to realistic mock data automatically.

---

## Deploying to Firebase Hosting

```bash
# Install Firebase CLI
npm install -g firebase-tools

# Login
firebase login

# Deploy
firebase deploy --only hosting
```

This gives you a public URL you can open on any device including a phone.

---

## Sample patient file

`sample_discharge_stroke.txt` is a realistic discharge summary for a stroke patient.
Upload it in Step 1 of the demo to show the AI pipeline with a real document.

Other built-in sample patients (selectable without uploading):
- 🧠 Stroke Recovery — Priya Venkataraman
- 🤱 Post-Delivery Care — Anjali Kapoor
- 🎗️ Chemo Recovery — Mohan Pillai

---

## Tech stack

| Layer | Technology |
|---|---|
| AI model | Gemini 2.5 Flash |
| AI platform | Google Vertex AI |
| Backend | FastAPI on Google Cloud Run |
| Database | Google Cloud SQL (PostgreSQL 16) |
| File storage | Google Cloud Storage |
| Frontend hosting | Firebase Hosting |
| Auth | Application Default Credentials (ADC) |

---

## Backend repository

The backend (RecoveryOS API) is in a separate repository.

Architecture: 1 Orchestrator Agent + 5 Sub-Agents running in parallel:
- Medication Agent
- Appointment Agent (Google Calendar MCP)
- Symptom Monitor Agent
- Caregiver Coordinator Agent (Todoist MCP)
- Insurance Documents Agent

---

*RecoveryOS — Reducing preventable hospital readmissions through AI-coordinated post-discharge care.*
