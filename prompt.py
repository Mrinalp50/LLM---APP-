from langchain_core.prompts import PromptTemplate

email_prompt = PromptTemplate(
    input_variables=["topic", "email_type"],
    template="""
You are a professional email writer.

Write a {email_type} email on the following topic:

Topic:
{topic}

Guidelines:
- Use a proper subject line.
- Start with an appropriate greeting.
- Write the email in a professional and polite tone.
- Keep the email concise (150–250 words).
- End with a suitable closing and signature.
"""
)
