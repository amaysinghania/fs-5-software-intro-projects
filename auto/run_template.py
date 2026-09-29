import matplotlib.pyplot as plt
from pid_template import make_car
from pid_template import update
from pid_template import calculate_desired_acceleration
from pid_template import acceleration_to_throttle_percentage

K_P = 1.4
K_I = 0.03
K_D = 0.1
 
STEPS = 550
 
car = make_car(desired_v=50.0, dt=0.1)

velocities = []
errors = []
times = []

while car["step"] < STEPS:
    desired_acceleration, error = calculate_desired_acceleration(car, K_P, K_I, K_D)
    throttle_percentage = acceleration_to_throttle_percentage(desired_acceleration)
    
    velocities.append(car["v"])
    errors.append(error)
    times.append(car["t"])

    update(car, throttle_percentage)

plt.plot(times, velocities, color="blue")
plt.plot(times, errors, color="red")

plt.plot(times, [car["desired_v"]] * len(times), color="green", linestyle="--")

# print(errors)
# print(velocities)

# print(times)

plt.show()