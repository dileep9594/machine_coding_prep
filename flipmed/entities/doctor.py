class Doctor :
    def __init__(self , name,speciality,rating =0) :
        self.name = name
        self.speciality = speciality
        self.availability = {}

    def declare_availability(self, start_time, end_time):
        pass

    def book_appointment(self, patient, start_time):
        # Book an appointment
        pass

    def cancel_appointment(self, start_time):
        # Cancel an appointment
        pass