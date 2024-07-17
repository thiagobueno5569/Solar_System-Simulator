import random
import math
import time
import turtle
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from solarsystem import SolarSystem, Sun, Planet

# Constantes físicas
G = 6.67430e-11
AU = 149.6e9


def orbital_velocity(mass, distance):
    return math.sqrt(G * mass / distance)


solar_system = SolarSystem(width=1900, height=900)  # Tamanho inicial da tela


sun = Sun(solar_system, mass=1.989e30, position=(0, 0, 0), velocity=(0, 0, 0))  # Massa real do Sol

# Adicionando planetas
planet_data = [
    {"name": "Terra", "mass": 5.39e23, "distance": 1 * AU, "initial_velocity": None},  # Terra
    {"name": "Marte", "mass": 6.39e23, "distance": 1.52 * AU, "initial_velocity": None},  # Marte
    {"name": "Mercúrio", "mass": 3.285e23, "distance": 0.39 * AU, "initial_velocity": None},  # Mercúrio
    # Adicione mais planetas conforme desejado
]

planets = []
for data in planet_data:
    initial_velocity = data["initial_velocity"] if data["initial_velocity"] is not None else orbital_velocity(sun.mass, data["distance"])
    angle = random.uniform(0, 2 * math.pi)
    x = data["distance"] * math.cos(angle)
    y = data["distance"] * math.sin(angle)
    z = 0
    planets.append(
        Planet(solar_system, mass=data["mass"], position=(x, y, z), velocity=(4000000000,initial_velocity,400000))
    )

def adjust_sleep_time():
    global sleep_time
    new_sleep_time = float(turtle.textinput("Ajustar tempo de pausa", "Digite o novo tempo de pausa (segundos):"))
    sleep_time = new_sleep_time


turtle.listen()
turtle.onkeypress(adjust_sleep_time, "s")

sleep_time = 0.001


fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Loop principal da simulação
while True:
    solar_system.calculate_all_body_interactions()
    solar_system.update_all()

    for i, planet in enumerate(planets):
        positions = planet.history
        x_values = [pos[0] for pos in positions]
        y_values = [pos[1] for pos in positions]
        z_values = [pos[2] for pos in positions]

        ax.plot(x_values, y_values, z_values, label=f'{planet_data[i]["name"]}')

    x, y, z = sun.position()
    ax.scatter(x, y, z, color='yellow', s=100, label='Sol')

    ax.set_title('Trajetória dos Planetas no Sistema Solar')
    ax.set_xlabel('Posição X (m)')
    ax.set_ylabel('Posição Y (m)')
    ax.set_zlabel('Posição Z (m)')
    ax.legend()
    ax.grid(True)
    plt.pause(0.001)
    ax.clear()  # Limpar o gráfico para a próxima atualização

    time.sleep(sleep_time)  # Atraso ajustável entre cada atualização do quadro
