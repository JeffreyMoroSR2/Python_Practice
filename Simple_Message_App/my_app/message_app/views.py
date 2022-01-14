from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from datetime import date, datetime
import sqlite3


def index(request):
    # arr_list = [1, 2, 3]
    # return render(request, 'index.html', {'arr_list' : arr_list})
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('content'):
            post = Post()
            post.username = request.POST.get('username')
            post.content = request.POST.get('content')
            now = datetime.now()
            post.dateSubmitted = now.strftime("%d/%m/%Y %H:%M:%S")
            post.save()


            conn = sqlite3.connect('db.sqlite3')

            cur = conn.cursor()
            cur.execute("select username, content, dateSubmitted from message_app_post")
            rows = cur.fetchall()
            conn.close()

            usernames = []
            content = []
            dates = []
            for row in rows:
                usernames.append(row[0])
                content.append(row[1])
                dates.append(row[2])


            keys = []
            for i in range(len(usernames)):
                keys.append(usernames[i] + ' - ' + dates[i])
            value = content
            message = dict(zip(keys, value))

            return render(request, 'index.html', {'usernames': usernames, 'content': content, 'message': message})

    else:
        conn = sqlite3.connect('db.sqlite3')

        cur = conn.cursor()
        cur.execute("select username, content, dateSubmitted from message_app_post")
        rows = cur.fetchall()
        conn.close()

        usernames = []
        content = []
        dates = []
        for row in rows:
            usernames.append(row[0])
            content.append(row[1])
            dates.append(row[2])

        usernames = []
        content = []
        dates = []
        for row in rows:
            usernames.append(row[0])
            content.append(row[1])
            dates.append(row[2])
        # Test

        keys = []
        for i in range(len(usernames)):
            keys.append(usernames[i] + ' - ' + dates[i])
        value = content
        message = dict(zip(keys, value))

        return render(request, 'index.html', {'usernames': usernames, 'content': content, 'message': message})
