def search_fruit(shops, fruit):
    result = []
    for shop in shops:
        for department in shops[shop]:
            for goods in shops[shop][department]:
                if fruit.lower() in goods.lower():
                    result.append((shop, department))
    if not result:
        result.append((None, None))
    return result


if __name__ == "__main__":
    shops = {
        "Шестёрочка": {
            "Консервы": [
                "Ананасы кусочками",
                "Ананасы колечками"
            ],
            "Сухофрукты": [
                "Тропические ананасы",
                "Дуриан вяленый"
            ],
            "Фрукты": [
                "Бананы",
                "Манго"
            ]
        },
        "Микси": {
            "Овощи-фрукты": [
                "Яблоки",
                "Груши",
                "Личи"
            ]
        }
    }
    fruit = input()
    print(*search_fruit(shops, fruit))
