# -*- coding: utf8 -*-
__version__ = '1.0'                             # Verwaltungsinfos
__author__ = 'Ralf Adams (adams@tbs1.de)'


class AndGate:                                  # Beginn der Klassendefinition
    """
    This class calculates the logical AND function.
    """
    def __init__(self):                         # Hier werden die Attribute definiert
        self.Input0 = False
        self.Input1 = False
        self.Output = False
        self.Name = "YaAndGate"

    def execute(self):                          # Berechnung der Verknüpfung
        """
        Computes the result of the logical connection of the two inputs.
        :return: None
        """
        self.Output = False
        if True == self.Input0:
            if True == self.Input1:
                self.Output = True

    def __str__(self):                              # Ausformulieren der Stringumwandlung
        """
        Converts the status of the object to a string. The function will be called
        implicitly when you try to convert the object in a string.
        :return: Printable string of the status.
        """
        cwidth = 50
        first_last = ''.ljust(cwidth, '-')
        format_string = "-- {{0:10}}: {{1:{0}}} --".format(cwidth-18)

        return_string = first_last
        return_string = return_string + "\n" + format_string.format("Name", self.Name)
        return_string = return_string + "\n" + format_string.format("Type", type(self).__name__)
        return_string = return_string + "\n" + format_string.format("Input0", str(self.Input0))                     # so
        return_string = return_string + "\n" + format_string.format("Input1", "True" if (self.Input1) else "False") # oder so
        return_string = return_string + "\n" + format_string.format("Output", "True" if (self.Output) else "False")
        return_string = return_string + "\n" + first_last
        return return_string

    def show(self):
        """
        Shows the value of each property of the class and the class name.
        :return: None
        """
        print(self.__str__())

if __name__ == "__main__":          # Nur zum Rumspielen
    a = AndGate()

    a.show()

    a.Input0 = True
    a.Input1 = True
    a.execute()
    a.show()
