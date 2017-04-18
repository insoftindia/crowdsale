from django import forms
from .models import CrowdFundingPostProposal, CrowdFundingProposalContribute

class CrowdFundingPostProposalForm(forms.ModelForm):

    class Meta:
        model = CrowdFundingPostProposal
        fields = ('title', 'text','amount', 'end_date')


class CrowdFundingProposalContributeForm(forms.ModelForm):

    class Meta:
        model = CrowdFundingProposalContribute
        fields = ('amount',)