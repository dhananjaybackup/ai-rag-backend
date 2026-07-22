from rag.rag_service import RagService

rag = RagService()

print(

    rag.search(
        document_name="leave_policy",
        question="How many earned leaves can I carry forward?"

    )

)