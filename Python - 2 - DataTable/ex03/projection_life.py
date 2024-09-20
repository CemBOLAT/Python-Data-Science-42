from load_csv import load
import matplotlib.pyplot as plt


def main():
    try:
        year = '1900'
        gdp_per_capita = \
            load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        life_expectancy = load("life_expectancy_years.csv")
        if gdp_per_capita is None or life_expectancy is None:
            raise AssertionError("Dataset cannot be loaded")
        gdp_per_capita_columns = gdp_per_capita[year].values
        life_expectancy_columns = life_expectancy[year].values

        plt.scatter(gdp_per_capita_columns, life_expectancy_columns)
        plt.title(f"GDP per Capita vs Life Expectancy in {year}")
        plt.xlabel("Gross Domestic Product")
        plt.ylabel("Life Expectancy")
        plt.xscale("log")
        plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
        plt.tight_layout()
        plt.show()
    except AssertionError as e:
        print(f"Assertion Error: {e}")
        return
    except KeyboardInterrupt:
        print("Process interrupted by the user")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return


if __name__ == "__main__":
    main()
