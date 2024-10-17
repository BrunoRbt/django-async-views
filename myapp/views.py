import asyncio
from django.http import JsonResponse

async def async_counter(request):
    for i in range(5):
        await asyncio.sleep(1)
        print(f"Contagem: {i+1}")
    return JsonResponse({'message': 'Contagem concluída'})
