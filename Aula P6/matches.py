def allmatches (teams):
    assert len(teams) >= 2, "Uhm, it requires two or more teams. Bestie, what are you doing with your life?"
    half_matches = []                           # Initialize a list named "half_matches"

    for team in teams:                          # For each team in the teams list...
        opponents = teams
        opponents.remove(team)                  # Set a list of opponents for each team.

        for opponent in opponents:
            t = (team, opponent)                # Create a tuple with a single match: the team and one of the opponents.
            half_matches.append(t)              # Add the tuple to "half_matches".
    
    reverse_matches = []                        # Initialize another list named "reverse_matches". The next lines are needed because two opponents play two times (i.e. ["FCP", "SCP"], ["SCP", "FCP"]).
    for match in half_matches:                  # For each match in the previous matches list...
        reverse_match = match[::-1]             # Reverse each tuple.
        reverse_matches.append(reverse_match)   # Add the newly-reversed tuple to "reverse_matches".

    matches = half_matches + reverse_matches    # Create a new list that is the sum of the previous two lists.

    return matches                              # Return the new list.
