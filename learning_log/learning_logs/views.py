from django.shortcuts import render
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    '''pagina principal do learning log'''
    return render(request, 'learning_logs/index.html')

def topics(request):
    '''mostra todos os assuntos'''
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics }
    return render(request,'learning_logs/topics.html', context)

def topic(request, topic_id):
    '''mostra um unico assunto e todas as suas entradas'''
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries':entries}
    return render(request,'learning_logs/topic.html', context)

def new_topic(request):
    """adiciona um novo assunto"""
    if request.method != 'POST':
        # nenhum dado submetido/ cria um formulario em branco
        form = TopicForm()
    else:
        # Dados de POST submetidos/ processa os dados
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topics'))
    context = {'form': form}
    return render(request,'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    """acrescenta uma nova entrada pra um assunto em particular"""
    topic = Topic.objects.get(id =topic_id)

    if request.method != 'POST':
        # nenhum dado submetido cria um formulario em branco
        form = EntryForm()
    
    else: 
        #dados de POST submetidos processa os dados
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic =  topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic',args=[topic_id]))
        
    context = {'topic':topic, 'form':form}
    return render(request, 'learning_logs/new_entry.html',context)


def edit_entry(request, entry_id):
    '''edita uma entrada especifica.'''
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # requisicao inicial preenche previmente o formulario com a entrada digital
        form = EntryForm(instance=entry)

    else: 
        # dados de Post submetidos processa os dados
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic', args=[topic.id]))
    context = {'entry':entry, 'topic':topic, 'form': form } 
    return render(request, 'learning_logs/edit_entry.html', context)

