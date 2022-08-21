from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from cats.models import Cat, Breed
from cats.forms import CatForm, BreedForm

class MainView(LoginRequiredMixin, View):
    def get(self, request):
        breedCount = Breed.objects.all().count()
        catList = Cat.objects.all()

        ctx = {'breed_count': breedCount, 'cat_list': catList}
        return render(request, 'cats/cat_list.html', ctx)

class BreedView(LoginRequiredMixin, View):
    def get(self, request):
        breedList = Breed.objects.all()
        ctx = {'breed_list': breedList}
        return render(request, 'cats/breed_list.html', ctx)

class CatUpdate(LoginRequiredMixin, View):
    model = Cat
    template = 'cats/cat_form.html'
    success_url = reverse_lazy('cats:all')

    def get(self, request, pk):
        catIsSelected = get_object_or_404(self.model, pk=pk)
        form = CatForm(instance=catIsSelected)
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        catIsSelected = get_object_or_404(self.model, pk=pk)
        form = CatForm(request.POST, instance=catIsSelected)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)

class CatDelete(LoginRequiredMixin, View):
    model = Cat
    success_url = reverse_lazy('cats:all')
    template = 'cats/cat_confirm_delete.html'

    def get(self, request, pk):
        catIsSelected = get_object_or_404(self.model, pk=pk)
        form = CatForm(instance=catIsSelected)
        ctx = {'cat': catIsSelected}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        catIsDeleted = get_object_or_404(self.model, pk=pk)
        catIsDeleted.delete()
        return redirect(self.success_url)

class CatCreate(LoginRequiredMixin, View):
    template = 'cats/cat_form.html'
    success_url = reverse_lazy('cats:all')

    def get(self, request):
        form = CatForm()
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request):
        form = CatForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)
        form.save()
        return redirect(self.success_url)

#generic views
class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


