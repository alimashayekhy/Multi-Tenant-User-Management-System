from django.contrib.auth import get_user_model

User = get_user_model()

# Tenant 1 Users
admin1 = User.objects.create_user(username='admin1', password='adminpass', role='admin', email='alimashayekhiy@gmail.com')
tech1 = User.objects.create_user(username='tech1', password='techpass', role='technician')
operator1 = User.objects.create_user(username='operator1', password='operatorpass', role='operator')
user1 = User.objects.create_user(username='user1', password='userpass', role='user')

# Tenant 2 Users
admin2 = User.objects.create_user(username='admin2', password='adminpass2', role='admin', email='alihamzeh.mashayekhi@gmail.com')
tech2 = User.objects.create_user(username='tech2', password='techpass2', role='technician')
operator2 = User.objects.create_user(username='operator2', password='operatorpass2', role='operator')
user2 = User.objects.create_user(username='user2', password='userpass2', role='user')