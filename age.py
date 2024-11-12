from datetime import datetime, timedelta

# Date de naissance
date_naissance = datetime(2002, 7, 22)

# Date actuelle
aujourd_hui = datetime.now()

# Calcul de l'âge actuel
age_actuel = aujourd_hui.year - date_naissance.year
if (aujourd_hui.month, aujourd_hui.day) < (date_naissance.month, date_naissance.day):
    age_actuel -= 1

# Calcul de l'âge dans 10 ans
age_dans_10_ans = age_actuel + 10

# Affichage du résultat
print(f"Dans 10 ans vous aurez = {age_dans_10_ans} ans.")
