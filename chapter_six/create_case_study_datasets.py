import pandas as pd
import numpy as np

# Setting the seed for reproducibility
np.random.seed(42)

"""1. Financial Case Study"""
# Function to create the financial analytics dataset
def create_financial_dataset():
    # Date range (36 months)
    dates = pd.date_range(start='2020-01-01', periods=36, freq='M')
    
    # Revenue, Expenses, and Investments data generation
    revenue = np.random.uniform(100000, 500000, len(dates))
    expenses_categories = ['salaries', 'R&D', 'marketing']
    expenses = pd.DataFrame(np.random.uniform(20000, 150000, size=(len(dates), len(expenses_categories))), 
                            columns=expenses_categories)
    total_expenses = expenses.sum(axis=1)
    profit = revenue - total_expenses
    investments = pd.DataFrame(np.random.uniform(5000, 50000, size=(len(dates), 3)), 
                               columns=['type1', 'type2', 'type3'])
    
    # Market Segment
    market_segments = ['Consumer', 'Enterprise', 'SMB']
    segment_distribution = np.random.choice(market_segments, len(dates))

    # Creating the DataFrame
    financial_df = pd.DataFrame({
        'Date': dates,
        'Revenue': revenue,
        'Total Expenses': total_expenses,
        'Profit': profit,
        'Investment Type 1': investments['type1'],
        'Investment Type 2': investments['type2'],
        'Investment Type 3': investments['type3'],
        'Market Segment': segment_distribution
    })
    
    return financial_df

# Generate the financial analytics dataset
financial_dataset = create_financial_dataset()
financial_dataset.head()

"""2. Healthcare Case Study"""
# Function to create the healthcare analytics dataset
def create_healthcare_dataset():
    # Generating patient IDs
    patient_ids = np.arange(1000, 1125)
    
    # Random age distribution from 0 to 100
    ages = np.random.randint(0, 100, len(patient_ids))
    
    # Gender distribution
    genders = np.random.choice(['Male', 'Female', 'Other'], len(patient_ids))
    
    # Condition/Diagnosis categories
    conditions = ['Condition A', 'Condition B', 'Condition C', 'Condition D']
    patient_conditions = np.random.choice(conditions, len(patient_ids))
    
    # Treatment types
    treatments = ['Treatment 1', 'Treatment 2', 'Treatment 3']
    treatment_types = np.random.choice(treatments, len(patient_ids))
    
    # Treatment outcomes
    outcomes = ['Success', 'Partial Success', 'No Change', 'Deterioration']
    treatment_outcomes = np.random.choice(outcomes, len(patient_ids))
    
    # Length of stay (in days)
    length_of_stay = np.random.randint(1, 30, len(patient_ids))
    
    # Hospital departments
    departments = ['Cardiology', 'Neurology', 'Oncology', 'Pediatrics']
    hospital_departments = np.random.choice(departments, len(patient_ids))

    # Creating the DataFrame
    healthcare_df = pd.DataFrame({
        'Patient ID': patient_ids,
        'Age': ages,
        'Gender': genders,
        'Condition': patient_conditions,
        'Treatment Type': treatment_types,
        'Treatment Outcome': treatment_outcomes,
        'Length of Stay': length_of_stay,
        'Department': hospital_departments
    })
    
    return healthcare_df

# Generate the healthcare analytics dataset
healthcare_dataset = create_healthcare_dataset()
healthcare_dataset.head()

"""3. Social Media Case Study"""
import datetime

