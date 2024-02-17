from django.shortcuts import render,HttpResponse
import requests

# def index(request):
    

def get_redirected_links(url):
    session = requests.Session()
    response = session.head(url, allow_redirects=True)

    # Extract all the redirected URLs
    redirected_links = [history.url for history in response.history]

    redirected_links.append(response.url)

    return redirected_links

def index(request):
    if request.method == 'POST':
        input_url = request.POST.get('url', '')
        print(input_url)
        redirected_links = get_redirected_links(input_url)

        result = "\n".join([f"Redirect {index + 1}: {link}" for index, link in enumerate(redirected_links)])

        context = {
            "redirectionsData":result
        }
        return render(request,'data.html',context)
    
    return render(request,'index.html')