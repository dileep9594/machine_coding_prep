# entities/doctor.py
class Doctor:
    def __init__(self, name, speciality, rating=0):
        self.name = name
        self.speciality = speciality
        self.rating = rating
        self.availability = {}

    def declare_availability(self, start_time, end_time):
        slot = (start_time, end_time)
        if slot not in self.availability:
            self.availability[slot] = True
            print(f"Availability declared by {self.name} from {start_time} to {end_time}")
        else:
            print(f"Slot {start_time} to {end_time} is already booked or declared.")

    def book_appointment(self, patient, start_time):
        slot = (start_time, start_time + 30)
        if slot in self.availability and self.availability[slot]:
            patient.book_appointment(self, start_time)
            self.availability[slot] = False
            print(f"Appointment booked by {patient.name} with {self.name} at {start_time}")
        else:
            print(f"Slot {start_time} is not available.")

    def cancel_appointment(self, start_time):
        slot = (start_time, start_time + 30)
        if slot in self.availability and not self.availability[slot]:
            self.availability[slot] = True
            print(f"Appointment canceled by {self.name} at {start_time}")
        else:
            print(f"No appointment found to cancel at {start_time}")
