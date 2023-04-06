from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import LLMChain, HypotheticalDocumentEmbedder
from langchain.prompts import PromptTemplate
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
import json


def chat(domain, question):
    prompt_template = """質問に回答する文章を書いてください
    質問: {question}
    回答:"""
    prompt = PromptTemplate(
        input_variables=["question"], template=prompt_template)
    llm_chain = LLMChain(llm=OpenAI(), prompt=prompt)

    embeddings = HypotheticalDocumentEmbedder(
        llm_chain=llm_chain,
        base_embeddings=OpenAIEmbeddings(),
    )

    with open(f"{domain}.txt") as f:
        bocchi_txt = f.read()
    text_splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=0,
        separator="。"
    )
    texts = text_splitter.split_text(bocchi_txt)
    query = question

    docsearch = FAISS.from_texts(texts, embeddings)
    docs = docsearch.similarity_search(query, k=1)

    chain = load_qa_chain(OpenAI(), chain_type="stuff")
    result = json.loads(json.dumps(chain({"input_documents": docs, "question": query},
                                         return_only_outputs=True)))["output_text"]
    print(result)
    return result
