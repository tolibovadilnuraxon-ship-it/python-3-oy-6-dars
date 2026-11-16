from datetime import datetime

def bugungi_sana():
    return datetime.now().date()

def hozirgi_vaqt():
    return datetime.now().time().strftime("%H:%M:%S")

def yilni_aniqla(sana):
    if isinstance(sana, str):
        return datetime.strptime(sana, "%Y-%m-%d").year
    return sana.year
