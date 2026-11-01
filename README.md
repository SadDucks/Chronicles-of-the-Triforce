# Chronicles of the Triforce

## Installation

### Releases

Go to the [Releases](https://github.com/SadDucks/COSC-1301-Project/releases)
page and download the build for your operating system. Extract the download if
needed, then open the game application.

### Building It Yourself

You will need **Python 3.10 or newer** and an internet connection to install
the required packages. From a terminal, clone the repository, install the
dependencies, and start the game:

```shell
git clone https://github.com/SadDucks/COSC-1301-Project.git
cd COSC-1301-Project
python -m pip install PySide6 setproctitle
python launcher.py
```

Run the final command from the project directory so the game can find its
assets and configuration file.

## How to play

### Goal

Defeat opponents' active character cards to earn prize cards. The first player
to collect **6 prize cards** wins.

### Cards and setup

- Each player starts with **10 energy** and **5 cards**.
- **Attack cards** are characters with health, an attack value, and an energy
  cost. Each player can have one active attack card at a time.
- **Support cards** are one-use items. They can restore health or energy,
  strengthen your next attack, or shield you from incoming damage. Playing a
  support card does not cost energy; its effects are applied immediately or
  last until the next attack they affect.
- **Prize cards** are awarded when you defeat an opponent's active card.

### Taking a turn

1. On your first turn, click an attack card in your hand and choose **Set
   Active**. This sets your character and ends your setup turn.
2. On later turns, you may set an attack card active, replacing your current
   one, and use support cards from your hand.
3. To attack, click your active card, choose **Attack**, then click an
   opponent's active card. You can attack once per turn, after the setup round,
   and only if you have enough energy to pay that character's cost.
4. End your turn with **End Turn**. You gain **8 energy** if you attacked, or
   **3 energy** if you did not. You then draw a card, if the deck and your hand
   have room. Your hand can hold up to **8 cards**.

Attacks reduce the target's health. Shields absorb damage first. At **0
health**, the active card is discarded and the attacker earns a prize card;
the defeated player can set a new character active on a later turn. If you run
out of energy, use support cards or wait for your end-of-turn energy.

### Controls

- Click a card in your hand to preview it and show its available actions.
- Choose **Set Active** on an attack card to make it your character.
- Choose **Use** on a support card to play it.
- Choose **Attack**, then select an opponent's active card as the target.
- Use **End Turn** to finish your turn. **Score** shows the players' prize
  cards.

## Multiplayer

Multiplayer games are hosted over a local network. One player hosts the session
and starts the game after at least one other player has joined. The game
supports up to four players total: the host, up to three guests, and bots in
any remaining seats.

### Host a game

1. Open Multiplayer from the main menu and choose **Host a Game**.
2. Keep the lobby open while other players join. The lobby shows the host's
   available network addresses and connected players.
3. Select **Start Game** once at least one guest has joined.

### Join a game

1. Open Multiplayer from the main menu and choose **Join a Game**.
2. Choose a discovered game from the list, or enter the host's IP address or
   computer name and select **Join by Address**.
3. Wait in the lobby until the host starts the game.

Automatic discovery works for players on the same local network. If the host
does not appear, use **Join by Address** with the IP address shown in the
host's lobby. Connections must be allowed through the host computer's firewall
on the private network.

The game uses TCP port `55555` for player connections and UDP port `55556` for
local-network game discovery. Direct-address joining uses the TCP connection;
automatic discovery additionally requires UDP discovery traffic to be allowed.

## Credits

To see the credits for this project go you [Credits](https://github.com/SadDucks/Chronicles-of-the-Triforce/blob/main/CREDITS.md)
