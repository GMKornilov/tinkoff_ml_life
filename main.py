import field
import argparse
import colored
from time import sleep

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-probas", nargs=4, help="Probabilities of appearing empty cell, fish cell, shrimp cell and rock cell(sum should be 1)", required=True)
    parser.add_argument("-size", type=int, help="Size of field", required=True)
    parser.add_argument("-seed", type=int, default=200)

    args = parser.parse_args()._get_kwargs()

    for i in args:
        print(i)

    probas = [float(i) for i in args[0][1]]
    seed = args[1][1]
    size = args[2][1]

    print(probas)
    lifeField = field.LifeField(size, seed, probas)
    while True:
        lifeField.Visualize()
        lifeField.Proccess()
        sleep(1)
        colored.ClearScreen()