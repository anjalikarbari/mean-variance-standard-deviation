import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data
    df = pd.read_csv('adult.data.csv')

    # 1. How many of each race are represented?
    race_count = df['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. % of people with a Bachelor's degree
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 4. % with and without advanced education making >50K
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education

    higher_education_rich = round((df[higher_education]['salary'] == '>50K').mean() * 100, 1)
    lower_education_rich = round((df[lower_education]['salary'] == '>50K').mean() * 100, 1)

    # 5. Min work hours
    min_work_hours = df['hours-per-week'].min()

    # 6. % earning >50K among min workers
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers['salary'] == '>50K').mean() * 100, 1)

    # 7. Country with highest % earning >50K
    rich_by_country = df[df['salary'] == '>50K']['native-country'].value_counts()
    total_by_country = df['native-country'].value_counts()
    percent_rich_country = (rich_by_country / total_by_country * 100).fillna(0)
    highest_earning_country = percent_rich_country.idxmax()
    highest_earning_country_percentage = round(percent_rich_country.max(), 1)

    # 8. Most popular occupation for >50K earners in India
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

    # Print results
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print("Min work time:", min_work_hours, "hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    # Return dictionary
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
