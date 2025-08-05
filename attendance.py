import pandas as pd

def mark_attendance(scanned_file, teams_file, output_file):
    # Read scanned QR codes
    scanned_df = pd.read_excel(scanned_file)
    # Read hackathon teams
    teams_df = pd.read_excel(teams_file)

    # Columns to check for attendance
    code_columns = [
        'Leader Unique Code',
        'Member 2 Unique Code',
        'Member 3 Unique Code',
        'Member 4 Unique Code'
    ]
    scanned_codes = set(scanned_df['Scanned QR Data'].astype(str))

    # Mark attendance for each member
    for col in code_columns:
        if col in teams_df.columns:
            teams_df[col + ' Attendance'] = teams_df[col].astype(str).apply(
                lambda code: 'Present' if code in scanned_codes else 'Absent'
            )

    # Save to new Excel file
    teams_df.to_excel(output_file, index=False)

if __name__ == "__main__":
    scanned_file = "scanned_qrcode_camera.xlsx"
    teams_file = "hackathon_teams.xlsx"
    output_file = "attendance_output.xlsx"
    mark_attendance(scanned_file, teams_file, output_file)
