import asyncio
from langchain_community.document_loaders import AsyncHtmlLoader
from langchain_community.document_transformers import Html2TextTransformer

async def main():
    urls = ["https://investors.sonos.com/investors/default.aspx"]
    loader = AsyncHtmlLoader(urls)
    
    docs = loader.load()

    print(docs)
    
    # html2text = Html2TextTransformer()
    # if docs:
    #     docs_transformed = html2text.transform_documents(docs)
    #     print(docs_transformed[0].page_content)
    # else:
    #     print("No documents were loaded.")

# Run the main async function
asyncio.run(main())

