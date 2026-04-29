import random, string, datetime

DEPARTMENTS = [
    "Road & Traffic management Department",
    "Solid Waste Management",
    "Electric Department",
    "Water Supply Department",
    "Sewage & Drainage Department",
    "Encroachment Department"
]

STATUS_LIST = ["Pending", "In Progress", "Resolved", "Escalated"]

SAMPLE_COMPLAINTS = [
    {"id": "LK-2024-0001", "text": "Large pothole on main road near station, causing accidents.",
     "dept": "Roads", "status": "In Progress", "date": "2024-11-05", "location": "Station Road",
     "priority": "High", "image": False},
    {"id": "LK-2024-0002", "text": "No water supply for 3 days in sector 7.",
     "dept": "Water Supply", "status": "Resolved", "date": "2024-11-06", "location": "Sector 7",
     "priority": "High", "image": False},
    {"id": "LK-2024-0003", "text": "Garbage not collected for over a week.",
     "dept": "Sanitation", "status": "Pending", "date": "2024-11-07", "location": "Ward 12",
     "priority": "Medium", "image": True},
    {"id": "LK-2024-0004", "text": "Street light broken for two weeks near school.",
     "dept": "Electricity", "status": "Escalated", "date": "2024-11-08", "location": "MG School Road",
     "priority": "Medium", "image": False},
    {"id": "LK-2024-0005", "text": "Sewage overflow on residential street.",
     "dept": "Drainage", "status": "In Progress", "date": "2024-11-09", "location": "Shivaji Nagar",
     "priority": "High", "image": True},
    {"id": "LK-2024-0006", "text": "Park benches damaged and dangerous for children.",
     "dept": "Parks & Gardens", "status": "Pending", "date": "2024-11-10", "location": "Central Park",
     "priority": "Low", "image": False},
    {"id": "LK-2024-0007", "text": "Illegal construction blocking public walkway.",
     "dept": "Building & Permits", "status": "In Progress", "date": "2024-11-11", "location": "Tilak Road",
     "priority": "High", "image": True},
    {"id": "LK-2024-0008", "text": "Dead animals lying on road near market, health hazard.",
     "dept": "Public Health", "status": "Resolved", "date": "2024-11-12", "location": "Bazaar Road",
     "priority": "High", "image": False},
]

def generate_complaint_id():
    year = datetime.datetime.now().year
    suffix = ''.join(random.choices(string.digits, k=4))
    return f"LK-{year}-{suffix}"

def classify_complaint(text: str) -> str:
    """Mock ML classification – replace with real API call to ml-service."""
    keywords = {
        "Roads": ["road", "pothole", "path", "footpath", "highway", "street", "crack", "bump"],
        "Water Supply": ["water", "pipe", "supply", "tap", "leak", "borewell", "tanker"],
        "Sanitation": ["garbage", "waste", "trash", "litter", "dirty", "clean", "dump"],
        "Electricity": ["light", "electricity", "power", "electric", "street light", "wiring"],
        "Drainage": ["drain", "sewage", "flood", "overflow", "waterlogging", "sewer"],
        "Parks & Gardens": ["park", "garden", "tree", "bench", "playground", "grass"],
        "Building & Permits": ["construction", "building", "illegal", "permit", "encroachment"],
        "Public Health": ["health", "hospital", "disease", "animal", "mosquito", "epidemic", "stray"],
        "Fire Safety": ["fire", "smoke", "hazard", "explosion", "gas"],
        "Solid Waste": ["solid", "bin", "container", "collection", "segregation"],
    }
    text_lower = text.lower()
    scores = {dept: sum(1 for kw in kws if kw in text_lower) for dept, kws in keywords.items()}
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "General"

def get_complaints_for_dept(dept: str):
    if dept == "All":
        return SAMPLE_COMPLAINTS
    return [c for c in SAMPLE_COMPLAINTS if c["dept"] == dept]

def status_badge(status: str) -> str:
    cls = {"Pending": "badge-pending", "In Progress": "badge-progress",
           "Resolved": "badge-resolved", "Escalated": "badge-escalate"}.get(status, "badge-pending")
    return f'<span class="badge {cls}">{status}</span>'

def priority_icon(p):
    return {"High": "🔴", "Medium": "🟡", "Low": "🟢"}.get(p, "⚪")
