from rest_framework import serializers

from main import models


class ItemCreateSerializer(serializers.ModelSerializer):
    product_id = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=15, decimal_places=2)
    category = serializers.CharField(max_length=35)

    class Meta:
        model = models.ProductCheck
        fields = [
            'product_id',
            'quantity',
            'price',
            'category',
        ]


class PlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Place
        fields = [
            'place_id',
            'place_name',
        ]


class CheckCreateSerializer(serializers.ModelSerializer):
    items = ItemCreateSerializer(many=True)
    place = PlaceSerializer(many=False)

    class Meta:
        model = models.Check
        fields = [
            'transaction_id',
            'timestamp',
            'items',
            'total_amount',
            'nds_amount',
            'tips_amount',
            'payment_method',
            'place',
        ]

    def create(self, validated_data):
        items = validated_data.pop('items')
        place = validated_data.pop('place')

        if place:
            place_id = place.get('place_id')

            if not models.Place.objects.filter(place_id=place_id).exists():
                place = models.Place.objects.create(**place)
            else:
                place = models.Place.objects.get(place_id=place_id)

        check = models.Check.objects.create(place=place, **validated_data)

        for item in items:
            category = item.get('category')
            product_id = item.get('product_id')

            if not models.Category.objects.filter(name=category).exists():
                category_obj = models.Category.objects.create(name=category)
            else:
                category_obj = models.Category.objects.get(name=category)

            if not models.Product.objects.filter(product_id=product_id).exists():
                product_obj = models.Product.objects.create(
                    product_id=product_id,
                    price=item.get('price'),
                    category=category_obj
                )
            else:
                product_obj = models.Product.objects.get(product_id=product_id)

            models.ProductCheck.objects.create(
                product=product_obj,
                check_obj=check,
                quantity=item.get('quantity')
            )

        return check


class ItemSerializer(serializers.ModelSerializer):
    product_id = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()

    class Meta:
        model = models.ProductCheck
        fields = [
            'product_id',
            'quantity',
            'price',
            'category',
        ]

    @staticmethod
    def get_product_id(instance):
        return instance.product.product_id

    @staticmethod
    def get_price(instance):
        return instance.product.price

    @staticmethod
    def get_category(instance):
        return instance.product.category.name


class CheckSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    place = PlaceSerializer(many=False)

    class Meta:
        model = models.Check
        fields = [
            'transaction_id',
            'timestamp',
            'items',
            'total_amount',
            'nds_amount',
            'tips_amount',
            'payment_method',
            'place',
        ]
