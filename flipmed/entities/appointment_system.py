
from entities.doctor import Doctor
from entities.patient import Patient


class AppointmentSystem:
    def __init__(self):
        self.doctors = {}
        self.patients = {}

    def register_doctor(self, name, speciality):
        doctor = Doctor(name, speciality)
        self.doctors[name] = doctor

    def register_patient(self, name):
        patient = Patient(name)
        self.patients[name] = patient

    def declare_availability(self, doctor_name, start_time, end_time):
        doctor = self.doctors.get(doctor_name)
        if doctor:
            doctor.declare_availability(start_time, end_time)

    def book_appointment(self, patient_name, doctor_name, start_time):
        patient = self.patients.get(patient_name)
        doctor = self.doctors.get(doctor_name)
        if patient and doctor:
            doctor.book_appointment(patient, start_time)
        else:
            print("Patient or doctor not found.")

    def cancel_appointment(self, patient_name, start_time):
        patient = self.patients.get(patient_name)
        if patient:
            patient.cancel_appointment(start_time)
        else:
            print("Patient not found.")

    def join_waitlist(self, patient_name, doctor_name, start_time):
        patient = self.patients.get(patient_name)
        doctor = self.doctors.get(doctor_name)
        if patient and doctor:
            patient.join_waitlist(doctor, start_time)
        else:
            print("Patient or doctor not found.")

    def view_appointments(self, patient_name):
        patient = self.patients.get(patient_name)
        if patient:
            patient.view_appointments()
        else:
            print("Patient not found.")
