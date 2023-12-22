# main.py
from entities.appointment_system import AppointmentSystem

def main():
    appointment_system = AppointmentSystem()

    # Register doctors and patients
    appointment_system.register_doctor("Dr. Smith", "Cardiologist")
    appointment_system.register_doctor("Dr. Johnson", "Dermatologist")
    appointment_system.register_patient("Alice")

    # Declare doctor's availability
    appointment_system.declare_availability("Dr. Smith", "09:00", "10:00")

    # # Book appointments
    # appointment_system.book_appointment("Alice", "Dr. Smith", "09:00")
    # appointment_system.book_appointment("Alice", "Dr. Smith", "09:30")

    # # View patient's appointments
    # appointment_system.view_appointments("Alice")

    # # Cancel an appointment
    # appointment_system.cancel_appointment("Alice", "09:00")

    # # Join waitlist
    # appointment_system.join_waitlist("Alice", "Dr. Smith", "09:00")

if __name__ == "__main__":
    main()
