from __future__ import annotations
from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        """
        !!Задание нужно решить используя map!!
        Посчитать средний рейтинг фильмов (rating_kinopoisk) у которых две или больше стран.
        Фильмы у которых рейтинг не задан или равен 0 не учитывать в расчете среднего.

        :param list_of_movies: Список фильмов.
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :return: Средний рейтинг фильмов у которых две или больше стран
        """

        def get_rating(movie: dict) -> int:
            if "," in movie["country"] and movie["rating_kinopoisk"]:
                return float(movie["rating_kinopoisk"])
            return 0

        ratings = [get_rating(movie) for movie in list_of_movies]
        ratings = [r for r in ratings if r > 0]
        avg_rating = sum(ratings) / len(ratings)
        return avg_rating

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        """
        !!Задание нужно решить используя map!!
        Посчитать количество букв 'и' в названиях всех фильмов с рейтингом (rating_kinopoisk) больше
        или равным заданному значению

        :param list_of_movies: Список фильмов
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :param rating: Заданный рейтинг
        :return: Количество букв 'и' в названиях всех фильмов с рейтингом больше
        или равным заданному значению
        """

        def chars_count_each(movie: dict) -> int:
            if movie["rating_kinopoisk"] and float(movie["rating_kinopoisk"]) >= rating:
                encounters = [True for char in movie["name"] if char == "и"]
                return encounters.count(True)
            return 0

        return sum([chars_count_each(movie) for movie in list_of_movies])
