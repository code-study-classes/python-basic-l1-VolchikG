load = [10, 50, 20, 80, 30, 90, 40, 60, 10, 20]
print(f"Исходная нагрузка: {load}")

smoothed_load = []

for i in range(len(load)-2):
    window = load[i:i+3]
    average = sum(window) // 3
    smoothed_load.append(round(average,1))

print(f"Сглаженный тренд: {smoothed_load}")
