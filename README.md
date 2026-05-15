# Playlist Curator - Final Project (ITP 2)

## Project Overview
Система для управления музыкальными плейлистами с функциями анализа жанров, рекомендаций и экспорта в формат M3U. [cite_start]Проект демонстрирует использование ООП, функционального программирования и работы с файлами в Python[cite: 47, 49].

## Architectural Design (Class Hierarchy)
1. [cite_start]**BaseMedia (Parent)**: Базовый класс для медиа-файлов[cite: 62].
2. [cite_start]**Song (Child)**: Наследует BaseMedia, содержит данные о жанре и длительности[cite: 61, 62].
3. [cite_start]**Playlist**: Класс-контейнер, реализующий связь (Association) и кастомную итерацию[cite: 62, 78].
4. [cite_start]**Services**: Модули для анализа (GenreAnalyzer), рекомендаций (Recommender) и экспорта (M3UExporter)[cite: 50].

## Individual Contributions (Roles)
* **Член группы 1 (Lead of Models)**: Разработка `models/song.py` и `models/playlist.py`. [cite_start]Реализация ООП и итераторов[cite: 88].
* **Член группы 2 (Lead of Services)**: Разработка `services/`. [cite_start]Реализация лямбда-выражений, генераторов и Regex[cite: 88].
* **Член группы 3 (Lead of Logic & Testing)**: Разработка `main.py` и `tests/`. [cite_start]Обеспечение 100% покрытия тестами и PEP8[cite: 88].

## How to Run
1. Запуск приложения: `python main.py`
2. [cite_start]Запуск тестов: `python -m unittest discover tests` [cite: 76]

## Features Implemented
- [x] [cite_start]Advanced OOP (Inheritance, Encapsulation) [cite: 61, 62]
- [x] [cite_start]Functional Programming (map, filter, lambda) [cite: 66]
- [x] [cite_start]Custom Iterators/Generators [cite: 78]
- [x] [cite_start]Input Validation via Regex [cite: 79]
- [x] [cite_start]Unit Testing (unittest) [cite: 76]