from django.shortcuts import get_list_or_404, render
from django.http import HttpResponseRedirect
from django.template import loader
from .models import Anime, Сharacter, Genre, Anime_Genre


def index(request):
    anime_list = Anime.objects.all()
    genre_anime_list = {}
    for i in anime_list:
        anime_genre_list = get_list_or_404(Anime_Genre, anime=i.id)
        genre_list_lol = []
        for j in anime_genre_list:
            genre_list_lol.append(j.genre.name)
        genre_anime_list[i.id] = genre_list_lol
    genre_list = Genre.objects.all()
    context = {'anime_list': anime_list, 'genre_anime_list': genre_anime_list, 'genre_list': genre_list}
    return render(request, 'jutsu/index.html', context)

 
def character(request, anime_id):
    anime_list = Anime.objects.all()
    anime = 0
    for i in anime_list:
        if i.id == anime_id:
            anime = i
    if request.method == "GET":
        char_list = get_list_or_404(Сharacter, name=anime_id)
        return render(request, 'jutsu/detail_char.html', {'anime': anime,
                                                          'char_list': char_list})
    elif request.method == "POST":
        anime.name = request.POST.get("anime_name")
        anime.release_time = request.POST.get("anime_release")
        anime.save()
        # name_group_change = request.POST.get("group_name")
        # for group in group_list:
        #     if group.name == name_group_change:
        #         group_change = group
        #         break
        # for schedule in schedule_list:
        #     if schedule.group == group_change:
        #         schedule.lesson_time = request.POST.get("lesson_time")
        #         schedule.save()
        return HttpResponseRedirect(f"/jutsu/{anime_id}/")


def genres(request, genre_name):
    genre_list = Genre.objects.all()
    for i in genre_list:
        if i.name == genre_name:
            genre = i.id
    anime_genre_list = get_list_or_404(Anime_Genre, genre=genre)
    anime_list = []
    for i in anime_genre_list:
        anime_list.append(i.anime)
    return render(request, 'jutsu/index.html', {'genre_name': genre_name,
                                                'anime_list': anime_list,
                                                'genre_list': genre_list})