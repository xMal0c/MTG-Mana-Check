def HasEnoughMana(manapool, manacost):
    manapool_counts = {color: manapool.count(color) for color in 'WUBRGC'}

    #Manan tarkastus / kustannus
    if manacost and manacost[0].isdigit():
        generic_cost, specific_cost = int(manacost[0]), manacost[1:]
    else:
        generic_cost, specific_cost = 0, manacost

    #Manan vähennys
    for color in specific_cost:
        if manapool_counts[color] > 0:
            manapool_counts[color] -= 1
        else:
            return False



    #Manan kustannus / neutraali (mikä tahansa väri)
    total_remaining_mana = sum(manapool_counts.values())
    if total_remaining_mana < generic_cost:
        return False #Jos ei riitä
    return True

print(HasEnoughMana("RRRR", "2RR"))
print(HasEnoughMana("WRUGB", "3WW"))