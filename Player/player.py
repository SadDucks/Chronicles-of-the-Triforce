from Deck.deck import hand;

# Creates players
class player:
    def __init__(self, name, isBot):
        self.name = name;
        self.isBot = isBot;
        self.bot = None;
        self.hand = hand();
        self.activeCard = None;
        self.bench = [];
        self.prizeCards = [];
        self.energy = 10;
        self.attacked = False;
        self.selectedCards = None;
        self.round = 1;

    # Sets Active Cards

    def setActiveCard(self, card):
        self.activeCard = card;

    # Adds Cards to Bench

    def addToBench(self, card):
        self.bench.append(card);

    # Gives Players Prize Cards

    def addPrizeCard(self, card):
        self.prizeCards.append(card);
    
    def getEnergy(self):
        return self.energy;

    def applySupportCard(self, support):
        activeCard = self.activeCard;

        print("Support card:", support.name); # Test line

        for effect in support.effects:
            effectType = effect["effectType"];
            amount = effect["amount"];
            duration = effect["duration"];

            if effectType == "energy" and duration == "instant":
                self.energy += amount;

            elif effectType == "healing" and duration == "instant":
                if activeCard is not None:
                    activeCard.currentHealth = min(
                        activeCard.currentHealth + amount,
                        activeCard.health
                    )

            elif effectType == "damage_boost" and duration == "next_attack":
                if activeCard is not None:
                    activeCard.damageBoost += amount;

            elif effectType == "shield" and duration == "next_incoming_attack":
                if activeCard is not None:
                    activeCard.shield += amount;

            else:
                raise ValueError(f"Unknown support effect: {effect}");

        # Test lines
        if activeCard is not None:
            print("Card damage boost:", activeCard.damageBoost);
            print("Card shield:", activeCard.shield);

    # Selects Cards

    def selectCard(self, card):
        if self.selectedCards == card:
            self.selectedCards = None;
        else:
            self.selectedCards = card;