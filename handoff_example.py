from agents import Agent, Runner
import asyncio

spanish_agent = Agent(
    name="Spanish agent",
    instructions="You only speak Spanish.",
)

english_agent = Agent(
    name="English agent",
    instructions="You only speak English",
)

tamil_agent = Agent(
    name="Tamil agent",
    instructions="You only speak Tamil",
)

tamil_english_agent = Agent(
    name="Tamil English agent",
    instructions="You only speak English but transliterate tamil words to english and use",
)

triage_agent = Agent(
    name="Triage agent",
    instructions="Handoff to the appropriate agent based on the language of the request.",
    handoffs=[spanish_agent, english_agent, tamil_agent, tamil_english_agent],
)


async def main():
    # result = await Runner.run(triage_agent, input="Tell a Haiku ")
    # result = await Runner.run(triage_agent, input="கவிதைக ")
    #result = await Runner.run(triage_agent, input="¡Disfruta, amigo!")
    result = await Runner.run(triage_agent, input="Tell a Kavithai")
    print(result.final_output)
    # ¡Hola! Estoy bien, gracias por preguntar. ¿Y tú, cómo estás?


if __name__ == "__main__":
    asyncio.run(main())
