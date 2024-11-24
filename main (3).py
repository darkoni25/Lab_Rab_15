import pandas as pd
import os
import matplotlib.pyplot as plt
file_path = "comptage_velo_2018.csv"

if os.path.exists(file_path):
    print("Файл знайдено, починаємо обробку...")

    data = pd.read_csv(file_path)

    data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')
    data['Month'] = data['Date'].dt.month
    data_numeric = data.drop(columns=['Date', 'Unnamed: 1'], errors='ignore').select_dtypes(include=['number'])
    data['Total_Count'] = data_numeric.sum(axis=1)
    monthly_counts = data.groupby('Month')['Total_Count'].sum().reset_index()
    most_popular_month = monthly_counts.loc[monthly_counts['Total_Count'].idxmax()]

    # Виведення результатів
    print("\nЗагальна кількість велосипедистів по місяцях:")
    print(monthly_counts)
    print("\nНайпопулярніший місяць:")
    print(f"Місяць: {int(most_popular_month['Month'])}, Кількість велосипедистів: {int(most_popular_month['Total_Count'])}")

    # Візуалізація даних
    plt.figure(figsize=(10, 6))
    plt.bar(monthly_counts['Month'], monthly_counts['Total_Count'], color='skyblue', edgecolor='black')
    plt.title('Кількість велосипедистів по місяцях у 2018 році', fontsize=14)
    plt.xlabel('Місяць', fontsize=12)
    plt.ylabel('Кількість велосипедистів', fontsize=12)
    plt.xticks(monthly_counts['Month'], labels=[
        'Січень', 'Лютий', 'Березень', 'Квітень', 'Травень', 
        'Червень', 'Липень', 'Серпень', 'Вересень', 'Жовтень', 
        'Листопад', 'Грудень'], rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

else:
    print("Файл не знайдено. Переконайтеся, що він у тій же папці, що й виконуваний файл.")
