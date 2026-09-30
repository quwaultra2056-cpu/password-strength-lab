# Password Strength Lab - Defensive Tool
# Author: Quwa Ultra 2056 - White Hat
# Purpose: Check YOUR OWN password strength

def check(pw):
    score = 0
    if len(pw) >= 8: score += 1
    if len(pw) >= 12: score += 1
    if any(c.isupper() for c in pw): score += 1
    if any(c.isdigit() for c in pw): score += 1
    if any(c in "!@#$%" for c in pw): score += 1
    
    if score <= 2:
        return "❌ ضعيفة - بتتكسر في ثانية"
    elif score == 3:
        return "⚠️ متوسطة"
    else:
        return "✅ قوية جدا - آمنة"

print("=== Password Strength Checker ===")
pw = input("اكتب الباسورد العايز تفحصو: ")
print(check(pw))
