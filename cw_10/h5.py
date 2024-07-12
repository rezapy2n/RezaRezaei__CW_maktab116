class VariableScopeDemo:
    class_variable = 'class!!'
    def __init__(self) -> None:
        self.instance_varaible = ''

    @classmethod
    def class_level(cls):
        cls.class_variable = 'changed by class level method'
        return cls.class_variable

    def instance_level(self):
        self.instance_varaible = 'changed by instance level method'
        return self.instance_varaible
    

o1 = VariableScopeDemo()

print(o1.class_level())
print(o1.instance_level())
