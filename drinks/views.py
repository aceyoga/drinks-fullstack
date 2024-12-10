from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def get_all_drinks(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM drinks")
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        drinks = [dict(zip(columns, row)) for row in rows]
    return JsonResponse(drinks, safe=False)

def get_drink(request, drink_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM drinks WHERE id = %s", [drink_id])
        row = cursor.fetchone()
        if row:
            columns = [col[0] for col in cursor.description]
            drink = dict(zip(columns, row))
            return JsonResponse(drink)
        else:
            return JsonResponse({'error': 'Drink not found'}, status=404)

def create_drink(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO drinks (name, description, price) VALUES (%s, %s, %s)",
                [name, description, price]
            )
        return JsonResponse({'message': 'Drink created successfully'})

def update_drink(request, drink_id):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE drinks SET name = %s, description = %s, price = %s WHERE id = %s",
                [name, description, price, drink_id]
            )
        return JsonResponse({'message': 'Drink updated successfully'})

def delete_drink(request, drink_id):
    if request.method == 'DELETE':
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM drinks WHERE id = %s", [drink_id])
        return JsonResponse({'message': 'Drink deleted successfully'})