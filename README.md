# ExplAInCheck 🌾
**AI Explanation Verifier for Smart Agriculture - CornHacks 2025**


> [!IMPORTANT]
> **Competition Integrity Notice**
> 
> - ✅ **No code was published or developed before the competition started**
> - ✅ **All development was completed within the official competition timeframe**
> - ℹ️ The repository was created beforehand with an initial README placeholder
> - ℹ️ The README content was fully updated after the competition start time
>
> - 
[![CornHacks 2025](https://img.shields.io/badge/CornHacks-2025-green)](https://unlcornhacks.com)
[![Track](https://img.shields.io/badge/Track-Agriculture-orange)](https://unlcornhacks.com)
[![Sponsor](https://img.shields.io/badge/Sponsored_by-Conagra_Brands-red)](https://www.conagrabrands.com/)

---

## 🌐 Live Demo

**Try it now:** [https://explaincheck-1.onrender.com](https://explaincheck-1.onrender.com)

![ExplAInCheck Demo](https://github.com/rashedhasan090/ExplAInCheck/blob/main/Assets/ExplAInCheck_Demo.gif)
---

## 🏆 Competition Track: **AGRICULTURE**
**Innovate for the future of food and farming** | Sponsored by Conagra Brands

Also pursuing: **BANANA** Track (Because verification is bananas! 🍌)

---

## Overview

Modern agriculture increasingly relies on AI-powered recommendations for critical farming decisions—crop management, irrigation schedules, pesticide application, soil treatment, and harvest timing. But here's the problem: **What happens when AI gives farmers bad advice?**

A single wrong recommendation can result in:
- 💸 **Crop failure** costing thousands of dollars
- 🌱 **Soil damage** that takes years to recover
- ☠️ **Food safety issues** from incorrect pesticide guidance
- 🚜 **Wasted resources** (water, fertilizer, time, equipment)

Farmers and agricultural businesses need a way to **verify AI explanations before acting on them**—especially when the stakes are this high.

**ExplAInCheck** addresses this challenge by creating the world's first real-time AI explanation verification system specifically designed for agriculture. When an AI system provides farming advice or recommendations, ExplAInCheck automatically:
- ✅ Parses the explanation into verifiable logical components
- 🔍 Checks each claim for consistency and completeness
- ⚠️ Flags potential gaps, contradictions, or unsubstantiated assumptions
- 🎯 Provides interactive explanations that farmers can understand

---

## 🎥 Demo Video

Watch ExplAInCheck in action! See how our AI explanation verification system works with real agricultural scenarios:

**[📺 Watch the Demo Video](https://1drv.ms/v/c/645fee2ef572d93d/EWpqlwyv9v1IgS61TK_Z5XsBM7hPBg38tHpb5Fz2xzURxA?e=Ng9dgF)**

*Click the link above to view our full demonstration on OneDrive.*

---

## The Agricultural Problem

AI agricultural advisors (from apps, IoT sensors, precision ag platforms) can generate detailed recommendations, but they often:

- **Make logical leaps without justification**
  - "Increase irrigation by 30%" → But why? Based on what soil moisture data?
  
- **Include hidden assumptions that may not apply to your farm**
  - "This fertilizer schedule works" → Assumes specific soil pH, climate, crop variety
  
- **Contradict themselves across different advice**
  - "Reduce water usage" vs "Increase yield" without explaining the tradeoff
  
- **Omit critical safety information**
  - Pesticide application timing without weather/wind considerations
  
- **Present unverified claims as established facts**
  - "This will increase yield by 25%" → No data source or confidence interval

For agriculture, these gaps can lead to **economic losses, environmental damage, and food safety risks**. Yet farmers often lack the technical expertise or time to identify these logical flaws.

---

## Our Solution: AI Verification for Smart Farming

ExplAInCheck bridges the gap between AI-generated agricultural advice and trustworthy farming decisions through:

### 1. 🧠 **Intelligent Parsing**
Using advanced NLP and agricultural domain knowledge, we break down AI farming recommendations into discrete logical statements:
- Input claims (soil data, weather, crop type)
- Reasoning steps (why this recommendation makes sense)
- Output actions (what to do, when, and how)

### 2. ✅ **Formal Verification**
We apply symbolic reasoning and constraint-solving techniques (SAT/SMT solvers) to verify:
- Logical consistency (do all the pieces fit together?)
- Causal relationships (does A actually lead to B?)
- Agricultural constraints (safe ranges for water, chemicals, temperature)

### 3. 🔎 **Gap Detection**
Our system identifies:
- Missing premises ("Use this fertilizer" → but what about soil pH?)
- Circular reasoning (conclusion depends on itself)
- Unsubstantiated yield/cost claims
- Safety violations (pesticide application windows)

### 4. 💬 **Interactive Debugging**
Farmers can click on any part of an AI explanation to:
- See why it's valid, questionable, or potentially unsafe
- Get plain-English explanations (no technical jargon)
- View alternative recommendations
- Understand risk levels (critical vs. minor concerns)

### 5. 🌾 **Agriculture-Specific Intelligence**
Special attention to farming domains:
- **Crop management** (planting, growth stages, harvest timing)
- **Soil health** (pH, nutrients, organic matter)
- **Irrigation** (water usage optimization)
- **Pest control** (safe pesticide/herbicide application)
- **Food safety** (harvest intervals, contamination risks)
- **🍌 Banana farming** (potassium requirements, tropical conditions)

---

## Why It Matters: Innovation for Agriculture

This project represents a novel convergence of:

✨ **Generative AI** → Understanding natural language farming advice  
🔬 **Formal Methods** → Mathematical verification of agricultural logic  
🛡️ **AI Safety** → Protecting farmers from harmful AI mistakes  
♿ **Accessibility** → Making verification tools usable by non-experts  
🌾 **AgTech** → Advancing precision agriculture with trustworthy AI  

**No existing platform offers real-time, interactive verification of AI agricultural recommendations.** Current AgTech solutions either:
- Blindly trust AI outputs without verification
- Require expert agronomists to manually review (slow, expensive)
- Focus on data collection but not decision validation

ExplAInCheck empowers **farmers, agricultural businesses, and food producers** to confidently use AI tools while maintaining critical oversight over decisions that affect their crops, land, and livelihoods.

---

## CornHacks 2025 Demo: Smart Banana Farming 🍌

For this hackathon, we're showcasing ExplAInCheck with **banana agriculture** examples—perfectly aligned with the **BANANAHACKS** theme!

### Demo Scenarios:

**1. Banana Irrigation Advice**
- Submit: "Increase watering to 50mm/week for optimal banana growth"
- ExplAInCheck verifies: soil drainage, climate, growth stage, potassium uptake
- Flags: Missing rainfall data, no mention of root rot risks

**2. Potassium Fertilizer Recommendations**
- Submit: "Apply 200kg/hectare potassium sulfate now"
- ExplAInCheck checks: soil test results, banana variety, application timing
- Flags: Potential over-fertilization, no mention of magnesium balance

**3. Pest Management for Banana Plantations**
- Submit: "Spray neem oil every 3 days to control aphids"
- ExplAInCheck validates: safety intervals, weather conditions, beneficial insects
- Flags: May harm pollinators, too frequent application

**4. Harvest Timing Optimization**
- Submit: "Harvest when bananas reach 75% maturity for export"
- ExplAInCheck verifies: ripening indicators, transportation time, quality standards
- Highlights: Valid approach, explains maturity measurement methods

---

## Technical Architecture

```
┌─────────────────┐
│   Web Frontend  │  React + TailwindCSS
│  (User Input)   │  
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   REST API      │  Flask Backend
│  /api/verify    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  NLP Parser     │  spaCy + Agriculture NER
│  (Extract       │  Domain: crops, soil, water
│   Claims)       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Formal Verifier │  Z3 SMT Solver
│ (Check Logic)   │  Agricultural Constraints
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Results        │  Interactive Visualization
│  Generator      │  + Farmer-Friendly Explanations
└─────────────────┘
```

### Tech Stack:
- **Frontend**: React, TypeScript, TailwindCSS, D3.js (visualization)
- **Backend**: Python, Flask, spaCy, Z3-solver
- **NLP**: Pre-trained models + custom agricultural lexicon
- **Database**: SQLite (for demo), extensible to PostgreSQL
- **Deployment**: Frontend (Vercel), Backend (Render/Railway)

---

## Getting Started

### Prerequisites
```bash
# Check installations
node -v   # v14+ required
npm -v    # v6+ required
python -v # Python 3.9+ required
```

### Installation

```bash
# Clone repository
git clone https://github.com/rashedhasan090/ExplAInCheck.git
cd ExplAInCheck

# Backend setup
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m spacy download en_core_web_lg

# Frontend setup
cd ../frontend
npm install

# Start development servers
# Terminal 1 (Backend):
cd backend && python app.py

# Terminal 2 (Frontend):
cd frontend && npm start
```

### Usage

1. Open `http://localhost:3000` in your browser
2. Paste AI-generated agricultural advice (or use examples)
3. Click "Verify Explanation"
4. Explore interactive results:
   - ✅ Green: Verified claims
   - ⚠️ Yellow: Questionable assumptions
   - ❌ Red: Logical errors or safety concerns
5. Click any highlighted text for detailed reasoning

---

## Project Timeline (24-Hour Hackathon)

### Saturday 11:00 AM - 6:00 PM: Core Backend
- ✅ Flask API + NLP parsing
- ✅ Agricultural domain lexicon
- ✅ Basic Z3 verification logic

### Saturday 6:00 PM - Sunday 2:00 AM: Frontend + Integration
- ✅ React UI with input/results panels
- ✅ Backend-frontend integration
- ✅ Banana-themed examples

### Sunday 2:00 AM - 9:00 AM: Polish + Demo
- ✅ Interactive explanation features
- ✅ Demo video recording
- ✅ Documentation

### Sunday 9:00 AM - 10:00 AM: Final Testing + Submission


---

## Team

- **Developer**: Md Rashedul Hasan  
- **GitHub**: [@rashedhasan090](https://github.com/rashedhasan090)  


---

## Scoring Alignment (CornHacks Rubric)

| Category | Score | How We Excel |
|----------|-------|-------------|
| **Problem Solved** | 15 | Addresses critical agricultural safety and economic risks from bad AI advice |
| **Innovation** | 20 | First-ever real-time formal verification of AI agricultural recommendations |
| **Difficulty** | 15 | Combines NLP, formal methods, AgTech domain knowledge in 24 hours |
| **Completeness** | 15 | Working demo with backend verification + interactive frontend |
| **Solution Quality** | 15 | Directly prevents crop/financial losses; benefits farmers and food industry |
| **Design Practices** | 10 | Modular architecture, documented code, scalable design |
| **Presentation** | 10 | Clear demo, farmer-friendly explanations, interactive visualization |
| **TOTAL** | **100** | |

---

## Future Enhancements

🔮 **Post-Hackathon Roadmap**:
- Integration with major AgTech platforms (John Deere, Climate FieldView)
- Mobile app for on-farm verification
- Multi-language support (Spanish, Portuguese for global farming)
- Historical data learning (improve verification with farm outcomes)
- IoT sensor integration (real-time verification with live data)
- Blockchain for verified recommendation tracking

---

## Acknowledgments

🙏 **Special Thanks:**
- **CornHacks 2025** organizers and volunteers
- **Conagra Brands** for sponsoring the Agriculture Track
- **UNL School of Computing** for hosting
- Open-source communities: spaCy, Z3, React

---

## License

MIT License - See [LICENSE](https://github.com/rashedhasan090/ExplAInCheck/blob/main/LICENSE/MIT%20License.txt) for details

---

**Built for CornHacks 2025 | Agriculture Track 🌾 + Banana Track 🍌**

*Innovating for the future of food and farming with trustworthy AI*
