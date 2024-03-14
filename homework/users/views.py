from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, LoginForm, AuthorForm, QuoteForm
from quotes.models import Tag, Author
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


def signupuser(request):
    if request.user.is_authenticated:
        return redirect(to='quotes:root')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:root')
        else:
            return render(request, 'users/signup.html', context={"form": form})

    return render(request, 'users/signup.html', context={"form": RegisterForm()})


def loginuser(request):
    if request.user.is_authenticated:
        return redirect(to='quotes:root')

    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, 'Username or password didn\'t match')
            return redirect(to='users:login')

        login(request, user)
        return redirect(to='quotes:root')

    return render(request, 'users/login.html', context={"form": LoginForm()})


@login_required
def logoutuser(request):
    logout(request)
    return redirect(to='quotes:root')


@login_required
def addquote(request):
    tags = Tag.objects.all()
    authors = Author.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():

            new_quote = form.save(commit=False)

            author_name = request.POST.get("author")
            if author_name:
                chosen_author = Author.objects.get(fullname=author_name)
                new_quote.author = chosen_author

            new_quote.save()
            chosen_tags = Tag.objects.filter(name__in=request.POST.getlist("tags"))
            for tag in chosen_tags:
                new_quote.tags.add(tag)

            return redirect(to='quotes:root')
        else:
            return render(request, 'users/addquote.html', {'authors': authors, 'tags': tags, 'form': form})
    return render(request, 'users/addquote.html', context={'authors': authors, 'tags': tags, "form": QuoteForm()})


@login_required
def addauthor(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:root')
        else:
            return render(request, 'users/addauthor.html', {'form': form})
    return render(request, 'users/addauthor.html', context={"form": AuthorForm()})


@login_required
def profile(request):
    return render(request, 'users/profile.html')


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    html_email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')
    success_message = "An email with instructions to reset your password has been sent to %(email)s."
    subject_template_name = 'users/password_reset_subject.txt'



