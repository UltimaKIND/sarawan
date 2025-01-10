from rest_framework.serializers import ModelSerializer  # type: ignore

from users.models import User


class UserSerializer(ModelSerializer):
    """
    сериализатор модели пользователя
    """

    class Meta:
        model = User
        fields = "__all__"


class OtherUserSerializer(ModelSerializer):
    """
    сериализатор модели другого пользователя
    """

    class Meta:
        model = User
        exclude = ("password",)
