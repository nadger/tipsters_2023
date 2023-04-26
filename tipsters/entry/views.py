from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms import (
    ModelForm,
    formset_factory,
    inlineformset_factory,
    modelformset_factory,
)
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import score_entry
from .models import Fixtures, Players, Question, configdata, entry_data_new

User = get_user_model()


class entryview(TemplateView):
    template_name = "entry/entries_form_df.html"

    def get(self, request, pk):
        # game_week = Fixtures.objects.filter(game_week='1')
        current_user = request.user
        current_usrid = current_user.id
        current_gw = pk
        usr_team_name = User.team_name
        gwdata = get_object_or_404(configdata, id=current_gw)
        if gwdata.gw_active == False:
            return render(request, "entries/error.html")
        gw_fix = Fixtures.objects.filter(game_week__pk=current_gw)
        gw_questions = Question.objects.filter(game_week__pk=current_gw)
        if entry_data_new.objects.filter(
            user_id__pk=current_usrid, entry_gw=pk
        ).exists():
            entry_data = entry_data_new.objects.get(
                user_id__pk=current_usrid, entry_gw=pk
            )
            EntryFormSet = score_entry(instance=entry_data)
        else:
            EntryFormSet = score_entry(
                initial={
                    "fixture_id1": gw_fix[0].pk,
                    "fixture_id2": gw_fix[1].pk,
                    "fixture_id3": gw_fix[2].pk,
                    "fixture_id4": gw_fix[3].pk,
                    "fixture_id5": gw_fix[4].pk,
                    "fixture_id6": gw_fix[5].pk,
                    "fixture_id7": gw_fix[6].pk,
                    "fixture_id8": gw_fix[7].pk,
                    "fixture_id9": gw_fix[8].pk,
                    "fixture_id10": gw_fix[9].pk,
                    "question_id1": gw_questions[0].pk,
                    "question_id2": gw_questions[1].pk,
                    "question_id3": gw_questions[2].pk,
                    "question_id4": gw_questions[3].pk,
                    "question_id5": gw_questions[4].pk,
                    "question_id6": gw_questions[5].pk,
                    "question_id7": gw_questions[6].pk,
                    "question_id8": gw_questions[7].pk,
                    "entry_gw": current_gw,
                    "user_id": current_usrid,
                }
            )
        form = EntryFormSet
        context = {
            "gw_fix": gw_fix,
            "form": form,
            "gwdata": gwdata,
            "gw_questions": gw_questions,
            "usr_team_name": usr_team_name,
        }
        return render(request, self.template_name, {"context": context})

    def post(self, request, pk):
        current_user = request.user
        current_usrid = current_user.id
        usr_team_name = User.team_name
        current_gw = pk
        gwdata = get_object_or_404(configdata, id=current_gw)
        gw_fix = Fixtures.objects.filter(game_week=pk)
        gw_questions = Question.objects.filter(game_week__pk=current_gw)
        if entry_data_new.objects.filter(
            user_id__pk=current_usrid, entry_gw=pk
        ).exists():
            update_ins = entry_data_new.objects.get(
                user_id__pk=current_usrid, entry_gw=pk
            )
            form = score_entry(request.POST, instance=update_ins)
        else:
            form = score_entry(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.entry_GW = pk
            post.entry_team = current_usrid
            post.save()
        context = {
            "gw_fix": gw_fix,
            "form": form,
            "gwdata": gwdata,
            "gw_questions": gw_questions,
            "usr_team_name": usr_team_name,
        }
        return render(request, self.template_name, {"context": context})
