import pandas as pd
import random

college_list = [
    "BMS College of Engineering", "Dayananda Sagar University", "SJCE Mysuru", "NIE Mysore",
    "RV College of Engineering", "Global Academy of Technology", "BNMIT Bengaluru",
    "MS Ramaiah Institute of Technology", "Siddaganga Institute of Tech", "NMIT Bengaluru "
]

college_digit_map = {college: str((i % 4) + 1) for i, college in enumerate(college_list)}

names = ["Alex", "Brian", "Cathy", "David", "Emma", "Frank", "Grace", "Helena", "Ian", "Julia",
         "Kevin", "Lara", "Mike", "Nina", "Omar", "Priya", "Quinn", "Ravi", "Sara", "Tom",
         "Uma", "Vikram", "Wendy", "Xander", "Yara", "Zane"]
surnames = ["Smith", "Johnson", "Patel", "Kumar", "Garcia", "Lopez", "Mehta", "Das", "Sharma", "Iyer"]
team_names_base = ["Algo", "Byte", "Code", "Hack", "Script", "Pixel", "Stack", "Debug", "Logic",
                   "Syntax", "Bit", "Data", "Net", "Cyber", "Tech", "Cloud", "Mega", "Nano", "Quantum"]
team_suffixes = ["Ninjas", "Warriors", "Titans", "Squad", "Dynasty", "Invaders", "Blazers",
                 "Hunters", "Mavericks", "Raiders"]

num_teams = 45
members_per_team = 4  # leader + 3 members

def generate_phone_number():
    return str(random.choice([9, 8, 7])) + ''.join(str(random.randint(0,9)) for _ in range(9))

def generate_gmail(name, surname):
    return f"{name.lower()}.{surname.lower()}@example.com"

teams_data = []

for team_id in range(num_teams):
    team_num = f"{team_id + 1:02}"  # Format team number with leading zeros, e.g., 01, 02
    team_prefix = team_names_base[team_id % len(team_names_base)]
    team_suffix = team_suffixes[team_id % len(team_suffixes)]
    team_name = f"{team_prefix} {team_suffix}"
    college = college_list[team_id % len(college_list)]
    first_digit = college_digit_map[college]

    member_records = {"Team Number": team_num}

    for member_id in range(members_per_team):
        name = names[(team_id * members_per_team + member_id) % len(names)]
        surname = surnames[(team_id * members_per_team + member_id) % len(surnames)]
        full_name = f"{name} {surname}"
        year = 20 + (team_id % 5)
        branch_code = ["CS", "IT", "EC", "ME", "AI", "DS", "CE"][(team_id + member_id) % 7]
        serial_num = f"{(team_id * members_per_team + member_id) % 150 + 1:03}"
        usn = f"{first_digit}{college[0:2].upper()}{year}{branch_code}{serial_num}"
        phone = generate_phone_number()
        gmail = generate_gmail(name, surname)

        if member_id == 0:
            prefix = "Leader"
        else:
            prefix = f"Member {member_id + 1}"

        member_records[f"{prefix} Name"] = full_name
        member_records[f"{prefix} USN"] = usn
        member_records[f"{prefix} PH No"] = phone
        member_records[f"{prefix} Gmail"] = gmail

    member_records["Team Name"] = team_name
    member_records["College"] = college

    teams_data.append(member_records)

df_teams = pd.DataFrame(teams_data)
df_teams.to_excel("hackathon_teams_with_separate_teamnumber.xlsx", index=False)
print("Excel file generated: hackathon_teams_with_separate_teamnumber.xlsx")
