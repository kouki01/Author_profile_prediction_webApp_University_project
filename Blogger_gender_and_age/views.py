from django.shortcuts import render
from googleapiclient.errors import HttpError
from Blogger_gender_and_age.models import Author
from apiclient.discovery import build
from bs4 import BeautifulSoup
from django.utils import timezone
import pprint
from classifier import predict
import re

service = build('blogger', 'v3', developerKey="AIzaSyAGVkpw0ppuwS_Vcs3XW-saV32a6A7tIP0")


def index(request):
    """
    index page
    :param request:
    :return:
    """
    return render(request, 'Blogger_gender_and_age/index.html')


def add(request, pred_gender):
    """
    Add an author to data base after getting at least his predicted age and gender
    :param request:
    :param pred_gender: passed value in http POST
    :return:redirection to index page
    """
    print("hello")
    author = Author(age=int(request.GET['age']), gender=request.GET['gender'],
                    predictedAge=int(request.GET['pred_age']), predictedGender=pred_gender,
                    date=timezone.now())
    author.save()
    return render(request, 'Blogger_gender_and_age/index.html')


def result(request):
    """
    Get request from the index page
    Depending on the input type it calls functions to retrieve and process data
    It calls the classifier and get predicted values
    Finally, it displays those values or error message
    :param request:request from index page
    :return:the result html page with results or index html page with error
    """

    if 'BlogURL' in request.POST:
        data_id = getIdByUrl(str(request.POST['BlogURL']))
        if data_id[:5] == "error":
            return render(request, 'Blogger_gender_and_age/index.html', {'msg': "Your input is not valid"})
        else:
            data = getDataByBlogId(data_id)
            if data[:5] == "error":
                return render(request, 'Blogger_gender_and_age/index.html', {'msg': "Your input is not valid"})

    elif 'BlogID' in request.POST:
        data = getDataByBlogId(str(request.POST['BlogID']))
        if data[:5] == "error":
            return render(request, 'Blogger_gender_and_age/index.html', {'msg': "Your input is not valid"})

    elif 'rawText' in request.POST:
        data = str(request.POST['rawText'])
    pred_gender, pred_age = predict(data)
    print pred_gender, pred_age
    return render(request, 'Blogger_gender_and_age/result.html', {'pred_age': pred_age, 'pred_gender': pred_gender})


def getIdByUrl(input):
    """
    Get id of a blog from its URL
    :param input: Blog URL
    :return:Blog id or error
    """
    try:
        response = service.blogs().getByUrl(url=input, fields='id').execute()
        pprint.pprint(response)
        id2 = str(response['id'])
        return id2

    except HttpError as e:
        return "error"+e.resp['status']


def getDataByBlogId(input):
    """
    Crawl data using google api
    :param input: Blog id
    :return:crawled data or error
    """
    try:
        response = service.posts().list(blogId=input, maxResults=100, fields="items(title,content)").execute()
        pprint.pprint(response)
        dta = extractData(response)
        return dta

    except HttpError as e:
        return 'error'+e.resp['status']


def extractData(resp):
    """
    Extract the required data from google response
    :param resp: http response
    :return:extracted data
    """
    dt = ''
    for item in resp['items']:
        text = item.get('content')
        soup = BeautifulSoup(text).get_text()
        txt = re.sub(r"(\http://\S*)", '', soup)
        dt = dt + item.get('title') + ' ' + txt+' '
    return dt
