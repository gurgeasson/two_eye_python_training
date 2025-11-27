class MyCustomError(Exception):
    """Exception raised for custom error scenarios.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        
if __name__ == "__main__":
    raise Exception("Don't run this module, go to project root and run main.py instead")
