import openai
from langchain.prompts.chat       import ( ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate )
from langchain.document_loaders   import PyPDFLoader
# For checking # Create Document objects for each text chunk
from langchain.docstore.document  import Document
from langchain.text_splitter      import RecursiveCharacterTextSplitter
from langchain.embeddings         import OpenAIEmbeddings
from langchain.vectorstores       import Chroma
from langchain.chat_models        import ChatOpenAI
from langchain.chains             import RetrievalQA
from langchain.document_loaders   import DirectoryLoader
openai.api_key = "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"

system_prompt_template = """Use the following pieces of context to answer the users question.
                     If you don't know the answer, just say that you don't know, don't try to make up an answer.
                    {context}
                    ----------------
                    Question: {question}
                    Helpful Answer:"""


messages = [ SystemMessagePromptTemplate.from_template(system_prompt_template), HumanMessagePromptTemplate.from_template("{question}") ]
prompt   = ChatPromptTemplate.from_messages(messages)
embedding     = OpenAIEmbeddings(openai_api_key = openai.api_key)
llm           = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613",openai_api_key = openai.api_key)

persist_directory="Warren/chroma_db"

# load from disk
mydb = Chroma(persist_directory=persist_directory, embedding_function=embedding)

question      = "What are the characteristics of a value investor?" '''docs = vectorstore.similarity_search(question) len(docs)'''

qa_chain = RetrievalQA.from_chain_type( llm, retriever=mydb.as_retriever(), chain_type_kwargs = {"prompt": prompt})
result   = qa_chain({"query": question})
print(result)

#prediction api call
class warren_speaks(Resource):
    def get(self,question):
        return str("garima" + question)
