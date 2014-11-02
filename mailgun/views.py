from django.shortcuts import render

# from https://developer.rackspace.com/blog/mailgun-and-python/
# and http://blog.mailgun.com/handle-incoming-emails-like-a-pro-mailgun-api-2-0/
def email_in(request):
    if request.method == 'POST':
        is_spam   = request.POST.get['X-Mailgun-SFlag'] == 'Yes'
        sender    = request.POST.get('sender')
        recipient = request.POST.get('recipient')
        subject   = request.POST.get('subject', '')

        body_plain = request.POST.get('body-plain', '')
        body_without_quotes = request.POST.get('stripped-text', '')
        # note: other MIME headers are also posted here...

        # attachments:
        for key in request.FILES:
            file = request.FILES[key]
            # do something with the file


    # Returned text is ignored but HTTP status code matters:
    # Mailgun wants to see 2xx, otherwise it will make another attempt in 5 minutes
    return HttpResponse('OK')
