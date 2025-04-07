import os
import datetime
from openpyxl import Workbook

def create_folders():
    os.makedirs("htmlreports", exist_ok=True)
    os.makedirs("excelreports", exist_ok=True)

def save_html(owner):
    html_path = f"htmlreports/{owner}.html"
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(f"<html><body><h1>Report for {owner}</h1></body></html>")
    print(f"✅ HTML report saved to {html_path}")

def save_excel(owner):
    today = datetime.datetime.now().strftime("%Y%m%d")
    excel_path = f"excelreports/{owner}_{today}.xlsx"

    wb = Workbook()
    ws = wb.active
    ws.title = "Sample"
    ws.append(["Subscription NAME", "APM ID", "Compliance State"])
    ws.append(["Test Sub", "123456", "NonCompliant"])

    wb.save(excel_path)
    print(f"✅ Excel report saved to {excel_path}")

if __name__ == "__main__":
    owner = "test-owner"
    create_folders()
    save_html(owner)
    save_excel(owner)