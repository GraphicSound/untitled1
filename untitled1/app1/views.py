# coding: utf-8
import datetime
import json
import MySQLdb
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def execute_sql(sql):
    connection = MySQLdb.connect(host='127.0.0.1',user='root',passwd='root',db='daxue2',charset='utf8')
    cursor = connection.cursor()
    cursor.execute(sql)
    print sql
    connection.commit()

def query_sql(sql):
    connection = MySQLdb.connect(host='127.0.0.1',user='root',passwd='root',db='daxue2',charset='utf8')
    cursor = connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    return results

def get_cursor():
    connection = MySQLdb.connect(host='127.0.0.1',user='root',passwd='root',db='daxue2',charset='utf8')
    cursor = connection.cursor()
    return cursor

# Create your views here.

def index(request):
    return render(request, 'index.html', {'date': datetime.date.today(), 'request': request})


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=48, help_text='48 characters max.',
                    widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password = forms.CharField(max_length=48, help_text='48 characters max.',
                    widget=forms.TextInput(attrs={'placeholder': 'password'}))
    confirm_password = forms.CharField(
                    widget=forms.TextInput(attrs={'placeholder': 'confirm_password'}))
    cc_myself = forms.BooleanField(required=False)


    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password and password != confirm_password:
            raise forms.ValidationError("Passwords don't match")

        return self.cleaned_data


def register(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            cc_myself = form.cleaned_data['cc_myself']

            # 插入数据库
            sql = "INSERT INTO user (username, password) VALUES ('" + username + "', '" + password + "')"
            print sql
            execute_sql(sql)

            return HttpResponseRedirect('.')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


class InfoForm(forms.Form):
    user_id = forms.CharField(max_length=48, help_text='48 characters max.', widget=forms.TextInput(attrs={'placeholder': 'user_id'}))
    realname = forms.CharField(max_length=48, help_text='48 characters max.', widget=forms.TextInput(attrs={'placeholder': 'realname'}))
    gender = forms.CharField(max_length=48, help_text='48 characters max.', widget=forms.TextInput(attrs={'placeholder': 'gender'}))
    age = forms.CharField(max_length=48, help_text='48 characters max.', widget=forms.TextInput(attrs={'placeholder': 'age'}))
    avatar_link = forms.CharField()
    background_image_link = forms.CharField()
    introduction = forms.CharField()


    def clean(self):

        return self.cleaned_data


def add_info(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = InfoForm(request.POST)

        if form.is_valid():
            user_id = form.cleaned_data['user_id']
            realname = form.cleaned_data['realname']
            gender = form.cleaned_data['gender']
            age = form.cleaned_data['age']
            avatar_link = form.cleaned_data['avatar_link']
            background_image_link = form.cleaned_data['background_image_link']
            introduction = form.cleaned_data['introduction']

            # 插入数据库
            sql = "UPDATE user SET realname = '%s', gender = '%s', age = '%s', avatar_link = '%s', background_image_link = '%s', introduction = '%s' WHERE id = %d" %(realname, gender, age, avatar_link, background_image_link, introduction, int(user_id))
            print sql
            execute_sql(sql)

            return HttpResponseRedirect('.')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = InfoForm()

    return render(request, 'add_info.html', {'form': form})


class ShowcaseForm(forms.Form):
    user_id = forms.CharField(max_length=48, help_text='48 characters max.', widget=forms.TextInput(attrs={'placeholder': 'user_id'}))
    title = forms.CharField(max_length=48, help_text='48 characters max.', widget=forms.TextInput(attrs={'placeholder': 'title'}))
    finish_time = forms.CharField(max_length=48, help_text='48 characters max.', widget=forms.TextInput(attrs={'placeholder': 'finish_time'}))
    content = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'content'}))


    def clean(self):

        return self.cleaned_data


def add_showcase(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ShowcaseForm(request.POST)

        if form.is_valid():
            user_id = form.cleaned_data['user_id']
            title = form.cleaned_data['title']
            finish_time = form.cleaned_data['finish_time']
            content = form.cleaned_data['content']
            add_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # 插入数据库
            sql = "INSERT INTO showcase (title, finish_time, content, add_time) VALUES ('%s', '%s', '%s', '%s')" %(title, finish_time, content, add_time)
            print sql
            execute_sql(sql)

            return HttpResponseRedirect('.')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ShowcaseForm()

    return render(request, 'add_showcase.html', {'form': form})


class NoteForm(forms.Form):
    user_id = forms.CharField(max_length=48, help_text='48 characters max.', widget=forms.TextInput(attrs={'placeholder': 'user_id'}))
    title = forms.CharField(max_length=48, help_text='48 characters max.', widget=forms.TextInput(attrs={'placeholder': 'title'}))
    content = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'content'}))


    def clean(self):

        return self.cleaned_data


