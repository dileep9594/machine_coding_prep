# entities/appointment_system.py
from flipmed.entities.doctor import Doctor
from flipmed.entities.patient import Patient


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
