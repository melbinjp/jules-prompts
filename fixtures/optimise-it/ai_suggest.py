"""AI slot suggestions."""
import os

from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def suggest_slot(member, machine, free):
    prompt = (
        f"A woodshop member, {member}, wants to use the {machine}. "
        f"Free hours: {free}. Suggest the best hour and say why in one sentence."
    )
    reply = client.chat.completions.create(
        model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}]
    )
    return reply.choices[0].message.content
