
def gravity(sprite, gravity_value=0.5):
    if sprite.is_touching_ground:
        sprite.y_acceleration = 0
        sprite.y_velocity = 0

    elif not sprite.is_touching_ground and sprite.y_velocity < 0:
        sprite.y_acceleration = gravity_value

    else:
        sprite.y_acceleration = gravity_value * 3

def friction(sprite, friction_value=0.05):
    if sprite.x_velocity != 0:
        sprite.x_velocity *= (1 - friction_value)

def update_physics(sprite):
    # Update the position based on velocity
    sprite.x_position += sprite.x_velocity
    sprite.y_position += sprite.y_velocity

    # Update the velocity based on acceleration
    sprite.x_velocity += sprite.x_acceleration
    sprite.y_velocity += sprite.y_acceleration
