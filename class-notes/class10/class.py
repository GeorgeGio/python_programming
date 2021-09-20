class Tea:

    def __init__(self, temperature, tea_type,colour,with_milk):
        self.temperature = temperature
        self.tea_type = tea_type
        self.colour = colour
        self.with_milk = with_milk
        print("Tea is made")

    def stir(self):
        print(f'Stirring the {self.tea_type} tea')



yorkshire = Tea(100,'yorkshire','builders',True)
yorkshire.stir()
