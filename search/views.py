from django.shortcuts import render
from django.http.response import HttpResponse
from search.models import School, Student

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


def goSearch(request):
    allSchools=School.objects.all()
    return render(request,'go_search.html',{'allSchools':allSchools})#将结果传给search.html
def doSearch(request):
    school_id=request.POST.get('school_id','')
    study_status=request.POST.get('study_status','')
    students={}
    if school_id:
        if study_status:
            students=Student.objects.filter(study_status=study_status, school=school_id)
        else :#学生状态为空
            students=Student.objects.filter(school=school_id)
    else:#学校名为空
        if study_status:#学生状态不为空
            students=Student.objects.filter(study_status=study_status)
        else:
            pass
    resultlist=[]
    if students:
        for s in students:
            studentDict=dict()
            studentDict['name']=s.name
            studentDict['telephone'] = s.telephone
            studentDict['address']=s.school.address
            studentDict['school_name'] = s.school.school_name
            resultlist.append(studentDict)
    return render(request,'list_students.html',{"db_result":resultlist})

##适合学校名称输入框的模糊查询，一次查多个学校出来
def handle(request):
    school_name=request.POST.get('school_name','')
    study_status=request.POST.get('study_status','')
    students={}
    schoolIds=''
    if school_name:#学校名不为空
        schools=School.objects.filter(school_name=school_name)#查出满足条件的学校
        if schools:#查询结果不为空,则进行二次查询,查询学生列表
            for sc in schools:
                schoolIds += str(sc.id)+',' #二次查询，需要将学校id当作查询条件
            schoolIds=schoolIds[0:-1]  #去掉最后一位逗号
            if study_status:#学生状态不为空
                #根据学校名称筛选出来的对应school_id和学生状态查询
                students=Student.objects.filter(study_status=study_status).extra(where=['school_id in ('+schoolIds+') '])
            else :#学生状态为空
                #根据学校名称筛选出来的对应school_id查询学生表的所有记录
                students=Student.objects.extra(where=['school_id in ('+schoolIds+') '])
        else:#学校信息不存在
            pass
    else:#学校名为空
        if study_status:#学生状态不为空
            students=Student.objects.filter(study_status=study_status)
        else:
            pass
    resultlist=[]
    if students:
        for s in students:
            studentDict=dict()
            studentDict['name']=s.name
            studentDict['telephone'] = s.telephone
            studentDict['address']=s.school.address
            studentDict['school_name'] = s.school.school_name
            resultlist.append(studentDict)
    return render(request,'resp.html',{"db_result":resultlist})


