from services.QdrantService import QdrantService

qdrant = QdrantService()

qdrant.delete_collection()
qdrant.create_collection()

qdrant.seed_collection()

print("DONE!")
