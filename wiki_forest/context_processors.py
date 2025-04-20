def user_info(request):
    return {
        'user_type': request.session.get('user_type'),
        'user_name': request.session.get('user_name'),
        'user_email': request.session.get('user_email'),
        'user_phone': request.session.get('user_phone'),
        'user_country': request.session.get('user_country'),
        'user_id' : request.session.get('user_id'),
    }