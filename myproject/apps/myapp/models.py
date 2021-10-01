from django.db import models

from django.contrib.auth.hashers import check_password, make_password

class User(models.Model):
    name = models.CharField(max_length=45, blank=False, null =False)
    lastname =models.CharField(max_length=45, blank=False, null =False)
    email =models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)

        super(User, self).save(*args, **kwargs)
    
    @staticmethod 
    def authenticate(email, password): 
        results = User.objects.filter(email = email) 
        if len(results) == 1:
            user = results[0]
            bd_password = user.password
            if check_password(password, bd_password):
                  return user        
        return None

    @staticmethod
    def user_exists(email):
        return User.objects.filter(email = email).exists()
