#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np
import random as r

# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values() -> np.ndarray:
    return np.linspace(-1.3,2.5,64)


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:
    polar_coordinates = []
    for i in cartesian_coordinates:
        r = np.sqrt(i[0] ** 2 + i[1] ** 2)
        t = np.arctan2(i[1], i[0])
        polar_coordinates.append((r,t))
    return polar_coordinates
def polar(cartesian_coordinates: np.ndarray):

    a = np.zeros([len(cartesian_coordinates), 2])

    for i in range(len(cartesian_coordinates)):
        rho = np.sqrt(cartesian_coordinates[i][0] ** 2 + cartesian_coordinates[i][1] ** 2)

        phi = np.arctan2(cartesian_coordinates[i][1], cartesian_coordinates[i][0])

        polar_coordinate = (rho, phi)

        a[i] = polar_coordinate

    return np.array([a])

def find_closest_index(values: np.ndarray, number: float) -> int:
    differences = []
    for i in values:
        differences.append(abs(i - number))
    
    return differences.index(min(differences))


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    # for value in linear_values():
    #     print(value)
    print(coordinate_conversion([(0,0),(1,1),(2,2),(3,3)]))
    print(polar([(0,0),(1,1),(2,2),(3,3)]))
    #print(find_closest_index([4,1,7,2,3,10,5,9,100,65,56,78],60))


