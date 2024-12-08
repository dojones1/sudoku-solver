class Cell:
    poss_values = []
    value = None

    def __init__(self):
        self.poss_values = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.value = None
        self.calculated = False

    def __repr__(self):
        return "{} {} {}".format(self.value, self.poss_values, self.calculated)

    def is_solved(self):
        return not (self.value is None)

    def get_poss_values(self):
        return self.poss_values

    def get_value(self):
        if self.value is None:
            return '-'
        return self.value

    def get_calculated(self):
        return self.calculated

    def set(self, value, calculated):
        # Check that value is in the list of possible values
        try:
            assert (value in self.poss_values)
        except AssertionError:
            pass

        self.poss_values = [value]
        self.value = value
        self.calculated = calculated

    def remove_poss_value(self, value):
        # Make sure that don't override existing value
        resolved = False
        if self.value:
            resolved = False
        else:
            if value in self.poss_values:
                self.poss_values.remove(value)
            # Have we now only got one value left?
            if len(self.poss_values) == 1:
                print("     Have resolved a value: {}".format(self.poss_values[0]))
                self.set(self.poss_values[0], True)
                resolved = True

        return resolved
