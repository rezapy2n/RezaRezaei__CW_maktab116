class MedicalRecord:

    def __init__(self,doctor_name):
        self.name = ''
        self.last_name = ''
        self.__age = ''
        self.__sickness = ''
        self.doctor_name = doctor_name

    @property
    def sickness(self):
        return 'sickness is set'

    @sickness.setter
    def sickness(self,value):
        if value != '':
            self.__sickness = value
        else:
            print('error')

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self,value):
        if value != '':
            self.name = value
        else:
            print('error')

    @property
    def last_name(self):
        return self.last_name

    @last_name.setter
    def last_name(self,value):
        if value != '':
            self.last_name = value
        else:
            print('error')

    @property
    def age(self):
        return ''

    @age.setter
    def age(self,value):
        if value > 0:
            self.__sickness = value
        else:
            print('error')

    def display_patient_information(self):
        return f'patient name : {self.name}\npatient lastname : {self.last_name}\npatient age: {self.__age}\nsickness: {self.__sickness}\npatient doctor: {self.doctor_name}'
    

patient_1 = MedicalRecord('reza')

patient_1.name = 'mobin'
patient_1.age = 23
patient_1.sickness = 'cold'
patient_1.last_name = 'davaji'
print(patient_1.display_patient_information())