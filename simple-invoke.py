"""
ChatGoogleGenerativeAI
https://python.langchain.com/v0.2/docs/integrations/chat/google_generative_ai/

このスクリプトは、ChatGoogleGenerativeAIモデルを使用して翻訳を実行するためのlangchain_google_genaiライブラリの使用方法を示しています。
また、プロンプトテンプレートを使用したモデルのチェーンも紹介しています。スクリプトは以下の手順を実行します:
1. `dotenv`を使用して必要な環境変数を読み込みます。
2. 指定されたAPIキー、モデル、およびその他のパラメータで`ChatGoogleGenerativeAI`クラスをインスタンス化します。
3. `ChatGoogleGenerativeAI`モデルを呼び出して、ユーザーの文を英語から日本語に翻訳します。
4. 翻訳されたメッセージとその内容を印刷します。
5. 入力言語と出力言語を指定して`ChatPromptTemplate`クラスを使用してプロンプトテンプレートを作成します。
6. プロンプトテンプレートを`ChatGoogleGenerativeAI`モデルとチェーンさせます。
7. チェーンされたモデルを呼び出して、ユーザーの文を英語から日本語に翻訳します。
8. 翻訳されたメッセージとその内容を印刷します。
9. トークン数を含むチェーンモデルの使用メタデータを出力します。
注意: スクリプトは、`.env`ファイルから環境変数を読み込むために`dotenv`ライブラリを使用します。
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import time

load_dotenv()

# Instantiation
llm = ChatGoogleGenerativeAI(
    api_key=os.getenv("GOOGLE_API_KEY"),
    # Gemini 料金モデル -> https://ai.google.dev/pricing?hl=ja
    # model="gemini-1.5-pro",
    model="gemini-1.5-flash",
    temperature=0,
    max_output_tokens=None,
    timeout=None,
    max_retries=2,
)

# Invocation
message = [
    ("system","You are a helpful assistant that translates English to Japanese. Translate the user sentence."),
    ("human","I love programming."),
]
ai_msg = llm.invoke(message)
print(ai_msg)
print(ai_msg.content)

time.sleep(5)

# Chaining model with a prompt template
from langchain_core.prompts import ChatPromptTemplate

template_message = [
    ("system","You are a helpful assistant that translates {input_language} to {output_language}. Translate the user sentence."),
    ("human","{input}"),
]
prompt = ChatPromptTemplate.from_messages(template_message)

chain = prompt | llm
chain_msg = chain.invoke({
    "input_language": "English",
    "output_language": "Japanese",
    "input": "I love programming for enterprise business."
})
print(chain_msg)
print(chain_msg.content)
#print(type(chain_msg.content))

print(chain_msg.usage_metadata)
print('token-count(input):',chain_msg.usage_metadata['input_tokens'])

# dict.get() method is used to avoid KeyError
print('token-count:',chain_msg.usage_metadata.get('iiiinput_tokens', 'key not found'))