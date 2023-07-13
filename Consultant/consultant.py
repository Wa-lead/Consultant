from types import FunctionType
import inspect
from Consultant.gptx import GPTx
from Consultant.prompt import Prompt



def consultant(strategy: str):
    """
    This function takes in a strategy, and returns a decorator that will transform a function or a class according to the strategy.
    """
    if strategy not in [Prompt.OPTIMIZER, Prompt.ENGINEER]:
        raise ValueError("Strategy should be either Prompt.OPTIMIZER or Prompt.ENGINEER")

    def function_decorator(func: FunctionType):
        gpt = GPTx()
        code = inspect.getsource(func)
        new_code = gpt.generate(strategy, code)
        print('The new code produced by Consultant is:\n\n{}'.format(new_code))

        # Dummy function to replace the original function. this is to prevent the original function from being executed.
        def dummy_func(*args, **kwargs):
            pass

        return dummy_func
    
    
    def class_decorator(cls):
        gpt = GPTx()

        # Get the source code of the class
        code = inspect.getsource(cls)

        # Generate new code based on the strategy
        new_code = gpt.generate(strategy, code)

        # Print the new code
        print(f'The new code for class {cls.__name__} is:\n\n{new_code}')

        # Return the original class (unmodified)
        return cls

    def decorator(func_or_cls):
        if inspect.isfunction(func_or_cls):
            return function_decorator(func_or_cls)
        elif inspect.isclass(func_or_cls):
            return class_decorator(func_or_cls)
        else:
            raise TypeError("Decorator can only be used on functions or classes.")

    return decorator
