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
from flask_restful import Resource, Api
from flask import Flask,request
from flask_cors import CORS, cross_origin

openai.api_key = "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"

system_prompt_template = """Use the following pieces of context to answer the users question.
                     If you don't know the answer, just say that you don't know, don't try to make up an answer.
                    {context}
                    ----------------
                    Question: {question}
                    Helpful Answer:"""


messages      = [ SystemMessagePromptTemplate.from_template(system_prompt_template), HumanMessagePromptTemplate.from_template("{question}") ]
prompt        = ChatPromptTemplate.from_messages(messages)
embedding     = OpenAIEmbeddings(openai_api_key = openai.api_key)
llm           = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613",openai_api_key = openai.api_key)

persist_directory="/Users/abhishek/Downloads/anothersite/WarrenBot/Model/chroma_db/"

# load from disk
mydb = Chroma(persist_directory=persist_directory, embedding_function=embedding)

question      = "What are the characteristics of a value investor?" 

#docs = vectorstore.similarity_search(question) len(docs)

qa_chain = RetrievalQA.from_chain_type( llm, retriever=mydb.as_retriever(), chain_type_kwargs = {"prompt": prompt})
result   = qa_chain({"query": question})
print(result)

#prediction api call
class warren_speaks(Resource):
    def get(self,question):
        qa_chain = RetrievalQA.from_chain_type( llm, retriever=mydb.as_retriever(), chain_type_kwargs = {"prompt": prompt})
        result   = qa_chain({"query": question})
        print(result)
        return str(result)

app = Flask(__name__)
CORS(app)

# creating an API object
api = Api(app)
api.add_resource(warren_speaks, '/warren_speaks/<string:question>')

if __name__ == '__main__':
    app.run(debug=True)
