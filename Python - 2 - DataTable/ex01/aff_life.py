from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Load the life expectancy dataset and plot the life expectancy

    Returns:
        None

    Raises:
        AssertionError: If the dataset cannot be loaded or Tr data not found
        KeyboardInterrupt: If the process is interrupted

    Logic:
        - Load the dataset
        - Check if the dataset is loaded
        - Filter the data for Turkey
        - Check if Turkey data is found
        - Get the years and life expectancy data
        - Plot the life expectancy data
    """
    try:
        dataset = load("life_expectancy_years.csv")
        if dataset is None:
            raise AssertionError("Dataset cannot be loaded")
        turkey = dataset[dataset["country"] == "Turkey"]
        if turkey.empty:
            raise AssertionError("Turkey data not found")
        years = turkey.columns[1:]
        life_expct = turkey.values[0][1:]
        plt.plot(years, life_expct, label="Turkey")
        plt.title("Turkey Life Expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life Expectancy")
        plt.xticks(years[::40], rotation=45)
        plt.yticks(range(int(min(life_expct)), int(max(life_expct)), 10))
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
