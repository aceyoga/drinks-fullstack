from django.shortcuts import render
from django.http import JsonResponse
from .db import get_db_connection

def index(request):
    return render(request, 'index.html')

def get_all_drinks(request):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM drinks")
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        drinks = [dict(zip(columns, row)) for row in rows]
        return JsonResponse(drinks, safe=False)
    except Exception as error:
        return JsonResponse({'error': str(error)}, status=500)
    finally:
        if cursor:
            cursor.close()

def get_drink(request, drink_id):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM drinks WHERE id = %s", [drink_id])
        row = cursor.fetchone()
        if row:
            columns = [col[0] for col in cursor.description]
            drink = dict(zip(columns, row))
            return JsonResponse(drink)
        else:
            return JsonResponse({'error': 'Drink not found'}, status=404)
    except Exception as error:
        return JsonResponse({'error': str(error)}, status=500)
    finally:
        if cursor:
            cursor.close()

def create_drink(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO drinks (name, description, price) VALUES (%s, %s, %s)",
                [name, description, price]
            )
            connection.commit()
            return JsonResponse({'message': 'Drink created successfully'})
        except Exception as error:
            return JsonResponse({'error': str(error)}, status=500)
        finally:
            if cursor:
                cursor.close()

def update_drink(request, drink_id):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            cursor.execute(
                "UPDATE drinks SET name = %s, description = %s, price = %s WHERE id = %s",
                [name, description, price, drink_id]
            )
            connection.commit()
            return JsonResponse({'message': 'Drink updated successfully'})
        except Exception as error:
            return JsonResponse({'error': str(error)}, status=500)
        finally:
            if cursor:
                cursor.close()

def delete_drink(request, drink_id):
    if request.method == 'DELETE':
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            cursor.execute("DELETE FROM drinks WHERE id = %s", [drink_id])
            connection.commit()
            return JsonResponse({'message': 'Drink deleted successfully'})
        except Exception as error:
            return JsonResponse({'error': str(error)}, status=500)
        finally:
            if cursor:
                cursor.close()