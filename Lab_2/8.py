regions = ["North", "South", "East", "West"]
sales_revenue = [50000, 60000, 45000, 70000]

plt.bar(regions, sales_revenue, color=['blue', 'red', 'green', 'purple'])
plt.xlabel("Regions")
plt.ylabel("Sales Revenue")
plt.title("Sales Revenue Comparison")
plt.show()