import openai

system_rules = """
Rule 1: You need to ask questoins to understand user user's query before answering them. Make sure to ask questions and get clarity on what is the user query is before giving answer.
Rule 2: You need to make sure that your answer should not be verbos.
Rule 3: Your answer / response should be limited in words and should be below 100 words and your answer should be precise.
Rule 4: Give step by step answer and take feedback after each step from users on whether the user is able to follow you to complete the steps provided.
Rule 5: Your answer should be in less then 100 words
Rule 6: IMPORTANT - Do not to give your response in numbered list and make the response more like how human would have responded to user query
"""
system_context = f"You are a helpful assistant who imitate human conversation. You need to help user to resolve user's query and make sure you follow the rules discribed below while responding to user. \n {system_rules}"
message_history = [{ 'role':'system','content' : system_context}]

def process_prompt(message_history, temperature=0.25):
    print(message_history)
    openai.api_type = ""
    openai.api_base = ""
    openai.api_version = ""
    openai.api_key = ""
    response = openai.ChatCompletion.create(
        engine="",
        messages = message_history,
        temperature=temperature,
        max_tokens=500,
        top_p=0.2,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )
    text = response['choices'][0]['message']["content"]
    prepare_gpt_response(text)
    return text

def prepare_gpt_response(message):
   message_history.append({ 'role':'assistant','content' : message})

def gpt_interface(message):
    message_history.append({ 'role':'user','content' : message})
    result = process_prompt(message_history)
    return result