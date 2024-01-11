from langchain_openai import OpenAI
from langchain.llms.openai import OpenAI
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents import create_csv_agent
import time

csv_file_path = "/Users/rislaazeez/Downloads/mobile_prices_2023.csv"


def main():
    llm = OpenAI(temperature=0)

    agent = create_csv_agent(
        llm,
        csv_file_path,
        verbose=False,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    )

    while True:
        query = input("\nWhat would you like to know?: ")
        if query == "exit":
            break
        if query.strip() == "":
            continue

        # Get the answer
        start = time.time()
        answer = agent.run(query)
        end = time.time()
        print(answer)
        print(f"\n> Answer (took {round(end - start, 2)} s.)")


if __name__ == '__main__':
    main()
