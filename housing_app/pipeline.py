from .models import UserProfile

# code retrieved from https://stackoverflow.com/questions/29575713/retrieving-profile-picture-from-google-and-facebook-in-python-social-auth/29576422
def get_avatar(backend, strategy, details, response,
        User=None, *args, **kwargs):
    url = None
    if backend.name == 'google-oauth2':
        url = response['picture']
        # .get('url')
        ext = url.split('.')[-1]
    if url:
        if (User==None):
            User = User.objects.get(username = kwargs['username'])
        UserProfile.objects.get(user=User).avator = url
        UserProfile.objects.get(user = User).save()

