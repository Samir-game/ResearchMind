from langchain.tools import tool
from firecrawl import Firecrawl
import os
from dotenv import load_dotenv
from rich import print

load_dotenv()

firecrawl = Firecrawl(
    api_key=os.getenv("FIRECRAWL_API_KEY")
)


@tool
def web_search(query: str) -> str:
    """Search the web for recent and relevant information.
    Returns titles, URLs, and snippets."""
    try:
        results = firecrawl.search(
            query,
            limit=2
        )

        out = []

        # Firecrawl SDK search results contain web results
        for r in results.web:
            out.append(
                f"Title: {r.title}\n"
                f"URL: {r.url}\n"
                f"Snippet: {str(r.description or '')[:20]}\n"
            )

        return "\n----\n".join(out) if out else "No results found."

    except Exception as e:
        return f"Web search failed: {str(e)}"

print(web_search.invoke({"query": "latest AI news"}))