
def gravity(sprite, gravity_value=0.5):
    if sprite.is_touching_ground:
        sprite.acceleration[1] = 0
        sprite.velocity[1] = 0

    elif not sprite.is_touching_ground and sprite.velocity[1] < 0:
        sprite.acceleration[1] = gravity_value

    else:
        sprite.acceleration[1] = gravity_value * 3

def friction(sprite, friction_value=0.05):
    if sprite.velocity[0] != 0:
        sprite.velocity[0] *= (1 - friction_value)

def update_physics(sprite):
    # Update the position based on velocity
    sprite.x_position += sprite.velocity[0]
    sprite.y_position += sprite.velocity[1]

    # Update the velocity based on acceleration
    sprite.velocity[0] += sprite.acceleration[0]
    sprite.velocity[1] += sprite.acceleration[1]
