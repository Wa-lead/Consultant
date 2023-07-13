import openai

class GPTx:
    def generate(self, strategy, code):
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": f"{strategy}"},
                {"role": "user", "content": "Please refine the following code: \n" + code + "\n"},
            ]
        )
        return response.choices[0]['message']['content']
            