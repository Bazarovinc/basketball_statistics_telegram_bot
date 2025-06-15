
from typing import Sequence
import uuid

from langchain_core.language_models import LanguageModelLike
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import BaseTool, tool
from langchain_gigachat.chat_models import GigaChat
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver
from langchain_deepseek import ChatDeepSeek
import pytesseract


PROMT = ("Твоя задача извлечь данные из таблиц только для строки, у которой Фамилия Имя имеет значение {player}, "
         "колонки с пропусками заполнить 0. "
         "Извлеки значения только следующих столбцов:"
         "№, Фамилия Имя, О, 2 очк. З/В, 3 очк. З/В, штраф. З/В, АП, ПХ, БШ, СЩ, ЧЩ, ВС, ПТ, ФС, Ф, +/-, КПИ. "
         "Извлеченные данные представь в виде json"
         # "Извлеченные данные представить в виде json с полями по каждой колонке."
         )

PLAYER_NAME = "Веселенко Никита"


@tool
def print_response(statistics_data: dict) -> None:
    """
    Выводит полученные данные по статистике игрока
    Args:
        statistics_data: полученные данные
    """
    print(statistics_data)


FILE = "project_docs/files/photo_2025-06-14 18.40.50.jpeg"

class LLMAgent:
    def __init__(self, model: LanguageModelLike, tools: Sequence[BaseTool]):
        self._model = model
        self._agent = create_react_agent(
            model,
            tools=tools,
            checkpointer=InMemorySaver())
        self._config: RunnableConfig = {
                "configurable": {"thread_id": uuid.uuid4().hex}}

    def upload_file(self, file):
        file_uploaded_id = self._model.upload_file(file).id_  # type: ignore
        return file_uploaded_id

    def invoke(
        self,
        content: str,
        attachments: list[str]|None=None,
        temperature: float=0.1
    ) -> str:
        """Отправляет сообщение в чат"""
        message: dict = {
            "role": "user",
            "content": content,
            **({"attachments": attachments} if attachments else {})
        }
        result = self._agent.invoke(
            {
                "messages": [message],
                "temperature": temperature
            },
            config=self._config)
        print(result["messages"][1].content)




def main():
    model = GigaChat(
        model="GigaChat-2-Max",
        verify_ssl_certs=False,
        credentials="NzZlMWY0ZjUtOGViNC00YTIwLWI2YTAtOTU2NTdmYzBmMjE2OmVlYjBiMzIyLWEzNDUtNDRiZC05NjZmLWRjMGRlYmM4MjU3Ng=="
    )
    agent = LLMAgent(model, tools=[])
    file_uploaded_id = agent.upload_file(open(FILE, "rb"))
    agent_response = agent.invoke(content=PROMT.format(player=PLAYER_NAME), attachments=[file_uploaded_id])
    print(agent_response)


if __name__ == "__main__":
    main()
