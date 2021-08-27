from rest_framework import serializers

from .models import Category, Product, Subcategory, menuEntries, submenu, Fakedata

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "get_absolute_url",
            "Bprice",
            "Sprice",
            "amount",
            "get_image",
        )


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "icon",
            "slug",
            "get_absolute_url",
            "products",
        )


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = (
            "id",
            "name",
            "get_absolute_url",
        )


class CategoryTwoSerializer(serializers.ModelSerializer):
    subcategory = SubcategorySerializer(many=True)
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "icon",
            "get_absolute_url",
            "subcategory",
        )


class SubmenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = submenu
        fields = (
            "id",
            "title",
            "page",
        )


class menuSerializer(serializers.ModelSerializer):
    submenu = SubmenuSerializer(many=True)
    class Meta:
        model = menuEntries
        fields = (
            "id",
            "title",
            "page",
            "icon",
            "isOpen",
            "level",
            "submenu"
        )


class FakedataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fakedata
        fields = "__all__"
