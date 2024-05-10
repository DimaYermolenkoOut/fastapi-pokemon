# import aiohttp
# import asyncio
#
# async def fetch_pokemon_data(id):
#     url = f"https://pokeapi.co/api/v2/pokemon/{id}"
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             data = await response.json()
#             return data
#
#
# async def main():
#     pokemon1_id = 1
#     pokemon2_id = 2
#
#     pokemon1_data = await fetch_pokemon_data(pokemon1_id)
#     pokemon2_data = await fetch_pokemon_data(pokemon2_id)
#     # print(pokemon1_data['base_experience'])
#     # print(pokemon2_data['base_experience'])
#
#     # Сравниваем опыт покемонов
#     if pokemon1_data['base_experience'] > pokemon2_data['base_experience']:
#         print(f"{pokemon1_data['name']} выше опыта у {pokemon2_data['name']}.")
#     elif pokemon1_data['base_experience'] < pokemon2_data['base_experience']:
#         print(f"{pokemon2_data['name']} выше опыта у {pokemon1_data['name']}.")
#     else:
#         print(f"{pokemon1_data['name']} и {pokemon2_data['name']} одинакового опыта.")
#
#     # Сравниваем данные покемонов
#     if pokemon1_data['weight'] > pokemon2_data['weight']:
#         print(f"{pokemon1_data['name']} тяжелее, чем {pokemon2_data['name']}.")
#     elif pokemon1_data['weight'] < pokemon2_data['weight']:
#         print(f"{pokemon2_data['name']} тяжелее, чем {pokemon1_data['name']}.")
#     else:
#         print(f"{pokemon1_data['name']} и {pokemon2_data['name']} одинакового веса.")
#
# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())
import aiohttp
import asyncio

async def fetch_pokemon_data(id):
    '''Async function to fetch pokemon data from PokeAPI'''
    url = f"https://pokeapi.co/api/v2/pokemon/{id}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data

async def main():

    pokemon_ids = range(1, 11)  # ID покемонов от 1 до 10

    # Отримуємо дані покемонів асинхронно
    pokemon_data = await asyncio.gather(*(fetch_pokemon_data(id) for id in pokemon_ids))

    # Сортуємо покемонів за досвідом
    sorted_pokemon_data = sorted(pokemon_data, key=lambda p: p['base_experience'], reverse=True)

    # Выводим отсортированный список покемонов
    for pokemon in sorted_pokemon_data:
        print(f"Покемон: {pokemon['name']}, Досвід: {pokemon['base_experience']}")

    print()

    print(f"Переможець за досвідом: {sorted_pokemon_data[0]['name']}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
