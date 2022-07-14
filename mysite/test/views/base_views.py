from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question
from django.db.models import Q

def index(request):
    page = request.GET.get('page', '1')  # Default 페이지 가져오기
    kw = request.GET.get('kw', '')  # 검색어
    question_list = Question.objects.order_by('-create_date') # 게시글 객체 작성순으로 가져오기
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()
    paginator = Paginator(question_list, 10)  # 페이지 객체에 10개씩 데이터 저장하기
    page_obj = paginator.get_page(page) # 해당 페이지에 맞는 데이터 가져오기
    context = {'question_list': page_obj, 'page': page, 'kw': kw} #전해줄 데이터
    return render(request, 'test/question_list.html',context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'test/question_detail.html',context)

def tech(request):
    return render(request,'test/tech.html')




