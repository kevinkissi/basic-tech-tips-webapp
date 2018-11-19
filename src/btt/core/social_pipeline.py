from requests import request, HTTPError

from django.core.files.base import ContentFile


#def save_profile_picture(strategy, user, response, details, is_new=False,
#                         *args, **kwargs):

def save_profile_picture(backend, strategy, user, response, details, is_new=False, *args, **kwargs):
    # Save Facebook profile photo into a user profile, assuming a profile model
    # with a profile_photo file-type attribute':
#        url = 'http://graph.facebook.com/{0}/picture?type=large&width=150&height=150'.format(response['id'])
    url = None
    if backend.name == 'facebook':
        url = 'http://graph.facebook.com/{0}/picture?type=large&width=150&height=150'.format(response['id'])
    if backend.name == 'twitter':
        url = response.get('profile_image_url', '').replace('_normal','')
    if backend.name == 'google-oauth2':
        url = response['image'].get('url')
        ext = url.split('.')[-1]

        try:
            response = request('GET', url)
            response.raise_for_status()
        except HTTPError:
            pass
        else:
            profile = user.profile
            profile.url = url
            profile.save()
