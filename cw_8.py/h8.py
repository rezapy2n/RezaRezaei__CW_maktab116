class MedicalRecord:
    def __init__(self, patient_name, patient_id):
        self.__patient_name = patient_name
        self.__patient_id = patient_id

    def get_patient_name(self):
        return self.__patient_name

    def set_patient_name(self, new_name):
        if new_name.isalpha():
            self.__patient_name = new_name
        else:
            print("Invalid name format. Please provide a valid name.")

    def get_masked_patient_id(self):
        return "*" * len(self.__patient_id)

    def set_patient_id(self, new_id):
        if new_id.isdigit() and len(new_id) == 8:
            self.__patient_id = new_id
        else:
            print("Invalid patient ID. Please provide an 8-digit numeric ID.")

    def display_patient_info(self):
        print(f"Patient Name: {self.__patient_name}")
        print(f"Masked Patient ID: {self.get_masked_patient_id()}")

# Example usage:
patient_record = MedicalRecord("reza rezaei", "323576768")
patient_record.display_patient_info()
