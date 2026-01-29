from engines import *
from colorama import Fore, Style, init
from tabulate import tabulate
from datetime import datetime
import json
import os

init(autoreset=True)

ENGINES = {
    "URL Structure": url_structure_engine,
    "Keyword Analysis": keyword_engine,
    "Entropy Check": entropy_engine,
    "HTTPS Trust": https_engine
}

def banner():
    print(Style.BRIGHT + Fore.RED + "██████╗ ██╗      █████╗  ██████╗██╗  ██╗ █████╗ ████████╗")
    print(Style.BRIGHT + Fore.RED + "██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝██╔══██╗╚══██╔══╝")
    print(Style.BRIGHT + Fore.YELLOW + "██████╔╝██║     ███████║██║     █████╔╝ ███████║   ██║")
    print(Style.BRIGHT + Fore.YELLOW + "██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██╔══██║   ██║")
    print(Style.BRIGHT + Fore.GREEN + "██████╔╝███████╗██║  ██║╚██████╗██║  ██╗██║  ██║   ██║")
    print(Style.BRIGHT + Fore.GREEN + "╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝")
    print(Fore.CYAN + "      BLACKHAT TOTAL :: VirusTotal-Style URL Scanner")
    print(Fore.MAGENTA + "      Multi-Engine • Offline • Defensive\n")

def generate_lab():
    print(Fore.MAGENTA + "\n🧪 STUDENT LAB QUESTIONS")
    print("1) Kaunse engines ne URL ko malicious mark kiya?")
    print("2) High entropy ka matlab kya hota hai?")
    print("3) HTTPS hone ke baad bhi phishing kaise possible hai?")
    print("4) Ek URL design karo jo sirf 1 engine trigger kare.")
    print("5) Attacker ka objective kya ho sakta hai?\n")

def scan(url):
    banner()
    print(Fore.WHITE + f"Target → {url}\n")

    table = []
    stats = {"CLEAN":0, "SUSPICIOUS":0, "MALICIOUS":0}

    report = {
        "target": url,
        "time": str(datetime.now()),
        "engines": {}
    }

    for name, engine in ENGINES.items():
        verdict, reasons = engine(url)
        stats[verdict] += 1

        table.append([name, verdict, ", ".join(reasons) if reasons else "-"])
        report["engines"][name] = {"verdict": verdict, "reasons": reasons}

    print(tabulate(table, headers=["Engine", "Verdict", "Details"], tablefmt="fancy_grid"))

    print("\nDetection Ratio:")
    for k,v in stats.items():
        print(f" {k:<10}: {v}")

    if stats["MALICIOUS"] >= 2:
        final = Fore.RED + "🚨 LIKELY PHISHING"
        os.system("printf '\a'")  # 🔊 beep alert
    elif stats["SUSPICIOUS"] >= 2:
        final = Fore.YELLOW + "⚠️ SUSPICIOUS"
    else:
        final = Fore.GREEN + "✅ CLEAN"

    print("\nFinal Verdict:", final)

    with open("blackhat_report.json", "w") as f:
        json.dump(report, f, indent=4)

    print(Fore.GREEN + "\n[+] Report saved → blackhat_report.json")
    generate_lab()

if __name__ == "__main__":
    u = input("Enter URL to scan: ")
    scan(u)
