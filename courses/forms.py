from django import forms
from .models import Question

class QuizForm(forms.Form):
    def __init__(self, questions, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for q in questions:
            self.fields[f"question_{q.id}"] = forms.ChoiceField(
                label=q.question_text,
                choices=[
                    (1, q.option1),
                    (2, q.option2),
                    (3, q.option3),
                    (4, q.option4),
                ],
                widget=forms.RadioSelect,
                required=True
            )