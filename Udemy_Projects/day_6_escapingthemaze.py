# DAY 6 - ESCAPING THE MAZE
# Run: python .\Udemy_Projects\day_6_escapingthemaze.py
# Related: day_6_assets\problem_world.json,
# Related: day_6_assets\problem_world2.json,
# Related: day_6_assets\problem_world3.json
#
# Note:
# This Day 6 challenge is meant for Reeborg's World.
# The real solution logic should be pasted into the Reeborg editor after
# loading one of the JSON world files there.
#
# These functions are built into Reeborg and are not defined locally:
# - move()
# - turn_left()
# - front_is_clear() / wall_in_front()
# - right_is_clear() / wall_on_right()
# - at_goal()
#
# The three provided JSON files use the same maze idea with different
# starting orientation, so one right-wall-following solution can be used
# for all of them.
#
# Paste the code below into Reeborg after loading:
# - problem_world.json
# - problem_world2.json
# - problem_world3.json


def turn_right():
    """Reeborg helper made from three left turns."""
    turn_left()
    turn_left()
    turn_left()


# Move until the robot reaches a wall or starts touching one on its right.
# This helps the right-wall-following logic start cleanly.
while front_is_clear() and right_is_clear():
    move()


# Follow the wall on the right until the goal is reached.
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
