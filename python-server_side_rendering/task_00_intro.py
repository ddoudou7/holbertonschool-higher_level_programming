def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(d, dict) for d in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    for idx, person in enumerate(attendees, start=1):
        content = template
        for field in ["name", "event_title", "event_date", "event_location"]:
            value = person.get(field)
            content = content.replace("{" + field + "}", str(value) if value else "N/A")
        with open(f"output_{idx}.txt", "w") as file:
            file.write(content)
