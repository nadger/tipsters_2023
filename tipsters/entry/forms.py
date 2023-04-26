from crispy_forms.bootstrap import InlineCheckboxes, InlineRadios
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    HTML,
    ButtonHolder,
    Div,
    Field,
    Fieldset,
    Hidden,
    Layout,
    Submit,
)
from django import forms
from django.forms import HiddenInput, ModelForm, formset_factory
from django.forms.models import inlineformset_factory, modelformset_factory

from .models import Fixtures, Players, Question, configdata, entry_data_new

question_choices = (
    ("TRUE", "True"),
    ("FALSE", "False"),
)


class score_entry(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        question_answer_id1 = forms.ChoiceField(widget=forms.RadioSelect)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                "",
                HTML(
                    """ <div class="row"><div class="col-3 text-center"> <b> {{ context.gw_fix.0.home_team }} </b> </div> """
                ),
                Div("score_home_fid1", css_class="col-3 text-center"),
                Div("score_away_fid1", css_class="col-3 text-center"),
                HTML(
                    """<div class="col-3 text-center"> <b> {{ context.gw_fix.0.away_team }} </b>  </div> </div>"""
                ),
                HTML(
                    """ <div class="row"><div class="col-3 text-center"> <b> {{ context.gw_fix.1.home_team }} </b> </div> """
                ),
                Div("score_home_fid2", css_class="col-3 text-center"),
                Div("score_away_fid2", css_class="col-3 text-center"),
                HTML(
                    """<div class="col-3 text-center"> <b> {{ context.gw_fix.1.away_team }} </b>  </div> </div>"""
                ),
                HTML(
                    """ <div class="row"><div class="col-3 text-center"> <b> {{ context.gw_fix.2.home_team }} </b> </div> """
                ),
                Div("score_home_fid3", css_class="col-3 text-center"),
                Div("score_away_fid3", css_class="col-3 text-center"),
                HTML(
                    """<div class="col-3 text-center"> <b> {{ context.gw_fix.2.away_team }} </b>  </div> </div>"""
                ),
                HTML(
                    """ <div class="row"><div class="col-3 text-center"> <b> {{ context.gw_fix.3.home_team }} </b> </div> """
                ),
                Div("score_home_fid4", css_class="col-3 text-center"),
                Div("score_away_fid4", css_class="col-3 text-center"),
                HTML(
                    """<div class="col-3 text-center"> <b> {{ context.gw_fix.3.away_team }} </b>  </div> </div>"""
                ),
                HTML(
                    """ <div class="row"><div class="col-3 text-center"> <b> {{ context.gw_fix.4.home_team }} </b> </div> """
                ),
                Div("score_home_fid5", css_class="col-3 text-center"),
                Div("score_away_fid5", css_class="col-3 text-center"),
                HTML(
                    """<div class="col-3 text-center"> <b> {{ context.gw_fix.4.away_team }} </b>  </div> </div>"""
                ),
                HTML(
                    """ <div class="row"><div class="col-3 text-center"> <b> {{ context.gw_fix.5.home_team }} </b> </div> """
                ),
                Div("score_home_fid6", css_class="col-3 text-center"),
                Div("score_away_fid6", css_class="col-3 text-center"),
                HTML(
                    """<div class="col-3 text-center"> <b> {{ context.gw_fix.5.away_team }} </b>  </div> </div>"""
                ),
                HTML(
                    """ <div class="row"><div class="col-3 text-center"> <b> {{ context.gw_fix.6.home_team }} </b> </div> """
                ),
                Div("score_home_fid7", css_class="col-3 text-center"),
                Div("score_away_fid7", css_class="col-3 text-center"),
                HTML(
                    """<div class="col-3 text-center"> <b> {{ context.gw_fix.6.away_team }} </b>  </div> </div>"""
                ),
                HTML(
                    """ <div class="row"><div class="col-3 text-center"> <b> {{ context.gw_fix.7.home_team }} </b> </div> """
                ),
                Div("score_home_fid8", css_class="col-3 text-center"),
                Div("score_away_fid8", css_class="col-3 text-center"),
                HTML(
                    """<div class="col-3 text-center"> <b> {{ context.gw_fix.7.away_team }} </b>  </div> </div>"""
                ),
                HTML(
                    """ <div class="row"><div class="col-3 text-center"> <b> {{ context.gw_fix.8.home_team }} </b> </div> """
                ),
                Div("score_home_fid9", css_class="col-3 text-center"),
                Div("score_away_fid9", css_class="col-3 text-center"),
                HTML(
                    """<div class="col-3 text-center"> <b> {{ context.gw_fix.8.away_team }} </b>  </div> </div>"""
                ),
                HTML(
                    """ <div class="row"><div class="col-3 text-center"> <b> {{ context.gw_fix.9.home_team }} </b> </div> """
                ),
                Div("score_home_fid10", css_class="col-3 text-center"),
                Div("score_away_fid10", css_class="col-3 text-center"),
                HTML(
                    """<div class="col-3 text-center"> <b> {{ context.gw_fix.9.away_team }} </b>  </div> </div>"""
                ),
                "score_tg",
                HTML(""" {{ context.gw_questions.0 }}?<br>"""),
                InlineRadios("question_answer_id1"),
                HTML("""{{ context.gw_questions.1 }}?"""),
                InlineRadios("question_answer_id2"),
                HTML(""" {{ context.gw_questions.2 }}?<br>"""),
                InlineRadios("question_answer_id3"),
                HTML("""{{ context.gw_questions.3 }}?"""),
                InlineRadios("question_answer_id4"),
                HTML(""" {{ context.gw_questions.4 }}?<br>"""),
                InlineRadios("question_answer_id5"),
                HTML("""{{ context.gw_questions.5 }}?"""),
                InlineRadios("question_answer_id6"),
                HTML(""" {{ context.gw_questions.6 }}?<br>"""),
                InlineRadios("question_answer_id7"),
                HTML("""{{ context.gw_questions.7 }}?"""),
                InlineRadios("question_answer_id8"),
                "scorer_player1_ff",
                "scorer_player2_ff",
                "scorer_player3_ff",
                "scorer_player4_ff",
                "fixture_id1",
                "fixture_id2",
                "fixture_id3",
                "fixture_id4",
                "fixture_id5",
                "fixture_id6",
                "fixture_id7",
                "fixture_id8",
                "fixture_id9",
                "fixture_id10",
                "entry_gw",
                "user_id",
                "question_id1",
                "question_id2",
                "question_id3",
                "question_id4",
                "question_id5",
                "question_id6",
                "question_id7",
                "question_id8",
            ),
            ButtonHolder(
                Submit("submit", "Submit", css_class="btn btn-primary btn-lg btn-block")
            ),
        )
        super().__init__(*args, **kwargs)
        self.fields["score_home_fid1"].label = ""
        self.fields["score_home_fid2"].label = ""
        self.fields["score_home_fid3"].label = ""
        self.fields["score_home_fid4"].label = ""
        self.fields["score_home_fid5"].label = ""
        self.fields["score_home_fid6"].label = ""
        self.fields["score_home_fid7"].label = ""
        self.fields["score_home_fid8"].label = ""
        self.fields["score_home_fid9"].label = ""
        self.fields["score_home_fid10"].label = ""
        self.fields["score_away_fid1"].label = ""
        self.fields["score_away_fid2"].label = ""
        self.fields["score_away_fid3"].label = ""
        self.fields["score_away_fid4"].label = ""
        self.fields["score_away_fid5"].label = ""
        self.fields["score_away_fid6"].label = ""
        self.fields["score_away_fid7"].label = ""
        self.fields["score_away_fid8"].label = ""
        self.fields["score_away_fid9"].label = ""
        self.fields["score_away_fid10"].label = ""
        self.fields["score_tg"].label = "Total Goals"
        self.fields["scorer_player1_ff"].label = "Scorer - 4 Points"
        self.fields["scorer_player2_ff"].label = "Scorer - 3 Points"
        self.fields["scorer_player3_ff"].label = "Scorer - 2 Points"
        self.fields["scorer_player4_ff"].label = "Scorer - 1 Points"
        self.fields["question_answer_id1"] = forms.TypedChoiceField(
            label="", widget=forms.RadioSelect(), choices=question_choices
        )
        self.fields["question_answer_id2"] = forms.TypedChoiceField(
            label="", widget=forms.RadioSelect(), choices=question_choices
        )
        self.fields["question_answer_id3"] = forms.TypedChoiceField(
            label="", widget=forms.RadioSelect(), choices=question_choices
        )
        self.fields["question_answer_id4"] = forms.TypedChoiceField(
            label="", widget=forms.RadioSelect(), choices=question_choices
        )
        self.fields["question_answer_id5"] = forms.TypedChoiceField(
            label="", widget=forms.RadioSelect(), choices=question_choices
        )
        self.fields["question_answer_id6"] = forms.TypedChoiceField(
            label="", widget=forms.RadioSelect(), choices=question_choices
        )
        self.fields["question_answer_id7"] = forms.TypedChoiceField(
            label="", widget=forms.RadioSelect(), choices=question_choices
        )
        self.fields["question_answer_id8"] = forms.TypedChoiceField(
            label="", widget=forms.RadioSelect(), choices=question_choices
        )
        self.fields["user_id"].widget = HiddenInput()
        self.fields["entry_gw"].widget = HiddenInput()
        self.fields["fixture_id1"].widget = HiddenInput()
        self.fields["fixture_id2"].widget = HiddenInput()
        self.fields["fixture_id3"].widget = HiddenInput()
        self.fields["fixture_id4"].widget = HiddenInput()
        self.fields["fixture_id5"].widget = HiddenInput()
        self.fields["fixture_id6"].widget = HiddenInput()
        self.fields["fixture_id7"].widget = HiddenInput()
        self.fields["fixture_id8"].widget = HiddenInput()
        self.fields["fixture_id9"].widget = HiddenInput()
        self.fields["fixture_id10"].widget = HiddenInput()
        self.fields["question_id1"].widget = HiddenInput()
        self.fields["question_id2"].widget = HiddenInput()
        self.fields["question_id3"].widget = HiddenInput()
        self.fields["question_id4"].widget = HiddenInput()
        self.fields["question_id5"].widget = HiddenInput()
        self.fields["question_id6"].widget = HiddenInput()
        self.fields["question_id7"].widget = HiddenInput()
        self.fields["question_id8"].widget = HiddenInput()
        # ßself.fields["question_answer_id1"].widget = forms.RadioSelect()

    class Meta:
        model = entry_data_new
        exclude = ()
