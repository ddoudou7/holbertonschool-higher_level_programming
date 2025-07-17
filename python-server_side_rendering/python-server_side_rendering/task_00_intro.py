#!/usr/bin/python3
def generate_invitations(template, attendees):
    if not isinstance(template, str):
        raise TypeError("Invalid template type")
    if not isinstance(attendees, list):
        raise TypeError("Invalid attendees type")
    if template == "":
        return []
    if attendees == []:
        return []

    invitations = []
    for attendee in attendees:
        if not isinstance(attendee, dict):
            continue
        try:
            personalized = template.format(**attendee)
            invitations.append(personalized)
        except KeyError:
            continue
    return invitations
