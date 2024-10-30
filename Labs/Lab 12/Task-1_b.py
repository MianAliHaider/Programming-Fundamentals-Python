from random import *

def print_shortest_distance(d, city1, city2):
    distance = d[city1][city2]
    via = city1
    is_direct = True

    # Check if there's a shorter indirect route
    for i in range(len(d)):
        if i != city1 and i != city2:
            indirect_distance = d[city1][i] + d[i][city2]
            if distance > indirect_distance:
                distance = indirect_distance
                via = i
                is_direct = False

    # Print the result
    if is_direct:
        print(f"Shortest distance between city {city1 + 1} and city {city2 + 1} is {distance}.")
        print("The distance is direct.")
    else:
        print(f"Shortest distance between city {city1 + 1} and city {city2 + 1} is {distance} via city {via + 1}.")

def main():
    LENGTH = randint(5, 6)
    d = [[randint(1, 9) for i in range(LENGTH)] for j in range(LENGTH)]

    # Print the distance matrix
    print("Distance matrix:")
    for i in range(len(d)):
        for j in range(len(d)):
            print(d[i][j], end=" ")
        print()

    # Set distance from a city to itself as 0
    for i in range(LENGTH):
        d[i][i] = 0

    # Print shortest distance between all pairs of cities
    print("\nShortest distances:")
    for i in range(LENGTH):
        for j in range(LENGTH):
            if i != j:
                print_shortest_distance(d, i, j)

main()
