from django.contrib.auth import get_user_model
import graphene
from graphene_django import DjangoObjectType

from .models import CustomUser
# import graphene
# from graphene_django import DjangoObjectType


class QuestionType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = ("username", "email")

class Query(graphene.ObjectType):
    questions = graphene.List(QuestionType)
    question_by_id = graphene.Field(QuestionType, id=graphene.String())
    question_by_email = graphene.Field(QuestionType, enail=graphene.String())
    def resolve_questions(root, info, **kwargs):
        # Querying a list
        return CustomUser.objects.all()

    def resolve_question_by_id(root, info, id):
        # Querying a single question
        return CustomUser.objects.get(pk=id)
    
    def resolve_question_by_email(root, info, email):
        return CustomUser.objects.get(emaii = email)