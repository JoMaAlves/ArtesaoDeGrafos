from menu import printMenu
from graph import *


start, direc, valor = printMenu(0)

graph = graph(direc, valor)

while start:
    answer = printMenu(1)

    if answer == "0":
        break