# Function to create the social media analytics dataset
def create_social_media_dataset():
    # Generating post IDs
    post_ids = np.arange(10000, 10150)
    
    # Post dates (over the last year)
    start_date = datetime.date.today() - datetime.timedelta(days=365)
    dates = pd.date_range(start=start_date, periods=len(post_ids))
    
    # Content types
    content_types = ['Image', 'Video', 'Text', 'Link']
    post_content_types = np.random.choice(content_types, len(post_ids))
    
    # Interactions (Likes, Shares, Comments)
    likes = np.random.randint(0, 1000, len(post_ids))
    shares = np.random.randint(0, 500, len(post_ids))
    comments = np.random.randint(0, 300, len(post_ids))
    
    # Audience demographics (Age Group, Location)
    age_groups = ['18-24', '25-34', '35-44', '45-54', '55+']
    audience_age_groups = np.random.choice(age_groups, len(post_ids))
    
    locations = ['North America', 'Europe', 'Asia', 'South America', 'Africa', 'Australia']
    audience_locations = np.random.choice(locations, len(post_ids))

    # Creating the DataFrame
    social_media_df = pd.DataFrame({
        'Post ID': post_ids,
        'Date Posted': dates,
        'Content Type': post_content_types,
        'Likes': likes,
        'Shares': shares,
        'Comments': comments,
        'Audience Age Group': audience_age_groups,
        'Audience Location': audience_locations
    })
    
    return social_media_df

# Generate the social media analytics dataset
social_media_dataset = create_social_media_dataset()
social_media_dataset.head()


"""4. Digital Marketing Case Study"""
# Function to create the digital marketing/advertising analytics dataset
def create_digital_marketing_dataset():
    # Generating campaign IDs
    campaign_ids = np.arange(200, 250)
    
    # Campaign dates (over the last 6 months)
    start_date = datetime.date.today() - datetime.timedelta(days=180)
    dates = pd.date_range(start=start_date, periods=len(campaign_ids))
    
    # Advertising platforms
    platforms = ['Google', 'Facebook', 'LinkedIn', 'Twitter', 'Instagram']
    campaign_platforms = np.random.choice(platforms, len(campaign_ids))
    
    # Ad spend, Impressions, Clicks, Conversions
    ad_spend = np.random.uniform(500, 10000, len(campaign_ids))
    impressions = np.random.randint(1000, 100000, len(campaign_ids))
    clicks = np.random.randint(100, 10000, len(campaign_ids))
    conversions = np.random.randint(0, 1000, len(campaign_ids))
    
    # Conversion value (simulating revenue generated from conversions)
    conversion_value = conversions * np.random.uniform(10, 100)

    # Creating the DataFrame
    digital_marketing_df = pd.DataFrame({
        'Campaign ID': campaign_ids,
        'Date': dates,
        'Platform': campaign_platforms,
        'Ad Spend': ad_spend,
        'Impressions': impressions,
        'Clicks': clicks,
        'Conversions': conversions,
        'Conversion Value': conversion_value
    })
    
    return digital_marketing_df

# Generate the digital marketing/advertising analytics dataset
digital_marketing_dataset = create_digital_marketing_dataset()
digital_marketing_dataset.head()


"""5. Ecommerce Case Study"""
# Function to create the e-commerce analytics dataset
def create_ecommerce_dataset():
    # Generating order IDs
    order_ids = np.arange(5000, 5150)
    
    # Order dates (over the last year)
    start_date = datetime.date.today() - datetime.timedelta(days=365)
    dates = pd.date_range(start=start_date, periods=len(order_ids))
    
    # Product categories
    categories = ['Electronics', 'Clothing', 'Home & Garden', 'Books', 'Health & Beauty']
    product_categories = np.random.choice(categories, len(order_ids))
    
    # Quantity sold and unit price
    quantity_sold = np.random.randint(1, 10, len(order_ids))
    unit_price = np.random.uniform(10, 1000, len(order_ids))
    
    # Customer locations
    customer_locations = np.random.choice(['North America', 'Europe', 'Asia', 'South America', 'Africa', 'Australia'], len(order_ids))
    
    # Payment methods
    payment_methods = ['Credit Card', 'PayPal', 'Debit Card', 'Bank Transfer', 'Gift Card']
    payment_types = np.random.choice(payment_methods, len(order_ids))
    
    # Return status (Yes/No)
    return_status = np.random.choice(['Yes', 'No'], len(order_ids))

    # Creating the DataFrame
    ecommerce_df = pd.DataFrame({
        'Order ID': order_ids,
        'Date of Purchase': dates,
        'Product Category': product_categories,
        'Quantity Sold': quantity_sold,
        'Unit Price': unit_price,
        'Customer Location': customer_locations,
        'Payment Method': payment_types,
        'Return Status': return_status
    })
    
    return ecommerce_df

