# Beginner - Python Functions & Karel

## Learning Outcomes

- Learning how to use functions



The coding challenges today used [Reeborg's hurdle challenge](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json)s 1-4:


- Hurdle 4 was a fun challenge!


```python
# Make a jump function
def turn_right():
    turn_left()
    turn_left()
    turn_left()



# front_is_clear
# wall_in_front
# at_goal
# wall_on_right()

# if there is a wall in front
#     turn right (keep going)
# if there is no wall in front
#     move
right_turns = 0
while not at_goal():

    if not wall_on_right():

        turn_right()
        right_turns += 1
        move()
        if right_turns > 3:
            move()
            right_turns = 0
    elif not wall_in_front():
        move()
    else:
        turn_left()

```

