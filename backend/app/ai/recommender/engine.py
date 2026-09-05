from app.database.demo_data import DESTINATIONS

def score(place, budget, interests):
    match = len(set(x.lower() for x in interests) & set(place['tags'])) / max(len(interests), 1)
    budget_fit = max(0, 1 - max(place['average_cost'] - budget / 3, 0) / max(budget / 3, 1))
    rating = place['rating'] / 5
    hidden = place['hidden_gem_score'] / 100
    crowd = place['crowd_score'] / 100
    value = .30*match + .18*budget_fit + .17*rating + .25*hidden - .10*crowd
    reasons=[]
    if match: reasons.append('Matches your ' + ', '.join(interests[:2]) + ' interests')
    if place['crowd_score'] < 45: reasons.append('Lower estimated crowd than popular alternatives')
    if place['average_cost'] * 3 <= budget: reasons.append('Fits the estimated trip budget')
    if place['hidden_gem_score'] > 75: reasons.append('Strong hidden-gem score with local value')
    return round(value*100,1), reasons

def recommend(budget, interests):
    ranked=[]
    for p in DESTINATIONS:
        s, why = score(p,budget,interests); ranked.append({**p,'recommendation_score':s,'why_recommended':why})
    return sorted(ranked,key=lambda x:x['recommendation_score'],reverse=True)

def crowd_alternative(destination, budget, interests):
    source=next((x for x in DESTINATIONS if x['id']==destination.lower() or x['name'].lower()==destination.lower()), DESTINATIONS[0])
    options=[x for x in recommend(budget,interests) if x['id']!=source['id'] and x['crowd_score'] < source['crowd_score']]
    return {'popular_destination':source, 'alternative':options[0] if options else None, 'notice':'Crowd levels are context-based estimates from demo/historical data, not live detection.'}
