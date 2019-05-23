from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    # 전체 문장
    full_text = request.GET['fulltext']
    # 총 단어 수 세는 기능 구현
    word_list = full_text.split()
    # 각 단어 별로 나온 횟수 세는 기능 구현
    word_dictionary = {}
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1
    return render(request, 'count.html',{'fulltext':full_text,'total':len(word_list),'dictionary':word_dictionary.items()})
