from langchain_text_splitters import RecursiveCharacterTextSplitter


text = """LangChain is a framework for developing applications powered by language models. It can be used for chatbots, Generative Question-Answering (GQA), summarization, and much more.
        
The core idea of the library is that we can "chain" together different components to create more advanced use cases around LLMs. Chains may consist of multiple components from several modules:
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separators=["\n\n", "\n", " ", ""]
)

texts = splitter.split_text(text)
print(texts) 