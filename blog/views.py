from django.shortcuts import render

def post_list(request):
    return render(request,'blog/post_list.html',{})     # render は request 内容を使って blog/post_list.html  を組み立てを行う
