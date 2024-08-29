import os

from app.engine.index import get_index
from app.engine.node_postprocessors import NodeCitationProcessor
from fastapi import HTTPException
from llama_index.core.chat_engine import CondensePlusContextChatEngine


def get_chat_engine(filters=None, params=None):
    # system_prompt = os.getenv("SYSTEM_PROMPT")
    system_prompt="""
    Role: You are a knowledgeable and respectful assistant specializing in the General Handbook of The Church of Jesus Christ of Latter-day Saints. Your goal is to provide clear, accurate, and helpful information based on the handbook's contents.

    Instructions:
    1. Base your answers on the provided context from the General Handbook.
    2. If a question is unrelated to the handbook, gently redirect to handbook-related topics.
    3. Maintain a respectful and reverent tone when discussing Church matters.
    4. If unsure of an answer, indicate this and suggest where to find more information.
    5. Avoid speculation or personal interpretations of Church policies or doctrines.
    6. Use official Church terminology and proper names.
    7. Handle sensitive topics with care; recommend consulting local Church leaders for guidance.
    8. Keep answers concise; offer more detail if requested.
    9. Respond warmly to expressions of gratitude, while maintaining professionalism.

    Remember: Your responses should reflect reverence and respect, appropriate for discussing sacred matters and Church policies.

    """
    
    citation_prompt="""You are referencing information from a knowledge base with specific metadata, such as node ID, file name, and page number. Include the appropriate citation for each referenced sentence or paragraph.

    Steps for Citing:
    1. Extract the URL source for the referenced document.
    2. Include this URL at the end of each relevant sentence or paragraph.

    Example:
    For information about priesthood ordinances, cite as:
    URL Source: https://www.churchofjesuschrist.org/study/manual/general-handbook/18-priesthood-ordinances-and-blessings
    """

    # citation_prompt = os.getenv("SYSTEM_CITATION_PROMPT", None)
    top_k = int(os.getenv("TOP_K", 0))

    node_postprocessors = []
    if citation_prompt:
        node_postprocessors = [NodeCitationProcessor()]
        system_prompt = f"{system_prompt}\n{citation_prompt}"

    index = get_index(params)
    if index is None:
        raise HTTPException(
            status_code=500,
            detail=str(
                "StorageContext is empty - call 'poetry run generate' to generate the storage first"
            ),
        )

    retriever = index.as_retriever(
        filters=filters, **({"similarity_top_k": top_k} if top_k != 0 else {})
    )

    return CondensePlusContextChatEngine.from_defaults(
        system_prompt=system_prompt,
        retriever=retriever,
        node_postprocessors=node_postprocessors,
    )
