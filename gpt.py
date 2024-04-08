from openai import OpenAI
import os

os.environ["OPENAI_API_KEY"] = ''
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI()

def properties(prompt):
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature = 0,
        max_tokens=50,
        messages=[
                    {"role":"system", "content": "You analyze user request, and output tokenizer for noun and full instruction and properties into. \
                        ['noun:?', 'instruction:?'] \
                     "},
                    {"role":"user", "content": prompt}
                    ] 
        )
    reply_content = response.choices[0].message.content
    print(f"User propesties: {reply_content}")
    

def request(prompt):
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature = 0,
        max_tokens=1,
        messages=[
                    {"role":"system", "content": "You analyze user input, and output the names of functions to fullfil a user's needs.\
                      If the user is making a request subject, that means the '0' is needed. \
                      If the user is making a full question pure without request subject, that means the '1' is needed. \
                      You can output: 0,1 to fulfill a request, otherwise reply: 'chat'"},
                    {"role":"user", "content": prompt}
                    ] 
        )
    reply_content = response.choices[0].message.content.strip()
    print(reply_content)
    return reply_content

user_input = "Me entrega as ultimas transações do dia 10 de janeiro do usuário 1001"    
asked = request(user_input)

if asked == '1': 
    print('Duvida')
elif asked == '0':
     print('request')
     properties(user_input)
else: 
    print('fallback')