# Generate the e-commerce analytics dataset
ecommerce_dataset = create_ecommerce_dataset()
ecommerce_dataset.head()


"""6. Sports Case Study"""
# Function to create the sports analytics dataset
def create_sports_dataset():
    # Generating game dates (for one season, 50 games)
    start_date = datetime.date.today() - datetime.timedelta(days=180)
    game_dates = pd.date_range(start=start_date, periods=50, freq='W')
    
    # Teams (10 teams, playing against each other)
    teams = [f'Team {i}' for i in range(1, 11)]
    home_teams = np.random.choice(teams, len(game_dates))
    away_teams = np.random.choice(teams, len(game_dates))
    
    # Ensuring home and away teams are not the same
    for i in range(len(home_teams)):
        while home_teams[i] == away_teams[i]:
            away_teams[i] = np.random.choice(teams)
    
    # Scores (randomly generated)
    home_scores = np.random.randint(0, 5, len(game_dates))  # Assuming a sport where scores are relatively low (e.g., soccer)
    away_scores = np.random.randint(0, 5, len(game_dates))
    
    # Player stats (random selection of 5 players from each team per game, with random stats)
    player_ids = np.random.randint(100, 200, 5 * len(game_dates))  # Random player IDs
    player_positions = np.random.choice(['Forward', 'Midfielder', 'Defender', 'Goalkeeper'], len(player_ids))
    player_stats = np.random.randint(0, 3, len(player_ids))  # Assuming stats like goals, assists, etc.
    
    # Attendance (randomly generated)
    attendance = np.random.randint(5000, 50000, len(game_dates))
    
    # Venues (assuming each team has its own stadium)
    venues = [f'{team} Stadium' for team in home_teams]

    # Creating the DataFrame for games
    games_df = pd.DataFrame({
        'Game Date': np.repeat(game_dates, 5),  # Each game repeated for 5 players
        'Home Team': np.repeat(home_teams, 5),
        'Away Team': np.repeat(away_teams, 5),
        'Home Score': np.repeat(home_scores, 5),
        'Away Score': np.repeat(away_scores, 5),
        'Player ID': player_ids,
        'Player Position': player_positions,
        'Player Stats': player_stats,
        'Attendance': np.repeat(attendance, 5),
        'Venue': np.repeat(venues, 5)
    })
    
    return games_df

# Generate the sports analytics dataset
sports_dataset = create_sports_dataset()
sports_dataset.head(10)  # Displaying the first 10 rows to show data for two games


# Save each to separate Excel file for Tableau (optional)
# Define the base file path for saving the Excel files
base_file_path = "file_path_here" # double backslashes needed at end to go through directory

# Filenames for each dataset
filenames = [
    "Case_Study_I_Financial_Analytics.xlsx",
    "Case_Study_II_Healthcare_Analytics.xlsx",
    "Case_Study_III_Social_Media_Analytics.xlsx",
    "Case_Study_IV_Digital_Marketing_Analytics.xlsx",
    "Case_Study_V_Ecommerce_Analytics.xlsx",
    "Case_Study_VI_Sports_Analytics.xlsx"
]

# Datasets to be saved
datasets = [
    financial_dataset,
    healthcare_dataset,
    social_media_dataset,
    digital_marketing_dataset,
    ecommerce_dataset,
    sports_dataset
]

# Saving each dataset to an Excel file
file_paths = []
for filename, dataset in zip(filenames, datasets):
    file_path = base_file_path + filename
    dataset.to_excel(file_path, index=False)
    file_paths.append(file_path)

# Print file paths to confirm data location
file_paths



