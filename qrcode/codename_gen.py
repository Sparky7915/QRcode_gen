import pandas as pd

# Load the Excel file
df = pd.read_excel('student_teams.xlsx', engine='openpyxl')

# Assuming columns are named 'College' and 'Team Name'
def generate_code(college,usn,team,):
    
    # Take first two letters of College (ignoring spaces, uppercased)
    college_str = str(college).replace(' ', '').upper()
    college_letters = college_str[:2]
    # Take 4th and 5th character of USN
    usn_str = str(usn)
    usn_4th_5th = usn_str[3:5] if len(usn_str) >= 5 else ''
    # Take first letter of each word in Team Name, up to 2 letters
    team_words = str(team).split()
    team_letters = ''.join([word[0].upper() for word in team_words[:2]])
    return f"{college_letters}{usn_4th_5th}{team_letters}"

# Add a new column with the unique code (assuming 'USN' column exists)
df['Unique Code'] = df.apply(lambda row: generate_code(row['College'], row['USN'], row['Team Name']), axis=1)

# Save the result to a new Excel file
df.to_excel('student_teams_with_codes.xlsx', index=False)

print("Unique codes generated and saved to 'student_teams_with_codes.xlsx'.")
