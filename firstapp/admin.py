from django.contrib import admin
from firstapp.models import Contact

# Step 2
# Register your model here so it appears in Django admin dashboard
# Without this, even if model exists, it won't show in /admin panel

admin.site.register(Contact) # Here we're registring the models

# Step 3, go to 'app.py' copy app name and register it in 'settings.py' file in ur project folder
