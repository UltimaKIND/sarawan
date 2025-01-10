from rest_framework.serializers import ModelSerializer, SerializerMethodField
from slugify import slugify

from store.models import Category, Product


class CategorySerializer(ModelSerializer):
    """
    сериализатор модели категории
    """

    subcategories = SerializerMethodField(
        read_only=True, method_name="get_subcategories"
    )

    class Meta:
        model = Category
        fields = ["id", "parent", "category_name", "subcategories"]

    def create(self, validated_data):
        """
        генерирует slug включая slug родительской категории
        """
        slug = slugify(validated_data["category_name"])
        if not "parent" in validated_data:
            validated_data["slug"] = slug
            return Category.objects.create(**validated_data)
        else:
            parent = Category.objects.get(id=validated_data["parent"].id)
            slug = f"{parent.slug}/{slug}"
            validated_data["slug"] = slug
            return Category.objects.create(**validated_data)

    def get_subcategories(self, obj):
        """
        возвращает сериализованные subcategories
        """
        serializer = CategorySerializer(instance=obj.childs.all(), many=True)
        return serializer.data

    def to_representation(self, instance):
        """
        убирает поле subcategories и parent если их нет
        """
        category = super(CategorySerializer, self).to_representation(instance)
        if not instance.childs.first():
            category.pop("subcategories")
        if not instance.parent:
            category.pop("parent")
        return category


class CategorySpecialSerializer(ModelSerializer):
    """
    сериализатор модели категории
    """

    parent = SerializerMethodField(read_only=True, method_name="get_parent")

    class Meta:
        model = Category
        fields = ["id", "category_name", "parent"]

    def get_parent(self, obj):
        """
        возвращает сериализованные subcategories
        """
        serializer = CategorySpecialSerializer(instance=obj.parent)
        return serializer.data

    def to_representation(self, instance):
        """
        убирает поле parent если его нет
        """
        category = super(CategorySpecialSerializer, self).to_representation(instance)
        if not instance.parent:
            category.pop("parent")
        return category


class ProductSerializer(ModelSerializer):
    """
    сериализатор модели продукта
    """

    category_repr = SerializerMethodField(read_only=True, method_name="get_category")
    images = SerializerMethodField(read_only=True, method_name="get_images")

    class Meta:
        model = Product
        fields = (
            "id",
            "product_name",
            "slug",
            "category_repr",
            "category",
            "price",
            "images",
        )

    def get_category(self, obj):
        """
        возвращает сериализованную категорию
        """
        serializer = CategorySpecialSerializer(instance=obj.category)
        return serializer.data

    def get_images(self, obj):
        first_image = obj.first_image if obj.first_image else None
        second_image = obj.second_image if obj.second_image else None
        third_image = obj.third_image if obj.third_image else None

        return [first_image, second_image, third_image]

    def to_representation(self, instance):
        """
        убирает поле category
        """
        product = super(ProductSerializer, self).to_representation(instance)
        product.pop("category")
        return product
