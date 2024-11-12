from datetime import datetime

def calculer_age(date_naissance):
    """Calcule l'âge actuel à partir de la date de naissance."""
    aujourd_hui = datetime.now()
    age = aujourd_hui.year - date_naissance.year
    # Vérifie si l'anniversaire est déjà passé cette année
    if (aujourd_hui.month, aujourd_hui.day) < (date_naissance.month, date_naissance.day):
        age -= 1
    return age

def age_dans_x_ans(date_naissance, annees=10):
    """Calcule l'âge dans un nombre donné d'années."""
    age_actuel = calculer_age(date_naissance)
    return age_actuel + annees

def temps_depuis_majorite(date_naissance):
    """Calcule le nombre d'années depuis la majorité (18 ans)."""
    age_actuel = calculer_age(date_naissance)
    if age_actuel > 18:
        return age_actuel - 18
    else:
        return 0  # Pas encore majeur

def temps_depuis_permis(date_permis):
    """Calcule le temps écoulé depuis l'obtention du permis."""
    aujourd_hui = datetime.now()
    annees = aujourd_hui.year - date_permis.year
    mois = aujourd_hui.month - date_permis.month
    jours = aujourd_hui.day - date_permis.day

    # Ajustement pour les mois et jours négatifs
    if jours < 0:
        mois -= 1
        jours += 30  # Approximation du nombre de jours par mois
    if mois < 0:
        annees -= 1
        mois += 12

    return annees, mois

# Exemple d'utilisation
date_naissance = datetime(2002, 7, 22)
age_plus_10 = age_dans_x_ans(date_naissance, 10)

print(f"Dans 10 ans vous aurez = {age_plus_10} ans.")

# Vérifie si l'utilisateur est majeur et calcule le nombre d'années depuis la majorité
temps_majorite = temps_depuis_majorite(date_naissance)
if temps_majorite > 0:
    print(f"Cela fait {temps_majorite} ans que vous êtes majeur(e).")

# Demande à l'utilisateur la date d'obtention de son permis
date_permis_str = input("Entrez la date d'obtention de votre permis (au format JJ/MM/AAAA) : ")
date_permis = datetime.strptime(date_permis_str, "%d/%m/%Y")

# Calcul du temps écoulé depuis l'obtention du permis
annees_permis, mois_permis = temps_depuis_permis(date_permis)
print(f"Cela fait {annees_permis} ans et {mois_permis} mois que vous avez le permis.")
