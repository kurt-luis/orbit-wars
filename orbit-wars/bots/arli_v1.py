from kaggle_environments.envs.orbit_wars.orbit_wars import Planet, Fleet, CENTER, ROTATION_RADIUS_LIMIT


def agent(obs):
    planets = [Planet(*p) for p in obs.get("planets", [])]
    fleets = [Fleet(*f) for f in obs.get("fleets", [])]
    player_id = obs.get("player", 0)

    for p in planets:
        # print(p.id, p.owner, p.x, p.y, p.radius, p.ships, p.production)
        pass

    actions = []
    # ------------------------------------------------------------------------
    # Strategy logic
    # Which planets are mine, what to attack, the angle to launch fleets, etc.
    # ------------------------------------------------------------------------

    # Return [from_planet_id, angle, num_ships]
    return actions