from rest_framework import serializers
from MyTeam.models import TeamMember

class TeamMemberSerializer(serializers.ModelSerializer):
	class Meta:
		model = TeamMember
		feilds = '__all__'
		exclude = ()