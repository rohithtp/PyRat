import re
import sys
from pathlib import Path

def verify_specs():
    print("Verifying UI specifications against main.py...")
    
    try:
        content = Path("main.py").read_text(encoding="utf-8")
    except FileNotFoundError:
        print("Error: main.py not found.")
        sys.exit(1)
        
    checks = [
        {
            "name": "Header Title",
            "regex": r'PyRat: The High-Seas System Monitor',
            "required": True
        },
        {
            "name": "Header Color (Cyan)",
            "regex": r'Color\.Cyan',
            "required": True
        },
        {
            "name": "CPU Block Title",
            "regex": r'CPU Load:.*Peak:',
            "required": True
        },
        {
            "name": "CPU Color (Green)",
            "regex": r'Color\.Green',
            "required": True
        },
        {
            "name": "RAM Block Title",
            "regex": r'RAM Usage:',
            "required": True
        },
        {
            "name": "RAM Gauge Color (Magenta)",
            "regex": r'Color\.Magenta',
            "required": True
        },
        {
            "name": "Footer Instructions",
            "regex": r"Press 'q' to abandon ship",
            "required": True
        }
    ]
    
    failed = False
    for check in checks:
        if re.search(check["regex"], content):
            print(f"[PASS] {check['name']}")
        else:
            print(f"[FAIL] {check['name']}")
            if check["required"]:
                failed = True
                
    if failed:
        sys.exit(1)
    else:
        print("All spec verifications passed.")

if __name__ == "__main__":
    verify_specs()
