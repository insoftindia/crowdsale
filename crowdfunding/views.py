from django.contrib.auth.decorators import login_required
from .models import CrowdFundingMemberGroup, CrowdFundingMemberGroup, UserExtendedForFunding, CrowdFundingPostProposal, CrowdFundingProposalContribute
from .forms import CrowdFundingPostProposalForm, CrowdFundingProposalContributeForm
from django.shortcuts import redirect, get_object_or_404, render
from django.utils import timezone
from django.http import JsonResponse, HttpResponse
from django.db.models import Sum
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from login.forms import RegistrationForm
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url='/')
def crowdfunding(request):
    group_type = CrowdFundingMemberGroup.objects.all()
    latest_posts = CrowdFundingPostProposal.objects.filter(published_datetime__lte=timezone.now(), state='DT').order_by('published_datetime')
    closed_posts = CrowdFundingPostProposal.objects.filter(published_datetime__lte=timezone.now(), state='CD').order_by('published_datetime')
    closed_len = len(closed_posts)
    latest_len = len(latest_posts)
    facilitator_count = UserExtendedForFunding.objects.filter(user_type='FR').count()
    member_count = UserExtendedForFunding.objects.filter(user_type='MR').count()
    # voted_by_me_count = CrowdFundingProposalVoting.objects.filter(author=request.user).count()
    return render(request, 'crowdfunding/crowdfunding_home.html', {'posts':latest_posts, 'member_count':member_count, 'facilitator_count':facilitator_count, 'latest_len':latest_len, 'closed_len':closed_len, 'closed_posts':closed_posts, 'group_type':group_type})

@login_required(login_url='/')
def latest_crowdfunding_proposals(request):
    group_type = CrowdFundingMemberGroup.objects.all()
    latest_posts_list = CrowdFundingPostProposal.objects.filter(published_datetime__lte=timezone.now(), state='DT').order_by('published_datetime')
    latest_paginator = Paginator(latest_posts_list, 8)

    page = request.GET.get('page')
    try:
        latest_posts = latest_paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        latest_posts = latest_paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        latest_posts = latest_paginator.page(latest_paginator.num_pages)

    # upvote = CrowdFundingPostProposal.objects.filter(crowdfundingproposalvoting__vote_type='UP').count()
    # downvote = CrowdFundingPostProposal.objects.filter(crowdfundingproposalvoting__vote_type='DN').count()
    
    return render(request, 'crowdfunding/crowdfunding_proposals.html', {'posts':latest_posts, 'group_type':group_type, 'title':'Open Loan Proposals'})

# def voted_crowdfunding_proposals(request):
#     voted_posts_list = CrowdFundingProposalVoting.objects.filter(author=request.user)
#     self_user_proposal = [x.proposal_id for x in voted_posts_list]
#     return render(request, 'crowdfunding/crowdfunding_proposals.html', {'posts':self_user_proposal, 'title':'Voted Proposals'})

@login_required(login_url='/')
def closed_crowdfunding_proposals(request):

    group_type = CrowdFundingMemberGroup.objects.all()
    closed_posts_list = CrowdFundingPostProposal.objects.filter(published_datetime__lte=timezone.now(), state='CD').order_by('published_datetime')
    closed_paginator = Paginator(closed_posts_list, 4)
    page = request.GET.get('page')
    try:
        closed_posts = closed_paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        closed_posts = closed_paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        closed_posts = closed_paginator.page(closed_paginator.num_pages)
    return render(request, 'crowdfunding/crowdfunding_proposals.html', {'posts':closed_posts, 'group_type':group_type, 'title':'Approved Loan Proposals'})

@login_required(login_url='/')
def create_crowdfunding(request):
    if request.method == "POST":
        form = CrowdFundingPostProposalForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_datetime = timezone.now()
            post.save()
        return redirect('/')
    else:
        form = CrowdFundingPostProposalForm()
    return redirect('/')

@login_required(login_url='/')
def user_creation(request):
    if request.method == "POST":
        if request.POST.get('type') == 'create-user':
            request.POST = request.POST.copy()
            request.POST['repeat_password'] = request.POST.get('password')

            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password'],
                    email=form.cleaned_data['email'],
                )
                user_type = 'FR' if request.POST.get('user_type')=='FR' else 'MR'
                funding_type = 'MR' if request.POST.get('funding_type')=='MR' else 'GR'
                u_extended = UserExtendedForFunding(user=user, user_type=user_type,funding_type=funding_type, user_image=request.FILES.get('user_image'), funding_amout=request.POST.get('funding_amout'), ether_account_private_key=request.POST.get('private_key'))
                u_extended.save()
    return redirect('/')

@login_required(login_url='/')
def crowdfunding_detail(request, pk):

    proposal = get_object_or_404(CrowdFundingPostProposal, pk=pk)
    print proposal, "------------------22222-------", pk

    # group_type = CrowdFundingMemberGroup.objects.all()
    info = CrowdFundingProposalContribute.objects.filter(proposal_id__exact=pk)
    print info, '---------------------info----------'
    # v1 = []
    # info = CrowdFundingProposalContribute.objects.filter(proposal_id__exact=pk)
    # amt = info[1].amount
    # print info, '////////info--------------info', info[1].amount
    # for inf in info:
    #     # v1.append(inf)
    #     v1.append(inf.amount)
    # print v1, '////////////////////////////////----------------'    

    if request.method == "POST":
        print request.POST, "********************", request.user
        form = CrowdFundingProposalContributeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.contributer = request.user
            post.proposal_id = proposal
            post.created_datetime = timezone.now()
            post.save()
            return render(request, 'crowdfunding/post.html', {'post': proposal, 'form':form})
    else:
        form = CrowdFundingProposalContributeForm()
    return render(request, 'crowdfunding/post.html', {'post': proposal, 'form':form, 'contributes':info})

# def line_list(self):
#     data = cr.execute['crowdfunding_crowdfundingproposalcontribute']
#     print data, '--------------data--------'


# def displaytrans(request):
# TransType.objects.all()})
#   info = TransType.objects.all()
#   info2 = Trans.objects.all()
#   print info
#   bookdata = { "detail" : info, "details" : info2 }
#   print bookdata
#   resp =  render_to_response("account/displaytrans.html", bookdata, context_instance=Context(request))
#   return resp



@login_required(login_url='/')
def get_group_total_amount(request):
    group_type = request.GET.get('group_type', None)
    group_funding_amount_tot = UserExtendedForFunding.objects.filter(group_type__in=CrowdFundingMemberGroup.objects.filter(name=group_type)).aggregate(Sum('funding_amout'))
    data = {
        'total_amt': group_funding_amount_tot['funding_amout__sum']
    }
    return JsonResponse(data)

@login_required(login_url='/')
def close_proposal(request):
    post_id = request.GET.get('post_id', None)
    proposal = CrowdFundingPostProposal.objects.filter(pk=post_id)
    proposal.update(state='CD')
    return JsonResponse({})

@login_required(login_url='/')
def get_user_private_key(request):
    user_id = request.GET.get('user_id', None)
    key = False
    if int(request.user.id):
        if request.user.user_extented.ether_account_private_key:
            key = request.user.user_extented.ether_account_private_key
    data = {'key': key}
    return JsonResponse(data)