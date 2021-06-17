from django.shortcuts import render, redirect
from .models import Topic, Entry  # We first import the model associated with the data we need
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required # decorators son directivas que se escriben antes de una funcion para modificar un toque su comportamiento
from django.http import Http404


def index(request):
    """The home page for Learning Log"""
    return render(request, 'learning_logs/index.html')


def check_owner(request, topic):
    if topic.owner != request.user:  # se asegura que el topic pertence al usuario actual
        raise Http404   # si un usuario quiere acceder a la url de un topic que no le pertenece, salta un error de pagina no encontrada


@login_required  # aca uso el decorator login_required para que solo los usuarios logeados puedan acceder a topics
def topics(request):  # function needs one parameter: the request object Django received from the server
    """Show all topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')  # cuando un usuario se logea el objeto request tiene un atributo user, aca se muestran solo los topics en los que el atributo owner de Topic (en models) sea igual al atributo user de la request.
    context = {'topics': topics}  # es el diccionario que se manda a los templates
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    check_owner(request, topic)
    entries = topic.entry_set.order_by('-date_added')  # el - hace que los ordene al reves, el mas reciente primero.
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':  # puede ser POST o GET
        # no data submitted; create a blank form.
        form = TopicForm
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)  # commite=false hace que no se guarde en la base de datos, pero que quede en la variable new_topic
            new_topic.owner = request.user  # aca le asigno un owner al topic, claramente el usuario que hace la request
            new_topic.save()        # aca si se guarda en la base de datos
            return redirect('learning_logs:topics')
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)
    check_owner(request, topic)
    if request.method != 'POST':
        # No data submitted, create a blank form.
        form = EntryForm()
    else:
        # POST data submitted, process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)  # se crea un objeto Entry con los datos ingresados por el usuario pero no se guarda en la base de datos (commit=False)
            new_entry.topic = topic        # porque antes hay que darle valor a "topic" (un atributo de Entry)
            new_entry.save()           # ahora new_entry SI tiene todos los atributos (topic, text y date_added (que se genera automaticamente) completos.
            return redirect('learning_logs:topic', topic_id=topic_id)  # topic_id explicado en notas.txt
    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:  # chequea que atributo owner de topic sea igual que el atributo user del objeto request.
        raise Http404
    if request.method != 'POST':
        # Initial request, pre-fill form with the current entry.
        form = EntryForm(instance=entry)  # instance=entry hace que se genere un form con la informacion que el objeto ya tenia, por lo tanto se puede editar
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)  # instancia un objeto form con la informacion que ya existia y no fue modificada (instance=entry) y la info agregada y/o modificada (segundo argumento)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)


@login_required
def delete_entry(request, entry_id):
    """Delete an existing entry-"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    check_owner(request, topic)
    #entry.delete()
    return redirect('learning_logs:topic', topic_id=topic.id)