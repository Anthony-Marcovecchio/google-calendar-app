from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/calendar"]


def authenticate_user():
    flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
    credentials = flow.run_local_server(port=0)
    service = build("calendar", "v3", credentials=credentials)
    return service
