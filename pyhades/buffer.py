class Buffer(list):
    r"""
    Documentation here
    """

    def __init__(self, length:int=10, roll:str='forward'):
        r"""
        Documentation here
        """
        self._roll_type_allowed = ['forward', 'backward']
        self.max_length = length
        self.roll = roll
        super(Buffer, self).__init__([0] * self.max_length)

    @property
    def max_length(self):
        r"""
        Documentation here
        """
        return self._max_length

    @max_length.setter
    def max_length(self, value:int):
        r"""
        Documentation here
        """
        if not isinstance(value, int):

            raise TypeError("Only integers are allowed")

        if value <= 1:

            raise ValueError(f"{value} must be greater than one (1)")

        self._max_length = value

    @property
    def roll(self):
        r"""
        Documentation here
        """
        return self.roll_type

    @roll.setter
    def roll(self, value:str):
        r"""
        Documentation here
        """
        if not isinstance(value, str):

            raise TypeError("Only strings are allowed")

        if value not in self._roll_type_allowed:
            
            raise ValueError(f"{value} is not allowed, you can only use: {self._roll_type_allowed}")

        self.roll_type = value

    def __call__(self, value):
        r"""
        Documentation here
        """
        if self.roll.lower()=='forward':
            
            self.pop()
            super(Buffer, self).insert(0, value)

        else:

            self.pop(0)
            super(Buffer, self).append(value)

        return self