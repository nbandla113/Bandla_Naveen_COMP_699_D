from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TextReviewForm, ImageReviewForm, DraftReviewForm
from .services import (
    process_text_review,
    process_image_review,
    process_draft_review,
    get_review_result,
    get_user_history,
    clear_history
)


@login_required
def text_review_view(request):
    form = TextReviewForm()

    if request.method == "POST":
        form = TextReviewForm(request.POST)
        if form.is_valid():
            content = process_text_review(request.user, form.cleaned_data['text'])
            return redirect('result', content_id=content.id)

    return render(request, 'content/text_review.html', {'form': form})


@login_required
def image_review_view(request):
    form = ImageReviewForm()

    if request.method == "POST":
        form = ImageReviewForm(request.POST, request.FILES)
        if form.is_valid():
            content = process_image_review(request.user, request.FILES['image'])
            return redirect('result', content_id=content.id)

    return render(request, 'content/image_review.html', {'form': form})


@login_required
def draft_review_view(request):
    form = DraftReviewForm()

    if request.method == "POST":
        form = DraftReviewForm(request.POST, request.FILES)
        if form.is_valid():
            content = process_draft_review(
                request.user,
                form.cleaned_data.get('text'),
                request.FILES.get('image')
            )
            return redirect('result', content_id=content.id)

    return render(request, 'content/draft_review.html', {'form': form})


@login_required
def result_view(request, content_id):
    from .models import Content
    content = Content.objects.get(id=content_id)
    result = get_review_result(content)

    return render(request, 'content/result.html', {
        'content': content,
        'result': result
    })


@login_required
def history_view(request):
    history = get_user_history(request.user)
    return render(request, 'content/history.html', {'history': history})


@login_required
def clear_history_view(request):
    clear_history(request.user)
    return redirect('history')