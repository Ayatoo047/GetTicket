from django.shortcuts import render, redirect
from . models import Ticket
from django.db.models import Q

# Create your views here.
def index(request):
    # book_ticket(request)
    if request.method == 'POST':

        owner = request.POST['owner']
        number = request.POST['number']
        email = request.POST['email']
        phone = request.POST['phone']

        total = int(number) * 3500

        ticket = Ticket.objects.create(
           owner = owner,
           number = number,
           email =  email,
           phone =  phone,
           total_amount = total
        )
        return redirect('pay', ticket.id)
    return render(request, 'index.html')

def pay(request, pk):
    ticket = Ticket.objects.get(id=pk)

    context = {'ticket': ticket}
    return render(request, 'pay.html', context)

def book_ticket(request):
    # owner
    #  = request.POST['']
    if request.method == 'POST':

        owner = request.POST['owner']
        number = request.POST['number']
        email = request.POST['email']
        phone = request.POST['phone']

        Ticket.objects.create(
           owner = owner,
           number = number,
           email =  email,
           phone =  phone,
           total_amount = number * 3500
        )

def searchTicket(request):
    search_query = ""

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    # tags = Tags.objects.filter(name__icontains=search_query)

    tickets = Ticket.objects.distinct().filter(
        Q(type__house_type__icontains=search_query) |
        Q(location__location__icontains=search_query) |
        Q(conpletion_status__title__icontains=search_query)
    )

    return tickets, search_query


def all_tickets(request):
    # tickets = House.objects.all()
    tickets, search_query = searchTicket(request)
    # custom_range, tickets = paginatetickets(request, tickets, 10)
    context = {'tickets': tickets, 'search_query': search_query}
    context = {'tickets': tickets,}


def confirm_payment(request, pk):
    ticket = Ticket.objects.get(id=pk)
    ticket.completed = True
    ticket.save()
    # return redirect('index')

def about(request):
    return render(request, 'about.html')