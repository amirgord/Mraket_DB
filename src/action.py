from persistence import *

import sys

def activitie(splittedline : list[str]):

    if len(repo.products.find(id = splittedline[0])) == 0:
        return
    product = repo.products.find(id = splittedline[0])[0]
    if product is None:
        return
    if product.quantity + int(splittedline[1]) < 0:
        return

    repo._conn.execute("UPDATE Products SET quantity = ? WHERE id = ?",
                (product.quantity + int(splittedline[1]), product.id))

    #insert the activitie
    repo._conn.execute("INSERT INTO activities VALUES (?, ?, ?, ?)",
                (splittedline[0], splittedline[1], splittedline[2], splittedline[3]))

def main(args : list[str]):
    inputfilename : str = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(", ")
            activitie(splittedline)
    

if __name__ == '__main__':
    main(sys.argv)
