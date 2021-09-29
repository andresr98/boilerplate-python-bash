import argparse

class Parameters:
    """

    This component will capture the input information included in args at the execution start
    and return it to a dict like format to be used.
    For example: 'python ./main.py --example1 value_to_input'. 
    It will capture the String 'value_to_input' and store it in the 'example1' parameter. 

    ...

    Attributes
    ----------
    parser : ArgumentParser
        Save all definitions of input parameters that will be read at execution.
    initialized: Bool
        Check if parameters were initialized.

    Methods
    -------
    parse()
        Return all parameters in an object argparse.Namespace.

    """
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.initialized = False

    def initialize(self):
        """
        Initialize parameters that will be read at the begining of the execution.
        
        """
        self.parser.add_argument('--name', type=str, default='Sin nombre', help='Explicar el uso del argumento')

        # Set boolean argument
        #self.parser.add_argument('--boolean_arg', action='store_true', help='Explicacion del argumento booleano')

        # Set integer argument
        #self.parser.add_argument('--integer_arg', type=int, default=100, help='Explicacion del argumento numerico')
        self.initialized = True
    
    def parse(self):
        """
        Initialize parameters and convert them to a dictionary-like format.
        Where every parameter is called as a Attribute.
        For example: 'opt.example1' will call the information stored in the parameter 'example1'.

        Returns
        -------
        opt : `argparse.Namespace`
        
        """
        if not self.initialized:
            self.initialize()
        self.opt = self.parser.parse_args()
        
        return self.opt