def add_note(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NoteForm(request.POST)

        if form.is_valid():
            user_id = form.cleaned_data['user_id']
            title = form.cleaned_data['title']
            add_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            content = form.cleaned_data['content']

            # 插入数据库
            sql = "INSERT INTO note (user_id, title, content, add_time) VALUES (%d, '%s', '%s', '%s')" %(int(user_id), title, content, add_time)
            print sql
            execute_sql(sql)

            return HttpResponseRedirect('.')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NoteForm()

    return render(request, 'add_note.html', {'form': form})


def stage(request):
    user_id = request.GET.get('user_id')

    return render(request, 'stage.html', {'user_id': user_id})


class NewShowcaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(NewShowcaseForm, self).__init__(*args, **kwargs)

    type = forms.CharField(
    )

    title = forms.CharField(
        label="作品名称", required=True, max_length=48, help_text = "请不要超过48字"
    )

    finish_time = forms.DateField(
        label="完成时间", required=True # , input_formats=['%y/%m/%d']
    )

    content = forms.CharField(
        label="作品内容", required=True, widget = forms.Textarea(),
    )

    checkboxes = forms.MultipleChoiceField(
        label="版权声明",
        choices = (
            ('option_one', "同意本网站相关协议"),
        ),
        initial = 'option_one',
        widget = forms.CheckboxSelectMultiple,
        help_text = "<strong>注意:</strong> 一切解释权归本网站所有",
    )

    # Uni-form
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('type', css_class='hidden'),
        Field('title', css_class='input-xlarge'),
        Field('finish_time', css_class='input-xlarge'),
        Field('content', rows="3", css_class='input-xlarge'),
        Field('checkboxes', style="background: #FAFAFA; padding: 10px;"),
        FormActions(
            Submit('save_changes', '完成', css_class="btn-primary"),
            Submit('cancel', '取消'),
        )
    )


class NewNoteForm(forms.Form):
    text_input = forms.CharField()

    textarea = forms.CharField(
        widget = forms.Textarea(),
    )

    radio_buttons = forms.ChoiceField(
        choices = (
            ('option_one', "Option one is this and that be sure to include why it's great"),
            ('option_two', "Option two can is something else and selecting it will deselect option one")
        ),
        widget = forms.RadioSelect,
        initial = 'option_two',
    )

    checkboxes = forms.MultipleChoiceField(
        choices = (
            ('option_one', "Option one is this and that be sure to include why it's great"),
            ('option_two', 'Option two can also be checked and included in form results'),
            ('option_three', 'Option three can yes, you guessed it also be checked and included in form results')
        ),
        initial = 'option_one',
        widget = forms.CheckboxSelectMultiple,
        help_text = "<strong>Note:</strong> Labels surround all the options for much larger click areas and a more usable form.",
    )

    appended_text = forms.CharField(
        help_text = "Here's more help text"
    )

    prepended_text = forms.CharField()

    prepended_text_two = forms.CharField()

    multicolon_select = forms.MultipleChoiceField(
        choices = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')),
    )

    # Uni-form
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('text_input', css_class='input-xlarge'),
        Field('textarea', rows="3", css_class='input-xlarge'),
        'radio_buttons',
        Field('checkboxes', style="background: #FAFAFA; padding: 10px;"),
        AppendedText('appended_text', '.00'),
        PrependedText('prepended_text', '<input type="checkbox" checked="checked" value="" id="" name="">', active=True),
        PrependedText('prepended_text_two', '@'),
        'multicolon_select',
        FormActions(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
            Submit('cancel', 'Cancel'),
        )
    )


def background(request):
    user_id = request.GET.get('user_id')

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form1 = NewShowcaseForm(request.POST)

        if form1.is_valid():
            title = form1.cleaned_data['title']
            finish_time = form1.cleaned_data['finish_time']
            content = form1.cleaned_data['content']
            add_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # 插入数据库
            sql = "INSERT INTO showcase (user_id, title, finish_time, content, add_time) VALUES (%d, '%s', '%s', '%s', '%s')" %(int(user_id), title, finish_time, content, add_time)
            print sql
            execute_sql(sql)

            return HttpResponseRedirect('.')

    # if a GET (or any other method) we'll create a blank form
    else:
        form1 = NewShowcaseForm(initial = {"type": "1"})

    return render(request, 'background.html', {'user_id': user_id, 'NewShowcaseForm': form1, 'NewNoteForm': NewNoteForm})

# url interface

class Incrementor():
    index = -1
    def reset(self):
        index = -1
    def increment(self):
        self.index += 1
        return self.index

