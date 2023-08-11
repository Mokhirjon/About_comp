from rest_framework import serializers
class Computerserializers(serializers.ModelSerializer):
    comp_name=serializers.CharField()
    comp_vers=serializers.CharField()
    comp_summa=serializers.CharField()
    date_of_created=serializers.DateField()
    other_info=serializers.CharField()