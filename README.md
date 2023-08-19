# Consultant

## Description

Consultant provides a convenient way to interact with OpenAI's GPT-3.5 to refactor your code via decorators.

## Installation
> git clone https://github.com/Wa-lead/Consultant.git

> pip install -r requirements.txt

> pip install e . 

## Usage
1. Export your OpenAI API key as an environment variable:
   > export OPENAI_API_KEY= < your key >

2. Use it as a decorator:

https://github.com/Wa-lead/Consultant/assets/81301826/bc7747a9-6be0-44f4-ae74-6c046025110e

3. Add your own prompts

   ```python
   from Consultant.prompt import Prompt
   from Consultant.consultant import Consultant

   my_custom_prompt = Prompt(
                           name = 'Documenter',
                           description='This prompt aims to provide well documented code.',
                           instruction='Your job is to read a given code and provide standard documentation and comments for it.',
                           )
   @Consultant.consult(my_custom_prompt)
   def smallest_number(list: list) -> int:
      smallest = list[0]
      for number in list:
         if number < smallest:
               smallest = number
      return smallest

      ```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.



