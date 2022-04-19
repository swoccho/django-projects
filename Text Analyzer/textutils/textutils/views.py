import re
from string import punctuation
from django.http import HttpResponse,Http404
from django.shortcuts import render



def index(request):
    return render(request , 'index.html')

def _analization(purpose,analyzed):
    return {'purpose': purpose, 'analyzed_text': analyzed}


def analyze(request):
    user_text = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc' , 'off')
    captalize = request.POST.get('uppercase' , 'off')
    remove_newline = request.POST.get('removenewline' , 'off')
    removespace = request.POST.get('extraspaceremove' , 'off')
    charcount = request.POST.get('charcount' , 'off')
    wordcount = request.POST.get('wordcount' , 'off')

    try:
        if removepunc == 'on':
            analyzed =''
            for char in user_text:
                if char not in punctuation:
                    analyzed = analyzed +char

            analyzation = {'purpose': 'Removed Punctuation' , 'analyzed_text' : analyzed}
            user_text = analyzed


        if  captalize == 'on':
            analyzed =''
            for char in user_text:
                analyzed = analyzed + char.upper()

            analyzation = {'purpose': 'Captalized Text', 'analyzed_text': analyzed}
            user_text = analyzed

        
        if remove_newline == 'on':
            analyzed =''
            for char in user_text:
                if char != '\n' and char != '\r':
                    analyzed = analyzed + char
            analyzation = _analization('New line removed' , analyzed)
        

        if removespace == 'on':
            analyzed =''
            for index ,char in enumerate(user_text):
                if not (user_text[index] == ' ' and user_text[index +1] == ' '):
                    analyzed = analyzed + char
            analyzation =  _analization('Extra spaces Removed' , analyzed)
            user_text= analyzed


        if charcount == 'on':
            
            count = 0
            for char in  user_text:
                count += 1
            analyzation = _analization('CHaracter counted' , f'Your sentence has {count} characters')
            

        if wordcount == 'on':
            count = len(re.findall(r'\w+' , user_text))

            analyzation = _analization('Word counted' , f' Your sentence has {count} words.')


        return render(request, 'analyzed.html',analyzation)

    except UnboundLocalError:
        return render (
            request,'index.html',
            {
                'error_massage': "You didn't select any operation."
            }
        )




    
    