def api_latest_job(request):
    sql = "select j.id, j.title, j.salary, j.introduction, j.post_time, j.workplace, e.realname, e.avatar_link, c.name as company_name, c.introduction as company_introduction, c.location as company_location from job j inner join employer e on j.employer_id = e.id inner join company c on e.company_id = c.id LIMIT 4"
    print sql
    cursor = get_cursor()
    cursor.execute(sql)

    # 封装成数组
    result_array = []
    for row in cursor:
        # 封装成字典
        incrementor = Incrementor()
        row_dic = {'id': row[incrementor.increment()], 'title': row[incrementor.increment()], 'salary': row[incrementor.increment()], 'introduction': row[incrementor.increment()], 'post_time': row[incrementor.increment()], 'workplace': row[incrementor.increment()], 'realname': row[incrementor.increment()], 'avatar_link': row[incrementor.increment()], 'company_name': row[incrementor.increment()], 'company_introduction': row[incrementor.increment()], 'company_location': row[incrementor.increment()]}
        result_array.append(row_dic)

    return HttpResponse(json.dumps(result_array))


def api_latest_note(request):
    sql = "select n.id, n.user_id, n.title, n.content, n.add_time, u.realname, u.avatar_link from note n left join user u on n.user_id = u.id group by n.user_id ORDER BY n.id desc limit 4"
    print sql
    cursor = get_cursor()
    cursor.execute(sql)

    # 封装成数组
    result_array = []
    for row in cursor:
        # 封装成字典
        incrementor = Incrementor()
        row_dic = {'id': row[incrementor.increment()], 'user_id': row[incrementor.increment()], 'title': row[incrementor.increment()], 'content': row[incrementor.increment()], 'add_time': row[incrementor.increment()], 'realname': row[incrementor.increment()], 'avatar_link': row[incrementor.increment()]}
        result_array.append(row_dic)

    return HttpResponse(json.dumps(result_array))


def api_info(request):
    user_id = request.GET.get('user_id')

    sql = "SELECT u.id, u.username, u.realname, u.gender, u.age, u.avatar_link, u.background_image_link, u.introduction, f.description as field_description, s.description as speciality_description FROM user u left join user_field f on u.id = f.user_id left join user_speciality s on u.id = s.user_id WHERE u.id = %d" %(int(user_id))
    print sql
    cursor = get_cursor()
    cursor.execute(sql)

    # 封装成数组
    result_array = []
    for row in cursor:
        # 封装成字典
        incrementor = Incrementor()
        row_dic = {'id': row[incrementor.increment()], 'username': row[incrementor.increment()], 'realname': row[incrementor.increment()], 'gender': row[incrementor.increment()], 'age': row[incrementor.increment()], 'avatar_link': row[incrementor.increment()], 'background_image_link': row[incrementor.increment()], 'introduction': row[incrementor.increment()], 'field_description': row[incrementor.increment()], 'speciality_description': row[incrementor.increment()]}
        result_array.append(row_dic)

    return HttpResponse(json.dumps(result_array))


def api_showcase(request):
    user_id = request.GET.get('user_id')

    sql = "SELECT s.id, s.user_id, s.title, s.content, s.finish_time, s.add_time, i.link FROM showcase s left join image_link i on s.id = i.showcase_id WHERE user_id = %d ORDER BY finish_time" %(int(user_id))
    print sql
    cursor = get_cursor()
    cursor.execute(sql)

    # 封装成数组
    result_array = []
    for row in cursor:
        # 封装成字典
        incrementor = Incrementor()
        row_dic = {'id': row[incrementor.increment()], 'user_id': row[incrementor.increment()], 'title': row[incrementor.increment()], 'content': row[incrementor.increment()], 'finish_time': row[incrementor.increment()], 'add_time': row[incrementor.increment()], 'link': row[incrementor.increment()]}
        result_array.append(row_dic)

    return HttpResponse(json.dumps(result_array))


def api_note(request):
    user_id = request.GET.get('user_id')

    sql = "SELECT s.id, s.user_id, s.title, s.content, s.add_time, i.link FROM note s left join image_link i on s.id = i.note_id WHERE user_id = %d ORDER BY add_time" %(int(user_id))
    print sql
    cursor = get_cursor()
    cursor.execute(sql)

    # 封装成数组
    result_array = []
    for row in cursor:
        # 封装成字典
        incrementor = Incrementor()
        row_dic = {'id': row[incrementor.increment()], 'user_id': row[incrementor.increment()], 'title': row[incrementor.increment()], 'content': row[incrementor.increment()], 'add_time': row[incrementor.increment()], 'link': row[incrementor.increment()]}
        result_array.append(row_dic)

    return HttpResponse(json.dumps(result_array))


def api_job(request):
    return None
