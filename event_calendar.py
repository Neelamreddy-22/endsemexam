# event_calendar.py - Event Calendar Module

class EventCalendar:
    def __init__(self):
        self.events = []
    
    def add_event(self, event_id, event_name, date, time, location):
        """Add a new event to the calendar"""
        self.events.append({
            "event_id": event_id,
            "event_name": event_name,
            "date": date,
            "time": time,
            "location": location,
            "attendees": []
        })
        return {"success": True, "message": f"Event '{event_name}' created"}
    
    def register_attendee(self, event_id, attendee_id, attendee_name):
        """Register an attendee for an event"""
        event = next((e for e in self.events if e["event_id"] == event_id), None)
        if not event:
            return {"success": False, "message": "Event not found"}
        
        event["attendees"].append({
            "attendee_id": attendee_id,
            "attendee_name": attendee_name
        })
        return {"success": True, "message": f"{attendee_name} registered for event"}
    
    def get_events_by_date(self, date):
        """Get all events on a specific date"""
        return [e for e in self.events if e["date"] == date]
    
    def get_all_events(self):
        """Get all events sorted by date"""
        return sorted(self.events, key=lambda x: x["date"])
    
    def get_system_status(self):
        """Get the system status - WILL CAUSE MERGE CONFLICT"""
        return "Event Calendar System - v2.0 - Active"

if __name__ == "__main__":
    calendar = EventCalendar()
    print(calendar.get_system_status())
