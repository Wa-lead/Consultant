from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin


@dataclass
class Prompt(DataClassJsonMixin):
    name: str
    description: str
    instruction: str

class Optimizer(Prompt):
    def __init__(self):
        super().__init__(
            name='Optimizer',
            description='You have been given a specific function that performs a certain computation. Your task is to optimize and vectorize the function to improve its efficiency and performance.',
            instruction=f'''Given a code,please provide a more optimized version of this function using vectorized operations and Python best practices. Ensure the function maintains the same functionality and returns the same output.
            '''
        )
        
class Engineer(Prompt):
    def __init__(self):
        super().__init__(
            name='Engineer',
            description='You have been assigned a codebase that requires refactoring to improve its design and adhere to decoupling principles. Your task is to analyze the existing code and propose a refactored version that promotes loose coupling between its components.',
            instruction=f'''Given a code,
                            please provide a Python solution that prioritizes:
                            1. High readability and clean code.
                            2. Adherence to the functional programming paradigm.
                            3. Avoidance of side effects and global state.
                            4. Using meaningful variable and function names.
                            5. Proper documentation in the form of comments where necessary.

                            Ensure that the function or functions provided are pure and make efficient use of Python's functional capabilities.
                        '''
        )

