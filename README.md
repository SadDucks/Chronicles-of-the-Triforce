# COSC-1301-Project

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
