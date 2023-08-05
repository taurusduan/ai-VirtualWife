from __future__ import annotations
from abc import ABC, abstractmethod
# from .openai.aili_anchor_chat_robot import Aili
# from .openai.cat_lady_chat_robot import CatLady
# from .openai.enice_chat_robot import Enice
from .pygmalionai.pygmalionai_chat_robot import Pygmalionai
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

# 定义llm_model的抽象类


class LlmModelStrategy(ABC):
    @abstractmethod
    def chat(self, role_name: str, query: str) -> str:
        pass


# 定义策略类实现
class OpenAILlmModelStrategy(LlmModelStrategy):
    def chat(self, role_name: str, you_name: str, query: str) -> str:
        result = ""
        # if role_name == "aili":
        #     result = Aili.chat(query=query)
        # elif role_name == "catLady":
        #     result = CatLady.chat(query=query)
        # elif role_name == 'enice':
        #     result = Enice.chat(query=query)
        return result


class PygmalionAILlmModelStrategy(LlmModelStrategy):
    def chat(self, role_name: str, you_name: str, query: str) -> str:
        return Pygmalionai.chat(role_name=role_name, you_name=you_name, query=query)


# 定义驱动类
class LlmModel:
    def __init__(self, strategy: LlmModelStrategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: LlmModelStrategy) -> None:
        self._strategy = strategy

    def chat(self, role_name: str, you_name: str, query: str) -> str:
        return self._strategy.chat(role_name=role_name, you_name=you_name, query=query)


class LlmModelDriver():
    def chat(self, type: str, role_name: str, you_name: str, query: str) -> str:
        if type == "openai":
            strategy = OpenAILlmModelStrategy()
        elif type == "pygmalionai":
            strategy = PygmalionAILlmModelStrategy()
        else:
            raise ValueError("Unknown type")
        
        logger.debug(
            f"[BIZ] # LlmModelDriver.chat # type:{type} role_name:{role_name} you_name={you_name} query:{query}#")
        llmModel = LlmModel(strategy)
        result = llmModel.chat(role_name=role_name,
                               you_name=you_name, query=query)
        logger.debug(
            f"[BIZ] # LlmModelDriver.chat # type:{type} role_name:{role_name} you_name={you_name} query:{query} => result:{result} #")
        return result
