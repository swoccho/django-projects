import re
from string import punctuation
from django.shortcuts import render

def index(request):
    return render(request , 'index.html')

def about(request):
    return render(request, 'about.html')


def analyze(request):
    user_text = request.POST.get('text', 'default')
    user_input = request.POST.get('text' , 'default')
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
            user_text = analyzed
            analyzation = {'purpose': 'Removed Punctuation' ,'user_input': user_input, 'analyzed_text' : user_text}
            


        if  captalize == 'on':
            analyzed =''
            for char in user_text:
                analyzed = analyzed + char.upper()
            user_text = analyzed
            analyzation = {'purpose': 'Captalized Text','user_input': user_input, 'analyzed_text': user_text}
            

        
        if remove_newline == 'on':
            analyzed =''
            for char in user_text:
                if char != '\n' and char != '\r':
                    analyzed = analyzed + char
            user_text = analyzed

            analyzation = {'purpose': 'Captalized Text','user_input': user_input, 'analyzed_text': user_text}



            
        

        if removespace == 'on':
            # analyzed =''
            
            # for index ,char in enumerate(user_text):
            #     if not (user_text[index] == ' ' and user_text[index +1] == ' '):
            #         analyzed = analyzed + char
            #         
          
            def remove_extra_space():
                words = [word for word in user_text.split(' ') if word != '']
                return ' '.join(words)

            analyzed = remove_extra_space()
    
            user_text= analyzed
            analyzation = {'purpose': 'Extra spaces Removed' ,'user_input':user_input, 'analyzed_text' : user_text}
            


        if charcount == 'on':
            
            count = 0
            for char in  user_text:
                count += 1
            analyzation = {'method' : 'character counted' ,'user_input':user_input,'analyzed_text':user_text, 'char_text' : f'Your sentence has {count} characters' }
            

        if wordcount == 'on':
            count = len(re.findall(r'\w+' , user_text))

            analyzation = {'words':'Word counted' ,'user_input':user_input,'analyzed_text':user_text ,'word_text': f' Your sentence has {count} words.'}

        if (wordcount=='on' and charcount == 'on'):
            character_count = 0
            for char in user_text:
                character_count +=1

            word_count = len(re.findall(r'\w+' , user_text))

            analyzation = {'user_input' : user_input ,'analyzed_text':user_text, 'word_and_char_count' : f'Your sentence has {character_count} characters and {word_count} words.'}

        return render(request, 'analyzed.html',analyzation)

    except UnboundLocalError:
        return render (
            request,'index.html',
            {
                'error_massage': "You didn't select any operation."
            }
        )




    
    
