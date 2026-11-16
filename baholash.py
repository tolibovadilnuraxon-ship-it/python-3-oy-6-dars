def baho_aniqla(ball):
    if 90 <= ball <= 100:
        return "A'lo"
    elif 70 <= ball <= 89:
        return "Yaxshi"
    elif 50 <= ball <= 69:
        return "Qoniqarli"
    elif 0 <= ball <= 49:
        return "Qoniqarsiz"
    return "Noto'g'ri ball"

def ortacha_hisobla(balllar):
    return sum(balllar) / len(balllar) if balllar else 0

def eng_yaxshi_ball(balllar):
    return max(balllar) if balllar else 0
