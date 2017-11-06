

# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view

from rest_framework.response import Response

from ..models import Snippet
from ..serializers import SnippetSerializer

'''
snippets/urls.py에 urlpatterns 작성
config/urls.py에 snippets.urls를 include

아래의 snippet_list뷰가
    /snippets/에 연결되도록 구
'''

# CSRF 인증을 사용하지 않음
#@csrf_exempt

# 이 뷰는 api_view 형태로 동작 - request에 HttpRequest가 아닌 Request가 주어짐
@api_view(['GET','POST'])
def snippet_list(request, format=None):
    if request.method == 'GET':
        # snippets는 모든 Snippet의 쿼리셋
        snippets = Snippet.objects.all()
        # 쿼리셋을 serialize할 때는 many=True 옵션 추가
        serializer = SnippetSerializer(snippets, many=True)
        # JsonResponse는 기본적으로 dict형 객체를 받아 처리함
        # JSON 방식으로 response. safe 옵션이 False이면 주어진 데이터가 dict가 아니어도 됨(리스트 객체가 옴)

        # 데이터를 적절히 렌더링해주는 response 객체 반환
        return Response(serializer.data)

    elif request.method=='POST':
        # request로 전달된 데이터들을 JSONParser를 사용해 파이썬 데이터 형식으로 파싱
        #data = JSONParser().parse(request)
        # 처리된 데이터를 사용해 SnippetSerializer 인스턴스 생성
        serializer = SnippetSerializer(data=request.data)
        # 인스턴스에 주어진 데이터가 유효할 경우
        if serializer.is_valid():
            # 인스턴스의 save() 멤서드를 호출해 Snippet 객체 생성
            serializer.save()
            # HTTP 상태코드(201 created) 로 Snippet 생성에 사용된 serializer의 내용을 보내줌
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 유효하지 않으면 인스턴스의 에러들을 HTTP 400 Bad request 상태코드와 함께 보내줌
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#@csrf_exempt
@api_view(['GET','PUT','DELETE'])
def snippet_detail(request,pk,format=None):
    '''

    :param request:
    :param pk:
    :return:
    '''
    # pk에 해당하는 Snippet이 존재하는 지 확인 후 snippet 변수에 할당
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoseNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        # GET 요청시 snippet을 serialize한 결과를 보여줌
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)
    elif request.method=='DELETE':
        # DELETE 요청시에는 해당 Snippet 인스턴스 삭제
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method=='PUT':
        # PUT 요청시에는 전달된 데이터를 이용해서 snippet 인스턴스 내용 변경

        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

