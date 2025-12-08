import typer

def main(
    name: str,
    lastname: str = typer.Option(
        "", help="Фамилия пользователя (необязательная)."
    ),
    formal: bool = typer.Option(
        False, "--formal", "-f", help="Использовать формальное приветствие."
    ),
):
    """
    Выводит приветствие пользователю.

    Аргументы:
        name (str): Имя пользователя.
        lastname (str, optional): Фамилия пользователя. По умолчанию пустая.
        formal (bool, optional): Если True, используется формальное приветствие.
    """
    # Проверяем, нужно ли формальное приветствие
    if formal:
        greeting = f"Добрый день, {name} {lastname}!".strip()
    else:
        greeting = f"Привет, {name}!"

    print(greeting)


if __name__ == "__main__":
    # Запускаем CLI с помощью Typer
    typer.run(main)

