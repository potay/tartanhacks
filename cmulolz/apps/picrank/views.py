import random, datetime
from django.shortcuts import render
from models import Picture, Vote, Winner
from forms import PictureForm

def index(request):
	return render(request, "index.html")
# Create your views here.
def upload(request):
	if request.method == 'POST':
		form = PictureForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = PictureForm()
	return render(request, 'upload.html', {'form': form})

def vote(request):
	picture_id = None
	if request.method == 'POST':
		picture_id = request.POST['selectedPic']
		picture = Picture.objects.get(pk = picture_id)
		vote = Vote(picture = picture)
		vote.save()

	date = datetime.datetime.today()
	picture_set = Picture.objects.filter(timestamp__day = date.day,
										 timestamp__month = date.month,
		                                 timestamp__year = date.year)
	
	if picture_id:
		picture_set = picture_set.exclude(pk = picture_id)

	if len(picture_set) > 1:
		picture_pair = random.sample(picture_set, 2)
		sufficient_picture = True
	else:
		picture_pair = None
		sufficient_picture = False

	return render(request, 'vote.html', {'pictures': picture_pair;
		                                 'sufficient': sufficient_picture})

def result(request):
	date = datetime.datetime.today()
	picture_set = Picture.objects.filter(timestamp__day = date.day,
									     timestamp__month = date.month,
		                                 timestamp__year = date.year)

	if picture_set > 0:
		try:
			print date.day, date.month, date.year
			winner = Winner.objects.get(date__day = date.day,
			                            date__month = date.month,
			                            date__year = date.year)
			top_votes = winner.picture.vote_set.count()
			top_picture = winner

		except:
			top_votes = None
			top_picture = None

		for top in picture_set:
			if top.vote_set.count() > top_votes:
				if top_votes > 0:
					top_picture.picture = top
					top_votes = top.vote_set.count()
				else:

					top_picture = Winner(picture = top, 
						                 date = datetime.date.today())
					top_votes = top.vote_set.count()
		top_picture.save()
		winner_list = Winner.objects.all().order_by('-date')

	else:
		winner_list = []

	return render(request, 'results.html', {'winners': winner_list})







