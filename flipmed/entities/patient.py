# entities/patient.py
class Patient:
    def __init__(self, name):
        self.name = name
        self.appointments = []
        self.waitlist = []

    def book_appointment(self, doctor, start_time):
        self.appointments.append((doctor, start_time))
        print(f"Appointment booked with {doctor.name} at {start_time}")

    def cancel_appointment(self, start_time):
        for doctor, slot in self.appointments:
            if slot == start_time:
                self.appointments.remove((doctor, slot))
                doctor.cancel_appointment(slot)
                print(f"Appointment canceled at {start_time}")
                return
        print(f"No appointment found to cancel at {start_time}")

    def join_waitlist(self, doctor, start_time):
        self.waitlist.append((doctor, start_time))
        print(f"{self.name} joined the waitlist for {doctor.name} at {start_time}")

    def view_appointments(self):
        print(f"{self.name}'s Appointments:")
        for doctor, start_time in self.appointments:
            print(f"{doctor.name} at {start_time}")
