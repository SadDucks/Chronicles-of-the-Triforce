import sys;
from pathlib import Path;

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]));

from Deck import Combat;

class bot:
    def __init__(self, player, game):
        self.player = player;
        self.game = game;

    def getHand(self):
        return self.player.hand.cards;

    def getActiveCard(self):
        return self.player.activeCard;

    def getBench(self):
        return self.player.bench;

    def getEnergy(self):
        return self.player.energy;

    def getAttackOptions(self):
        options = [];

        if self.player.attacked:
            return options;

        candidates = [];

        if self.player.activeCard is not None:
            candidates.append(("active", self.player.activeCard));

        for location, attacker in candidates:
            if attacker.currentHealth <= 0:
                continue;

            target = self.chooseTarget(attacker);

            if target is None:
                continue;

            if attacker.energy > self.getEnergy():
                continue;

            damage = attacker.attack + getattr(attacker, "damageBoost", 0);
            damage = max(0, damage - getattr(target, "shield", 0));
            damage = min(damage, target.currentHealth);

            score = damage;

            if damage >= target.currentHealth and target.currentHealth > 0:
                score += 100;

            if attacker.currentHealth <= 5:
                score -=5;

            options.append({
                "card": attacker,
                "location": location,
                "target": target,
                "damage": damage,
                "energyCost": attacker.energy,
                "score": score
            });

        options.sort(key = lambda option: option["score"], reverse = True);

        return options;

    def getOpponents(self):
        opponents = [];

        for player in self.game.players:
            if player != self.player:
                opponents.append(player);

        return opponents;

    def hasAttacked(self):
        return self.player.attacked;

    def chooseActiveCard(self):
        if self.player.activeCard is None and len(self.player.bench) > 0:
            self.player.activeCard = self.player.bench.pop(0);
            self.player.activeCard.isActive = True;

    
    def chooseTarget(self, attacker):
        if attacker is None:
            return None;

        bestTarget = None;
        bestScore = float("-inf");

        for opponent in self.getOpponents():
            target = opponent.activeCard;

            if target is None or target.currentHealth <= 0:
                continue;

            score = self.evaluateTarget(
                attacker,
                target,
                opponent
            );

            if score > bestScore:
                bestScore = score;
                bestTarget = target;

        return bestTarget;


    
    def evaluateTarget(self, attacker, target, opponent):
        if target is None or target.currentHealth <= 0:
            return float("-inf");

        rawDamage = (attacker.attack + getattr(attacker, "damageBoost", 0));

        shield = getattr(target, "shield", 0);
        damage = min(max(0, rawDamage - shield), target.currentHealth);

        score = damage * 2

        if damage >= target.currentHealth:
            score += 100;

            if len(self.player.prizeCards) >= 5:
                score += 200;

        # Threat level
        score += len(opponent.prizeCards) * 20;

        # Damage efficiency
        score -= max(0, rawDamage - shield - target.currentHealth);

        return score;

    def playSupportCards(self):
        activeCard = self.player.activeCard;

        if activeCard is None:
            return;

        for card in self.player.hand.cards.copy():
            if not hasattr(card, "effects"):
                continue;

            shouldPlay = False;

            for effect in card.effects:
                effectType = effect["effectType"];
                amount = effect["amount"];

                if effectType == "energy":
                    shouldPlay = True;

                elif effectType == "healing":
                    missingHealth = (activeCard.health - activeCard.currentHealth);

                    if missingHealth >= amount and amount > 0:
                        shouldPlay = True;

                elif effectType == "damage_boost":
                    if amount > 0 and activeCard.energy <= self.player.energy:
                        shouldPlay = True;

                elif effectType == "shield":
                    if amount > 0 and getattr(activeCard, "shield", 0) < amount:
                        shouldPlay = True;

            if not shouldPlay:
                continue;

            Combat.applySupport(card, self.player);
            self.player.hand.removeCard(card);
            print("Bot played support card:", card.name);


    def takeTurn(self):

        print("TEST\n\n")#TEST

        self.chooseActiveCard();
        attacker = self.player.activeCard;

        if attacker is None:
            for card in self.player.hand.cards:
                if hasattr(card, "attack"):
                    self.player.activeCard = card;
                    self.player.hand.removeCard(card);
                    card.isActive = True;
                    print("Active card chosen:", self.player.activeCard.name);#TEST
                    attacker = card;
                    break;

        if attacker is None:
            print("No active card available, moving on.");
            return;
    
        self.playSupportCards();

        attackOptions = self.getAttackOptions();

        if not attackOptions:
            print("Bot has no legal attack.");
            return;

        bestAttack = attackOptions[0];
        attacker = bestAttack["card"];
        target = bestAttack["target"];

        if target is None:
            print("No target"); #TEST
            return;

        if self.player.energy < attacker.energy:
            print("Not enough energy!");#TEST
            return;

        self.player.energy -= attacker.energy;

        damage = Combat.attack(attacker, target);

        self.player.attacked = True;

        if target.currentHealth <= 0:
            target.currentHealth = 0;

        Combat.reportAttack(self.player, attacker, target, damage);
        if target.currentHealth == 0:
            defeatedPlayer = next(
                (
                    opponent for opponent in self.game.players
                    if opponent.activeCard is target
                ),
                None
            );
            if defeatedPlayer is None:
                raise RuntimeError("The defeated card has no owning player");
            self.game.resolveActiveCardDefeat(self.player, defeatedPlayer);