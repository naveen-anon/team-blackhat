#!/usr/bin/env python3
# BLACK HAT PHISHING ANALYZER - EDU MODE

import re, os, json, time, math, datetime
import tldextract
from colorama import Fore, Style, init

init(autoreset=True)

# ------------------ UTILITIES ------------------

def slow(text, color=Fore.WHITE, d=0.008):
    for c in text:
        print(color + c, end='', flush=True)
        time.sleep(d)
    print()

def beep():
    print('\a', end='')

def entropy(s):
    prob = [float(s.count(c)) / len(s) for c in dict.fromkeys(list(s))]
    return -sum(p * math.log(p, 2) for p in prob)

def load_rules():
    with open("rules.db") as f:
        return [x.strip().lower() for x in f if x.strip()]

def domain(url):
    e = tldextract.extract(url)
    return f"{e.domain}.{e.suffix}"

# ------------------ BANNER ------------------

def banner():
    print(Fore.RED + Style.BRIGHT + r"""
██████╗ ██╗      █████╗  ██████╗██╗  ██╗
██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝
██████╔╝██║     ███████║██║     █████╔╝ 
██╔══██╗██║     ██╔══██║██║     ██╔═██╗ 
██████╔╝███████╗██║  ██║╚██████╗██║  ██╗
╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
""")
    slow(" > TEAM BLACK HAT :: PHISHING ANALYZER [EDU MODE]", Fore.RED)
    slow(" > Think like an attacker. Act like a defender.\n", Fore.RED)

# ------------------ CORE ANALYSIS ------------------

def attacker_mindset(url):
    ideas = []
    if "login" in url or "signin" in url:
        ideas.append("Credential bait used to steal usernames/passwords")
    if len(url) > 70:
        ideas.append("Long URL hides the real malicious domain")
    if url.startswith("https"):
        ideas.append("HTTPS used to fake legitimacy and trust")
    if "-" in url:
        ideas.append("Typosquatting technique detected")
    return ideas

def psychology_analysis(url):
    return {
        "Trust Trigger": "HIGH" if "login" in url else "MEDIUM",
        "Urgency Factor": "HIGH" if "verify" in url or "update" in url else "LOW",
        "Fear Induction": "MEDIUM",
        "Manipulation Level": "STRONG" if len(url) > 65 else "MODERATE"
    }

def url_dna(url):
    return {
        "Length": "LONG" if len(url) > 70 else "NORMAL",
        "Entropy": round(entropy(url), 2),
        "Pattern": "PHISH-LIKE" if "login" in url else "NORMAL",
        "Attack Goal": "Credential Harvesting" if "login" in url else "Unknown"
    }

def hacker_explain(url):
    explain = []
    if "login" in url:
        explain.append("Victim ko login page par redirect kiya ja raha hai")
    if re.search(r'\b\d{1,3}(\.\d{1,3}){3}\b', url):
        explain.append("Raw IP use karke domain trust bypass kiya gaya")
    if len(url) > 75:
        explain.append("URL length excessive hai to confuse victim")
    return explain

# ------------------ SCAN ENGINE ------------------

def analyze(url, rules):
    score = 0
    hits = []

    if not url.startswith("https"):
        score += 2
        hits.append("NO HTTPS")

    if re.search(r'\b\d{1,3}(\.\d{1,3}){3}\b', url):
        score += 3
        hits.append("RAW IP USED")

    for r in rules:
        if r in url.lower():
            score += 1
            hits.append(f"RULE MATCH: {r}")

    if len(url) > 75:
        score += 1
        hits.append("LONG URL")

    status = "CLEAN" if score <= 2 else "SUSPICIOUS" if score <= 5 else "HIGH RISK"

    return {
        "url": url,
        "domain": domain(url),
        "score": score,
        "status": status,
        "findings": hits,
        "attacker_mindset": attacker_mindset(url),
        "psychology": psychology_analysis(url),
        "dna": url_dna(url),
        "explanation": hacker_explain(url)
    }

# ------------------ REPORT ------------------

def save_report(results):
    os.makedirs("reports", exist_ok=True)
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    txt = f"reports/blackhat_{ts}.txt"
    js  = f"reports/blackhat_{ts}.json"

    with open(txt, "w") as f:
        for r in results:
            f.write(f"\nURL: {r['url']}\nSTATUS: {r['status']}\nSCORE: {r['score']}\n")
            f.write("ATTACKER VIEW:\n")
            for a in r["attacker_mindset"]:
                f.write(f" - {a}\n")

    with open(js, "w") as f:
        json.dump(results, f, indent=4)

    print(Fore.GREEN + f"\n[+] Reports saved → {txt} , {js}")

# ------------------ MAIN ------------------

def main():
    banner()
    rules = load_rules()
    results = []

    if os.path.exists("urls.txt"):
        slow("[*] Bulk scan mode detected\n", Fore.CYAN)
        with open("urls.txt") as f:
            urls = [x.strip() for x in f if x.strip()]
    else:
        urls = [input(Fore.RED + "blackhat@edu ~$ " + Fore.WHITE)]

    for u in urls:
        r = analyze(u, rules)
        results.append(r)

        print(Fore.CYAN + "\n[TARGET] " + u)
        print(Fore.MAGENTA + f"[SCORE] {r['score']}  [STATUS] {r['status']}")

        print(Fore.YELLOW + "\n[ATTACKER MINDSET]")
        for a in r["attacker_mindset"]:
            print(" -", a)

        print(Fore.YELLOW + "\n[PSYCHOLOGY]")
        for k,v in r["psychology"].items():
            print(f" {k}: {v}")

        print(Fore.YELLOW + "\n[URL DNA]")
        for k,v in r["dna"].items():
            print(f" {k}: {v}")

        print(Fore.RED + "\n[HACKER EXPLANATION]")
        for e in r["explanation"]:
            print(" -", e)

        if r["status"] == "HIGH RISK":
            beep()

    save_report(results)

if __name__ == "__main__":
    main()
