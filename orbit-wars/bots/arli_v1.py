from kaggle_environments.envs.orbit_wars.orbit_wars import Planet, Fleet
import math

"""
Arli V1: The Baseline Bot
Strategy:
- Scan planets; determine which ones are mine and which ones are not
- Determine my strongest planet and the weakest planet not mine
- Plan an attack on the weakest planet by checking if strongest ship count > weakest ship count
- Add a little bit of margin to not exhaust strongest planet too much
- Launch half # of ships if plausible

"""

def agent(obs):
    planets = [Planet(*p) for p in obs.get("planets", [])]
    player_id = obs.get("player", 0)
    actions = []

    my_planets = [p for p in planets if p.owner == player_id]
    other_planets = [p for p in planets if p.owner != player_id]

    if not my_planets or not other_planets:
        return actions

    my_strongest = max(my_planets, key=lambda p: p.ships)
    weakest_target = min(other_planets, key=lambda p: p.ships)

    if my_strongest.ships > weakest_target.ships + 5:
        dx = weakest_target.x - my_strongest.x
        dy = weakest_target.y - my_strongest.y
        angle = math.atan2(dy, dx)

        ships_to_send = my_strongest.ships // 2

        actions.append([my_strongest.id, angle, ships_to_send])

    return actions