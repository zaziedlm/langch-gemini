# Langchain による Google Geminiモデルアクセス 検証実装
Geminiモデルに対して、Langchain実装を用いたLLMアクセスを検証します 

ChatGoogleGenerativeAI
https://python.langchain.com/v0.2/docs/integrations/chat/google_generative_ai/

## 概要

Langchain, ChatGoogleGenerativeAI を使用して、Geminiモデルへの問い合わせを実行します。加えて、テンプレートとのチェーンによる実装も用意します。

## 注意事項

Gemini API 課金には注意が必要。Proモデルの一日あたりの制限値は厳しいので、Flashモデルでの試行を推奨します。

Gemini API: Be careful with billing. The daily limit for the 'Pro' model is strict, so we recommend trying the 'Flash' model.
