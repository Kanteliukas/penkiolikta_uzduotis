def main():

    year_from = input("Įveskite metus nuo: ")
    year_from = int(year_from)
    year_to = input("Įveskite metus iki: ")
    year_to = int(year_to)

    set_range = range(year_from, year_to + 1)

    leap_year_results = [year for year in set_range if calendar.isleap(year)]
    print(leap_year_results)

main()