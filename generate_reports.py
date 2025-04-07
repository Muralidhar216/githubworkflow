import os
from openpyxl import Workbook
import datetime

# Sample HTML content
def save_html_report(owner):
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head><title>Report</title></head>
    <body>
        <h1>Report for {owner}</h1>
        <button onclick="alert('Filename: {owner}.html')">Show Filename</button>
    </body>
    </html>
    """
    folder = "htmlreports"
    os.makedirs(folder, exist_ok=True)
    filename = f"{owner}.html"
    filepath = os.path.join(folder, filename)

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(html_content)

    print(f"HTML report saved at {filepath}")

# Sample Excel content
def save_excel_report(owner):
    folder = "excelreports"
    os.makedirs(folder, exist_ok=True)

    headers = ["Name", "Value"]
    data = [
        ["Policy1", "Compliant"],
        ["Policy2", "Non-Compliant"]
    ]

    wb = Workbook()
    ws = wb.active
    ws.title = "Report"
    ws.append(headers)
    for row in data:
        ws.append(row)

    timestamp = datetime.datetime.now().strftime("%Y%m%d")
    filename = f"{owner}_{timestamp}.xlsx"
    filepath = os.path.join(folder, filename)

    wb.save(filepath)
    print(f"Excel report saved at {filepath}")

# Run both
if __name__ == "__main__":
    owner = "test-owner"
    save_html_report(owner)
    save_excel_report(owner)
