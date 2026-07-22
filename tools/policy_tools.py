from rag.document import Documents
from rag.rag_service import RagService

rag_service = RagService()

# def search_leave_policy(question):
#     return rag_service.search(question)

def search_leave_policy(question):
    return rag_service.search(
        Documents.LEAVE,
        question
    )


def search_gratuity_policy(question):
    return rag_service.search(
        Documents.GRATUITY,
        question
    )