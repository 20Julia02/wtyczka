x = []
y = []
z = []

with open("pros.txt", 'r') as file:
    for line in file.readlines():
        line = line.replace("\n", "")  # Usunięcie znaku nowej linii
        values = line.split(";")
        for _ in values:
            values[2] = values[2].replace("\n", "")  # Usunięcie znaku nowej linii
        x.append(values[0])
        y.append(values[1])
        z.append(values[2])

print(z)


    def get_data_from_file(self):
        selected_file = self.sciezka.filePath()
        x = []
        y = []
        z = []

        with open(selected_file, 'r') as file:
            for line in file.readlines():
                line = line.replace("\n", "")  # Usunięcie znaku nowej linii
                values = line.split(";")
                for _ in values:
                    values[2] = values[2].replace("\n", "")  # Usunięcie znaku nowej linii
                x.append(values[0])
                y.append(values[1])
                z.append(values[2])
        return x,y,z