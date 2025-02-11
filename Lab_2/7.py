import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temperatures = [30, 32, 31, 29, 28, 27, 26]

plt.plot(days, temperatures, marker='o', linestyle='-')
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Variations Over a Week")
plt.show()