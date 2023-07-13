# Consultant

## Description

Consultant provides a convenient way to interact with OpenAI's GPT-3.5 to refactor your code via decorators.

## Installation
> git clone https://github.com/Wa-lead/Consultant.git

> pip install -r requirements.txt

## Usage
1. Export your OpenAI API key as an environment variable:
   > export OPENAI_API_KEY= < your key >

2. Use it as a decorator:
   ```python
   from Consultant.consultant import consultant
    from Consultant.prompt import Prompt


    @consultant(Prompt.ENGINEER)
    def unoptimized_function(a,b):
        c = [] #common elements between a and b
        for i in a:
            for j in b:
                if i == j:
                    c.append(i)
        return c


    a = [1,2,3]
    b = [2,3,4]

    unoptimized_function(a,b)

    #OUTPUT:
    """
    def find_common_elements(a, b):
    return list(set(a).intersection(b))
    """
   ```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.



