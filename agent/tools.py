import json
import os
from dotenv import load_dotenv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv()

def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def get_openrouter_key():
    return os.getenv("OPENROUTER_API_KEY")

def fetch_sheet_data(sheet_url):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_url(sheet_url).sheet1
    return sheet.get_all_records()
