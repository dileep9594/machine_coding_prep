# entities/patient.py
class Patient:
    def __init__(self, name):
        self.name = name
        self.appointments = []
        self.waitlist = []

    def book_appointment(self, doctor, start_time):
        # Book an appointment
        pass

    def cancel_appointment(self, appointment):
        # Cancel an appointment
        pass

    def join_waitlist(self, doctor, start_time):
        # Join the waitlist
        pass

    def view_appointments(self):
        # View booked appointments
        pass
