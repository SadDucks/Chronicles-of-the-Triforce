def attack(attacker, defender):
    damage = attacker.attack + getattr(attacker, "damageBoost", 0);

    shield = getattr(defender, "shield", 0);

    print("Defender:", defender.name) # Test line
    print("Shield before attack:", shield) # Test line

    absorbed = min(damage, shield);
    damage -= absorbed;
    defender.shield = shield - absorbed;

    defender.currentHealth = max(0, defender.currentHealth - damage);
    attacker.damageBoost = 0;

    return damage;

def reportAttack(player, attacker, defender, damage):
    if defender.currentHealth <= 0:
        print("target defeated");

    print("Attacker: ", attacker.name, " dealt ", damage, " damage to ", defender.name);
    print("Target health: ", defender.currentHealth, "/", defender.health);
    print("Attacker health: ", attacker.currentHealth, "/", attacker.health);
    print("Player energy: ", player.energy);

def heal(card, amount):
    card.currentHealth = min(card.currentHealth + amount, card.health);


def applySupport(supportCard, player):

    print("DEBUG: applySupport was called\n\n\n") # Test line

    activeCard = player.activeCard;

    for effect in supportCard.effects:
        effectType = effect["effectType"];
        amount = effect["amount"];
        duration = effect["duration"];

        if effectType == "healing" and duration == "instant":
            if activeCard is not None:
                heal(activeCard, amount);

        elif effectType == "energy" and duration == "instant":
            player.energy += amount;

        elif effectType == "damage_boost" and duration == "next_attack":
            if activeCard is not None:
                activeCard.damageBoost += amount;

        elif effectType == "shield" and duration == "next_incoming_attack":
            if activeCard is not None:
                activeCard.shield += amount;

        else:
            raise ValueError(f"Unknown support effect: {effect}");

    print("Shield after support:", activeCard.shield if activeCard is not None else "No active card") # Test line