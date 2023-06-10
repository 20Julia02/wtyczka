#%%
import numpy as np
from scipy.spatial import Delaunay

x = [1,2,3]
y = [4,6,7]


coordinate_list = []

for xx,yy in zip(x,y):
    coordinate_list.append([xx, yy])
coordinate_array = np.array([coordinate_list])
triangulation = Delaunay(coordinate_array)
total_area = 0.0

# Iteruj po trójkątach w triangulacji
for triangle in triangulation.simplices:
    # Pobierz współrzędne wierzchołków trójkąta
    A = coordinate_array[triangle[0]]
    B = coordinate_array[triangle[1]]
    C = coordinate_array[triangle[2]]

    cross_product = np.cross(B - A, C - A)
    area = 0.5 * np.linalg.norm(cross_product)

    # Dodaj pole trójkąta do sumy
    total_area += area
# figure = QgsGeometry().fromPolygonXY([list_xy_coordinates])
# area = figure.area()
result_area = f"{total_area:.3f} m2"
print(result_area)

        

#%%

if len(selected_features) >= 3:
            x_coordinates = []
            y_coordinates = []

            for feature in selected_features:
                point_attributes = feature.attributes()
                x_coordinate = point_attributes[0]
                y_coordinate = point_attributes[1]
                x_coordinates.append(x_coordinate)
                y_coordinates.append(y_coordinate)

            list_xy_coordinates = []

            for x,y in zip(x_coordinates, y_coordinates):
                
                 xy_coordinate = [x,y]
                 list_xy_coordinates.append(xy_coordinate)

            results = []

            for number in range(1,len(list_xy_coordinates)+1):
                print(number)
                if number == len(list_xy_coordinates):
                    print("jestem")
                    prepared_x = list_xy_coordinates[0][0] + list_xy_coordinates[-1][0]
                    prepared_y = list_xy_coordinates[0][1] - list_xy_coordinates[-1][1]
                    result = prepared_x * prepared_y
                    results.append(result)
                else:
                    print("lol")
                    prepared_x = list_xy_coordinates[number][0] + list_xy_coordinates[number-1][0]
                    prepared_y = list_xy_coordinates[number][1] - list_xy_coordinates[number-1][1]
                    
                    result = prepared_x * prepared_y
                    results.append(result)

            final_area = abs(sum(results)/2)

            # figure = QgsGeometry().fromPolygonXY([list_xy_coordinates])
            # area = figure.area()
            result_area = f"{final_area:.3f} m2"
            self.result_label.setText(str(result_area))
    
            # print(f"Powierzchnia trójkąta: {area:.2f} m2")
        else:
            error = "Zaznacz przynajmniej trzy punkty."
            self.result_label.setText(str(error))
