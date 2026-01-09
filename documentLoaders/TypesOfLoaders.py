from langchain_community.document_loaders import TextLoader

# Initialize the loader with the path to your text file
loader = TextLoader("cricket.txt", encoding= "utf-8")

# Load the documents
documents = loader.load()

print(documents[0].page_content)