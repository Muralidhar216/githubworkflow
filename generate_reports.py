import os
import datetime
import base64
import requests
from openpyxl import Workbook

# === Config ===
REPO = os.getenv("GITHUB_REPOSITORY")  # GitHub repo (auto-set by Actions)
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Token from GitHub Actions
OWNER = "test-owner"  # Change as needed
BRANCH = "main"
API_URL = "https://api.github.com"

def create_excel(owner):
    os.makedirs("excelreports", exist_ok=True)
    date_str = datetime.datetime.now().strftime("%Y%m%d")
    filename = f"excelreports/{owner}_{date_str}.xlsx"

    wb = Workbook()
    ws = wb.active
    ws.title = "Report"
    ws.append(["Header 1", "Header 2"])
    ws.append(["Value 1", "Value 2"])
    wb.save(filename)

    print(f"✅ Excel report saved: {filename}")
    return filename

def create_html(owner):
    os.makedirs("htmlreports", exist_ok=True)
    content = f"<html><body><h1>Report for {owner}</h1></body></html>"
    filename = f"htmlreports/{owner}.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ HTML report generated: {filename}")
    return filename

def upload_html_as_blob(html_file):
    with open(html_file, "rb") as f:
        content = f.read()
    encoded = base64.b64encode(content).decode()

    url = f"{API_URL}/repos/{REPO}/contents/{html_file}"
    data = {
        "message": f"Add HTML report {html_file}",
        "content": encoded,
        "branch": BRANCH
    }

    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
    response = requests.put(url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"✅ Uploaded HTML to GitHub via REST API: {html_file}")
    else:
        print(f"❌ Failed to upload HTML: {response.status_code}")
        print(response.json())

def main():
    html = create_html(OWNER)
    create_excel(OWNER)
    upload_html_as_blob(html)

if __name__ == "__main__":
    main()
