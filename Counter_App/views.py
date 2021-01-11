from django.shortcuts import render, redirect

def session_counter(request):
    print('************this is the session statement**************')
    if 'counter' in request.session:
        request.session['counter'] +=1
    else:
        print("we are adding [counter]")
        request.session['counter'] = 1        #creates the session here

    print('***'*20)
    print(request.session['counter'])
    print('***'*20)


    return render(request,'index.html')

def destroy_session(request):
    print('we are destroying all the evidence')
    del request.session['counter']
    return redirect('/')
