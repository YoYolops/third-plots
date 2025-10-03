import gspread
import pandas as pd
import os

CURRENT_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
SERVICE_ACCOUNT_KEY_PATH = os.path.join(CURRENT_DIR_PATH, 'graficos-terceiros-03ea719a3e5c.json') 
SPREADSHEET_TITLE = 'Periodização Heavyv Duty'
SPREADSHEET_ID = '1O0aS4u4Jme_NcmCauCMta0dJSHTfE3RLpB73NyDg4r4'
WORKSHEET_NAME = 'Montagem do Treinamento'

RED = '\033[31m'
RED_RESET = '\033[0m'
GREEN = '\033[32m'
GREEN_RESET = '\033[0m'
# ---------------------

def read_google_sheet_data_service_account():
    if not os.path.exists(SERVICE_ACCOUNT_KEY_PATH):
        print(f"{RED}~~~ ERROR: Credential file not found at '{SERVICE_ACCOUNT_KEY_PATH}'. Please check the path.{RED_RESET}")
        return

    try:
        # gspread.service_account() automatically handles the creation of credentials from the file path.
        gc = gspread.service_account(filename=SERVICE_ACCOUNT_KEY_PATH)
        print(f"{GREEN}YOHAN LINDO DIZ:{GREEN_RESET} Successfully authenticated with Google Sheets API.")

        # key can be found in the url, other methods of identifying the spreadsheet are available
        spreadsheet = gc.open_by_key(SPREADSHEET_ID)
        
        # select the specific worksheet/tab
        worksheet = spreadsheet.worksheet(WORKSHEET_NAME)

        # Returns data as list of lists
        data = worksheet.get_all_values()
        print(data)
        df = pd.DataFrame(data)
        
        print(f"\n--- Data Read from Sheet '{WORKSHEET_NAME}' ---")
        print(df.head(20).to_string(index=False))

    except gspread.exceptions.SpreadsheetNotFound:
        print(f"~~~ ERROR: Spreadsheet '{SPREADSHEET_ID}' not found. Did you share it with the Service Account email?")
    except gspread.exceptions.WorksheetNotFound:
        print(f"~~~ ERROR: Worksheet '{WORKSHEET_NAME}' not found in the spreadsheet.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    read_google_sheet_data_service_account()