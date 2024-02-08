# https://ru.hexlet.io/challenges/python_declarative_programming_team_stats_exercise

from collections.abc import Iterable


def wins_by_team(iterable: Iterable) -> dict[str, set[str]]:
    return {
        team: {
            loser
            for winner, loser in iterable
            if winner == team
        }
        for team, _ in iterable
    }
