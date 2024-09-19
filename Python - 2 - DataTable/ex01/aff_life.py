from load_csv import load
import matplotlib.pyplot as plt

def main():
    try:
        dataset = load("life_expectancy_years.csv")
        if dataset is None:
            raise AssertionError("Dataset cannot be loaded")
        turkey = dataset[dataset["country"] == "Turkey"]
        if turkey.empty:
            raise AssertionError("Turkey data not found")
        years = turkey.columns[1:]
        life_expectancy = turkey.values[0][1:]
        plt.plot(years, life_expectancy, label="Turkey")
        plt.title("Turkey Life Expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life Expectancy")
        plt.xticks(years[::40], rotation=45)
        plt.yticks(range(int(min(life_expectancy)), int(max(life_expectancy)), 10))
        plt.legend()
        plt.tight_layout()
        plt.show()
    
    except AssertionError as e:
        print(f"Assertion Error: {e}")
        return
    except KeyboardInterrupt:
        print("Process interrupted by the user")
        return


if __name__ == "__main__":
    main()
