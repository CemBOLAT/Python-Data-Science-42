from load_csv import load
import matplotlib.pyplot as plt


def population_str_to_float(population: str) -> float:
    """
    Convert a population string to a float

    Args:
        population (str): The population string

    Returns:
        float: The population as a float

    Logic:
        - Check if the population string ends with "M"
        - Check if the population string ends with "K"
        - Convert the population string to a float
    """
    try:
        if population.endswith("M"):
            return float(population[:-1]) * 1e6
        elif population.endswith("K"):
            return float(population[:-1]) * 1e3
        return float(population)
    except ValueError:
        return 0.0


def main():
    try:
        min_year = 1800
        max_year = 2050
        counties = ["Turkey", "Germany", "United Kingdom"]
        dict_list = []
        dataset = load("population_total.csv")
        if dataset is None:
            raise AssertionError("Dataset cannot be loaded")

        country_data = dataset[dataset["country"] == counties[0]]
        years = country_data.columns[1:]
        years_int = []
        for year in years:
            year_int = int(year)
            if year_int >= min_year and year_int <= max_year:
                years_int.append(year_int)

        for country in counties:
            country_data = dataset[dataset["country"] == country]
            if country_data.empty:
                raise AssertionError(f"{country} data not found")

            population = []
            for i in range(1, len(years) + 1):
                pop = population_str_to_float(country_data.values[0][i])
                population.append(pop)

            dict_template = {
                "name": country,
                "population": population
            }
            dict_list.append(dict_template)

        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        print(range(min_year, max_year + 1, 40))
        plt.xticks(range(min_year, max_year + 1, 40), rotation=45)

        max_population = 0

        for data in dict_list:
            plt.plot(years, data["population"], label=data["name"])
            max_population = max(max_population, max(data["population"]))

        y_ticks = [i * 1e7 for i in range(int(max_population / 1e7) + 1)]
        plt.yticks(y_ticks, ["{:,.0f}M".format(pop / 1e6) for pop in y_ticks])
        plt.legend()
        plt.tight_layout()
        plt.show()
    except AssertionError as e:
        print(f"Assertion Error: {e}")
        return
    except ValueError as e:
        print(f"Value Error: {e}")
        return
    except KeyboardInterrupt:
        print("Process interrupted by the user")
        return


if __name__ == "__main__":
    main()
