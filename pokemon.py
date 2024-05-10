
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
