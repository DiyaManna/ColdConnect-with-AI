import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text


def create_streamlit_app(llm, portfolio, clean_text):
    st.title("Cold Email Generator")
    url_input = st.text_input("Enter a URL: ")
    submit_button = st.button("Submit")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)

            for job in jobs:
                skills = job.get("skills", [])
                portfolio_urls = portfolio.query_links(skills)
                email = llm.write_email(job, portfolio_urls)
                st.code(email, language="markdown")

        except Exception as e:
            st.error(f"An Error Occurred: {e}")


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio(file_path="D:\\cheddkhani\\coldemail\\pythonProject1\\DiyaManna-Resume.pdf-_3_.csv")
    st.set_page_config(layout="wide", page_title="Cold Email Generator")  # , page_icon="E")
    create_streamlit_app(chain, portfolio, clean_text)
