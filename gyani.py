import re
from data import CAREERS, STREAMS

def by_code(code):
    return [c for c in CAREERS if code in c["streams"]]

def names(lst, k=15):
    return ", ".join(c["name"] for c in lst[:k])

INTERESTS = {
 r"draw|art|design|creative": ["Architect", "Fashion Designer", "Interior Designer", "UI/UX Designer", "Filmmaker, Director & Screenwriter"],
 r"cod|program|comput|ai\b|tech|app": ["Software Engineer", "AI & ML Engineer", "Data Scientist", "Cyber Security Expert", "Web & App Developer"],
 r"math|number|statist": ["Actuary", "Statistician / Operations Research Analyst", "Economist / Policy Analyst", "Data Scientist"],
 r"bio|doctor|health|medic": ["Doctor (MBBS)", "Dentist (BDS)", "Biotechnologist", "Physiotherapist", "Nursing Officer"],
 r"writ|book|story|news": ["Journalism & Mass Communication", "Content Writer & Editor", "Filmmaker, Director & Screenwriter"],
 r"travel|fly|world": ["Commercial Pilot", "Merchant Navy Officer", "Aviation: Cabin Crew & Airport Management", "Hotel & Hospitality Manager"],
 r"business|money|financ|bank": ["Chartered Accountant (CA)", "Investment Banker", "Business Management (BBA / MBA)", "Entrepreneur / Startup Founder"],
 r"help|people|social|mind": ["Clinical Psychologist / Counsellor", "Social Work (MSW) & CSR", "HR Manager", "Teacher & Professor"],
 r"law|court|govt|government|ias": ["Lawyer (Corporate & Litigation)", "Civil Services (IAS, IPS, IFS)"],
}

def reply(text):
    t = text.lower()
    if re.search(r"\b(hi|hello|hey|namaste)\b", t):
        return "Namaste! 🙏 I am Gyani Baba. Tell me your stream (PCM, PCMB, PCB, Commerce, Humanities) or an interest like coding, drawing or travel, and I will suggest careers."
    for c in CAREERS:
        parts = [p.strip() for p in re.split(r"[/()&:]", c["name"].lower()) if len(p.strip()) > 4]
        if any(p in t for p in parts):
            return "%s\nStudy path: %s\nEntrance exams: %s\nSalary: %s\nScope: %s" % (c["name"], c["path"], c["exams"], c["sal"], c["scope"])
    for key, code in (("pcmb", "x"), ("pcm", "m"), ("pcb", "b"), ("commerce", "c"), ("humanities", "h"), ("arts", "h")):
        if key in t:
            return "Careers after %s: %s.\nAsk me about any of them for details!" % (key.upper() if key.startswith("pc") else key.title(), names(by_code(code), 20))
    if re.search(r"highest|top salary|high pay|best paying|most paid", t):
        top = sorted(CAREERS, key=lambda c: -c["hi"])[:8]
        return "Highest paying careers on BhavishyaPath:\n" + "\n".join("• %s: %s" % (c["name"], c["sal"]) for c in top)
    for pat, lst in INTERESTS.items():
        if re.search(pat, t):
            return "Based on your interest, explore: " + ", ".join(lst) + ".\nAsk me about any one for details!"
    return "I can help with streams (PCM, PCMB, PCB, Commerce, Humanities), a career name (try 'Pilot' or 'CA'), your interests, or the highest paying careers. What would you like to know?"
