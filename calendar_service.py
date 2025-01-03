def list_events(service):
    events_result = (
        service.events()
        .list(
            calendarId="primary", maxResults=10, singleEvents=True, orderBy="startTime"
        )
        .execute()
    )
    events = events_result.get("items", [])
    return events


def create_event(service, event_data):
    event = {
        "summary": event_data["summary"],
        "start": {"dateTime": event_data["start"], "timeZone": "UTC"},
        "end": {"dateTime": event_data["end"], "timeZone": "UTC"},
    }
    service.events().insert(calendarId="primary", body=event).execute()
