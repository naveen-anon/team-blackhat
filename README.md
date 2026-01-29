# 🔐 BlackHat Total  
### VirusTotal‑Inspired URL Analysis Tool (Educational)

BlackHat Total is a **lightweight, open‑source URL analysis tool** inspired by the
multi‑engine approach of **VirusTotal**.

It is designed **strictly for cyber‑security education, training, and awareness**,
helping students understand **how phishing URLs are analyzed**, not how attacks are performed.

---

## 📌 Why BlackHat Total?

Most beginners see only:
> “This link is dangerous.”

BlackHat Total answers:
> **WHY** it is dangerous  
> **HOW** attackers design it  
> **WHAT** indicators analysts look for  

This builds a **real Blue‑Team / SOC mindset**.

---

## 🎯 Core Objectives

- Understand phishing URL patterns
- Learn attacker manipulation techniques
- Practice analyst‑style investigation
- Study multi‑engine detection logic
- Build strong cyber‑security fundamentals

❌ No exploitation  
❌ No payloads  
❌ No attacks  

---

## 🧱 Project Structure (Minimal & Clean)
Designed intentionally with **only 2 core files**  
to keep learning simple and focused.

---

## ⚙️ How It Works (VirusTotal‑Style Logic)

A single URL is scanned by **multiple independent engines**.

Each engine:
- Analyzes a specific indicator
- Gives its own verdict
- Explains its reasoning

Final result is calculated using a **Detection Ratio**, similar to VirusTotal.

---

## 🧪 Analysis Engines Included

| Engine Name | Purpose |
|------------|--------|
| URL Structure Engine | Detects long URLs & typosquatting |
| Phishing Keyword Engine | Finds social‑engineering bait words |
| Entropy Engine | Detects obfuscation & randomness |
| HTTPS Trust Engine | Explains false trust in HTTPS |

Each engine returns:
- `CLEAN`
- `SUSPICIOUS`

---

## ▶️ Installation & Usage

### 1️⃣ Clone the repository
> - git clone https://github.com/naveen-anon/team-blackhat.git
> - pip3 install -r requirement.txt
> - cd team-blackhat
> - python3 main.py

## 🔐 Legal & Ethical Notice
This project is intended ONLY for educational and defensive purposes.
Do NOT use for real‑world attacks
Do NOT target live systems
Do NOT misuse analysis results
The author is not responsible for misuse.
## 🚀 Roadmap
CLI color & table output
Engine‑wise confidence scoring
Local Web UI (Flask)
Kali Linux .deb package
Student lab questions & challenges
## 👤 Author & Credits
Admin: @naveen-anon
Team: Team Black Hat
Focus Area: Cyber Security Education & Awareness
