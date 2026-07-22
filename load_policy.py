from rag.rag_service import RagService

rag = RagService()

# rag.load_policy("policy/leave_policy.pdf")

rag.load_policy("policy/leave_policy.pdf", document_name="leave_policy")

rag.load_policy("policy/gratuity_policy.pdf", document_name="gratuity_policy")

print("All policies loaded successfully.")
