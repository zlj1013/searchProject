from django.shortcuts import render
from django.http.response import HttpResponse
from search.models import School, Student
from . import service
#import service

# Create your views here.
def hello(request):
    return HttpResponse('hello，在网页上打印文字成功啦。。。')

def hello1(request):
    '''
    render把context的内容, 加载进templates中定义的文件, 并通过浏览器渲染呈现.
    context默认为字典格式
    '''
    context={}
    context['hello']='根据hello.html的hello关键字打开此行内容'
    return render(request, 'hello.html', context)

'''

'''
def search(request):
    return render(request,'search.html',{})#将结果传给search.html

def search1(request):
    allSchools = School.objects.all();
    return render(request,'search.html',{"allSchools": allSchools})#将结果传给search.html



def handle1(request):
    schoolcontent=request.POST.get('学校名称',False)
    db_result=School.objects.filter(school_name=schoolcontent)
    studentcontent=request.POST.get('毕业状态',False)#对应search.html中<input type="text",name="搜索内容">
    #db_result=School.objects.filter(study_status=content)
    print(db_result)
    student=db_result.school_student.all()
    #.filter(study_status=studentcontent)
    return render(request,'resp.html',{"db_result":student})# 将列表值返回给resp.html，使用resp接收

def handle(request):
    school_name=request.POST.get('school_name', '')
    study_status=request.POST.get('study_status', '')
    schoolIds = ''
    
    if school_name:
        
        schools=School.objects.filter(school_name=school_name) #查出满足条件的学校
        if schools: #如果查询结果不为空,则进行二次查询,查询学生列表
            for sc in schools:
                schoolIds += str(sc.id) + "," #二次查询，需要将学校id当作查询条件
            schoolIds = schoolIds[0:-1]
            if study_status:
                students = Student.objects.filter(study_status=study_status).extra(where=['school_id in ('+ schoolIds +')'])
            else:
                students = Student.objects.extra(where=['school_id in ('+ schoolIds +')'])
    else:
        if study_status:
            students = Student.objects.filter(study_status=study_status);
        else: #学校信息不存在
            pass
    
    resultList = []
    if students:
        for s in students:
            studentDict = dict()
            studentDict['name'] = s.name
            studentDict['telephone'] = s.telephone
            studentDict['school_name'] = s.school_id.school_name
            resultList.append(studentDict)
            print('resultList %s ', resultList)
    return render(request,'resp.html',{"db_result":resultList})# 将列表值返回给resp




