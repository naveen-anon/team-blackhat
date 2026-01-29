# 🧬 BlackHat Total
### Multi-Engine URL Scanner (VirusTotal-Inspired)

BlackHat Total is a **local, multi-engine URL analysis tool** inspired by the
**VirusTotal detection-ratio model**.

It analyzes a URL using **independent scanning engines**, explains *why* a URL
is flagged, and produces an **analyst-style verdict**.

> Built for **cyber-security education, SOC training, and student labs**

---

## ⚙️ Features

- Multi-engine URL analysis
- VirusTotal-style detection ratio
- Engine-wise explanation
- Local scanning (no API, no data upload)
- JSON report generation

❌ No exploitation  
❌ No payload delivery  
❌ No attack modules  

---

## 🧪 Detection Engines

| Engine Name | Purpose |
|------------|--------|
| URL Structure Engine | Long URLs, typosquatting |
| Phishing Keyword Engine | Social-engineering bait words |
| Entropy Engine | Obfuscation & randomness |
| HTTPS Trust Engine | False HTTPS trust |

Each engine returns:
- `CLEAN`
- `SUSPICIOUS`
- `MALICIOUS`

---

## 📊 Verdict Logic

| Detection Ratio | Result |
|----------------|--------|
| 2+ MALICIOUS | 🚨 Likely Phishing |
| 2+ SUSPICIOUS | ⚠️ Suspicious |
| Else | ✅ Clean |

Inspired by **VirusTotal scan ratios**.

---

## ▶️ Installation & Usage

```bash
git clone https://github.com/naveen-anon/team-blackhat.git
cd team-blackhat
pip3 install -r requirements.txt
python3 main.py
````
## 📁 Output
Colorized CLI table
Final verdict banner
JSON scan report

blackhat_report.json

## 🗺️ Roadmap
🔊 Sound alert on phishing detection
🌐 Local VirusTotal-style Web UI (Flask)
📦 Kali Linux .deb package
🧪 Auto-generated student lab questions


## ⚠️ Legal Disclaimer
This tool is intended strictly for educational and defensive purposes.
Do NOT use for:
Real-world attacks
Targeting live systems
Malicious activity
The author is not responsible for misuse.


## 👤 Author
@naveen-anon
Team Black Hat
Focus: Cyber Security Education & Awareness
