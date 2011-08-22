from django.shortcuts import get_object_or_404, render_to_response
from blog.models import Post
from datetime import datetime

def show_post(request,year,month,day,title):
	date = datetime(int(year),int(month),int(day))
	post = get_object_or_404(Post,date=date,title=title)
	return render_to_response("delivery/blog/post.html",{"post":post})
