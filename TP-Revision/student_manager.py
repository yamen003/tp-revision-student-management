def calculate_average(grades):
    """Retourne la moyenne d'une liste de notes. ValueError si la liste est vide."""
    if len(grades) == 0:
        raise ValueError("La liste de notes est vide")
    return sum(grades) / len(grades)


def get_mention(average):
    """Retourne la mention correspondant à la moyenne."""
    if average < 10:
        return "Échec"
    elif average < 12:
        return "Passable"
    elif average < 14:
        return "Assez bien"
    elif average < 16:
        return "Bien"
    elif average < 18:
        return "Très bien"
    else:
        return "Excellent"


def is_admitted(average):
    """True si la moyenne est >= 10, sinon False."""
    return average >= 10


def validate_grades(grades):
    """False si liste vide ou si une note est hors de [0, 20], sinon True."""
    if len(grades) == 0:
        return False
    return all(0 <= g <= 20 for g in grades)


if __name__ == "__main__":
    notes = [12, 15, 18]
    average = calculate_average(notes)
    print("Moyenne :", average)
    print("Mention :", get_mention(average))
    print("Admis :", is_admitted(average))
    print("Notes valides :", validate_grades(notes))
