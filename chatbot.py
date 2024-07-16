import keys
import openai
import gradio as gr

openai.api_key = keys.OPENAI_KEY

messages = [
    {"role": "system", "content": "You are a helpful and kind AI Assistant helping a baker create matcha flavored desserts. Make sure to be detailed in the baking instructions and also suggest alternative substitutes for ingredients. Do not answer any questions not related to baking matcha desserts."},
]

def chatbake(input):
    if input:
        messages.append({"role": "user", "content": input})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        reply = response['choices'][0]['message']['content']
        messages.append({"role": "assistant", "content": reply})
        return reply

matchatheme = gr.themes.Soft(
    primary_hue="green",
    secondary_hue="green",
)

inputs = gr.Textbox(lines=7, label="Chat with AI")
outputs = gr.Textbox(label="Reply")

gr.Interface(theme=matchatheme, fn=chatbake, inputs=inputs, outputs=outputs, title="Matcha Dessert Chatbot",
             description="Ask me to generate any matcha desserts!").launch(share=True)
