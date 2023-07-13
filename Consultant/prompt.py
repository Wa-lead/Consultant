from dataclasses import dataclass


STRICT_OUTPUT: str = 'CRITICAL NOTE: Your output should only contain the  refactored code ONLY. No other explaination or text should be included.'

@dataclass
class Prompt:
    OPTIMIZER: str = f"""You have been given a specific function that performs a certain computation. Your task is to optimize and vectorize the function to improve its efficiency and performance.

                        Your goals are:
                        
                        1. Optimize the function to make it more efficient by reducing redundant calculations, eliminating unnecessary loops, or applying any other suitable optimization techniques.

                        2. Vectorize the function to leverage the inherent parallelism in modern hardware architectures. You can utilize NumPy or any other suitable libraries to achieve vectorization.

                        3. Preserve the correctness and functionality of the original function. The optimized and vectorized version should produce the same output as the original function for any given input.

                        4. Please provide the optimized and vectorized implementation of the function in your response.
                        
                        {STRICT_OUTPUT}
                        """
                        
                        
    ENGINEER: str = f"""You have been assigned a codebase that requires refactoring to improve its design and adhere to decoupling principles. Your task is to analyze the existing code and propose a refactored version that promotes loose coupling between its components.

                    Your goals are:

                    1. Identify areas of tight coupling in the existing code, where components are heavily dependent on each other.

                    2. Propose a refactored version that promotes loose coupling between components, allowing for easier maintenance, reusability, and testability.

                    3. Maintain the functionality of the original code while ensuring that the refactored version achieves better decoupling.

                    4. Please provide the refactored code.
                    
                    {STRICT_OUTPUT}
                    """
                    
    