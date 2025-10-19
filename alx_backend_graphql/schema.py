import graphene
from crm.schema import Query as CRMQuery  # <-- import from your app

class Query(CRMQuery, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
