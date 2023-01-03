from csv import DictReader
from sklearn.neighbors import KNeighborsRegressor

def main():
    x_values = []
    y_values = []
    track_records = [61.808, 69.809, 70.5, 57.618, 60.912, 61.808, 55.378]

    for round_num in range(6):
        with open('Rounds/round' + str(round_num + 1) + '.csv', 'r', encoding='UTF-8') as file:
            reader = DictReader(file)

            for row in reader:
                if float(row['Best Lap time']) != 0:
                    x_values.append([int(row['Number']), track_records[round_num]])
                    y_values.append(float(row['Best Lap time']))

    neigh = KNeighborsRegressor(n_neighbors = 5)
    neigh.fit(x_values, y_values)
    print(neigh.predict([[57, 72.672]]))

if __name__ == '__main__':
    main()
