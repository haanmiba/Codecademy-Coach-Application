import pandas as pd
from scipy.stats import chi2_contingency, binom_test

## Read from CSV file
df = pd.read_csv('clicks.csv')

## Create a new column that records whether or not a purchase is made
df['is_purchase'] = pd.Series(['No Purchase' if pd.isnull(datum) else 'Purchase' for datum in df['click_day']])

## Keep count of purchases/no purchases by groups A, B, and C
purchase_counts = df.groupby(['group', 'is_purchase']).count()['user_id']

## Create a list of pairs of (# of purchases, # of no purchases) for each group
contingency = [[purchase_counts[group, 'Purchase'], purchase_counts[group, 'No Purchase']] for group in ('A', 'B', 'C')]
print(chi2_contingency(contingency))

## Record the total number of visitors to the site this week
num_visitors = len(df)
print('{} visitors came to the site this week.'.format(num_visitors))

# Calculate the number of people who would need to purchase a $0.99 upgrade in order to generate $1000.
# Then divide by the number of people who visit the site each week.
people_needed_A = (1000 / .99)
percentage_A = people_needed_A / num_visitors
print('Group A: {:.2f}% of visitors.'.format(percentage_A * 100))

# Calculate the number of people who would need to purchase a $1.99 upgrade in order to generate $1000.
# Then divide by the number of people who visit the site each week.
people_needed_B = (1000 / 1.99)
percentage_B = people_needed_B / num_visitors
print('Group B: {:.2f}% of visitors.'.format(percentage_B * 100))

# Calculate the number of people who would need to purchase a $4.99 upgrade in order to generate $1000.
# Then divide by the number of people who visit the site each week.
people_needed_C = (1000 / 4.99)
percentage_C = people_needed_C / num_visitors
print('Group C: {:.2f}% of visitors.'.format(percentage_C * 100))

# Test group A
print(binom_test(x=purchase_counts['A', 'Purchase'], n=purchase_counts['A'].sum(), p=percentage_A))

# Test group B
print(binom_test(x=purchase_counts['B', 'Purchase'], n=purchase_counts['B'].sum(), p=percentage_B))

# Test group C
print(binom_test(x=purchase_counts['C', 'Purchase'], n=purchase_counts['C'].sum(), p=percentage_C))