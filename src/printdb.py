from persistence import *

def main():

    # print the tables nicely
    print("Activities")
    for row in repo._conn.cursor().execute("SELECT * FROM activities ORDER BY date ASC"):
        print(row)

    print("Branches")
    for row in repo._conn.cursor().execute("SELECT * FROM branches ORDER BY id ASC"):
        print(row)

    print("Employees")
    for row in repo._conn.cursor().execute("SELECT * FROM employees ORDER BY id ASC"):
        print(row)

    print("Products")
    for row in repo._conn.cursor().execute("SELECT * FROM products ORDER BY id ASC"):
        print(row)

    print("Suppliers")
    for row in repo._conn.cursor().execute("SELECT * FROM suppliers ORDER BY id ASC"):
        print(row)

    print("\nEmployees report")
    for row in repo.employees_report():
        print("{0} {1} {2} {3}".format(row[0], row[1], row[2], row[3]))

    print("\nActivities report")
    for row in repo.activities_report():
        print(row)

if __name__ == '__main__':
    main()