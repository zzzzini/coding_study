def solution(bandage, health, attacks):
    answer = 0
    spree = 1
    max_health = health
    time = []
    for items in attacks:
        time.append(items[0])

    for i in range(attacks[len(attacks)-1][0]):
        if (i+1) not in time:
            if max_health == health:
                continue
            else:
                if spree == bandage[0]:
                    health += bandage[1]
                    health += bandage[2]
                    spree = 1
                else:
                    health += bandage[1]
                    spree += 1
        else:
            health -= attacks[time.index(i+1)][1]
            spree = 1

        if health >= max_health:
            health = max_health
            answer = health

        elif health > 0 and health < max_health:
            answer = health

        elif health <= 0:
            answer = -1
            break
    return answer