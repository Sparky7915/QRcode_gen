import cv2
import pandas as pd
import os

# Initialize the webcam
cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

# Load existing scanned codes
excel_file = 'scanned_qrcode_camera.xlsx'
if os.path.exists(excel_file):
    try:
        df_existing = pd.read_excel(excel_file)
        scanned_codes = set(df_existing['Scanned QR Data'].astype(str))
    except Exception:
        scanned_codes = set()
else:
    scanned_codes = set()

print("Scan QR codes. Each new code will be saved only once. Press 'q' to quit.")

while True:
    ret, img = cap.read()
    if not ret:
        print("Failed to grab frame. Is your camera on?")
        break

    data, bbox, _ = detector.detectAndDecode(img)
    if data:
        clean = data.strip()
        if clean and (clean not in scanned_codes):
            print(f"Scanned: {clean}")
            scanned_codes.add(clean)

    cv2.imshow("QR Scanner - Press 'q' to save and exit", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Save results
if scanned_codes:
    df = pd.DataFrame({'Scanned QR Data': list(scanned_codes)})
    df.to_excel(excel_file, index=False)
    print(f"Saved all scanned codes to {excel_file}")
else:
    print("No QR codes detected/scanned.")
