import pandas as pd 

titanic_data = pd.read_csv(r'D:/Titanic Dataset/tested.csv')

print(titanic_data.head())

# Get basic information about the dataset
print(titanic_data.info())


# Get statistical summary
print(titanic_data.describe())

# Check for missing values
print(titanic_data.isnull().sum())

# Sort by age (youngest to oldest)
titanic_sorted_by_age = titanic_data.sort_values(by='Age')


# Sort by multiple columns (class then age)
titanic_sorted_multiple = titanic_data.sort_values(by=['Pclass', 'Age'])

# Get only survivors
survivors = titanic_data[titanic_data['Survived'] == 1]

# Get only first class passengers
first_class = titanic_data[titanic_data['Pclass'] == 1]

# Get female survivors
female_survivors = titanic_data[(titanic_data['Survived'] == 1) & 
                               (titanic_data['Sex'] == 'female')]

# Select just the columns you're interested in
selected_columns = titanic_data[['Survived', 'Pclass','Sex', 'Age']]

# Fill missing age values with the mean age
titanic_data['Age'] = titanic_data['Age'].fillna(titanic_data['Age'].mean())

# Create a column for family size
titanic_data['FamilySize'] = titanic_data['SibSp'] + titanic_data['Parch'] + 1

# Create age groups
titanic_data['AgeGroup'] = pd.cut(titanic_data['Age'], 
                                 bins=[0, 12, 18, 65, 100], 
                                 labels=['Child', 'Teenager', 'Adult', 'Elderly'])


# Save to a new CSV file
titanic_data.to_csv('cleaned_titanic.csv', index=False)
