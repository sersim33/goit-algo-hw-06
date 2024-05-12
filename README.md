# goit-algo-hw-06
Ми проаналізуали зв"язок декількох станцій лондонського метро (в файлі test була спроба дослідити більше станцій, використовуючи CSV файл London tube lines, але виникли деякі труднощі з розподілом ребер та вузлів... Тому для подальшого аналізу вкористовувалися 8 вузлів)


Ми використали алгоритми пошуку в ширину (BFS) та пошуку в глибину (DFS), використовуючи за старт вузел Waterloo. 
Різниця між результатами в тому, що пошук у глибину (DFS) виконується шляхом відвідування вершини, а потім рекурсивного відвідування всіх сусідніх вершин, які ще не були відвідані.  А BFS  відвідує всі вершини на певному рівні перед тим, як перейти до наступного рівня:

DFS
Waterloo Paddington Charing Cross Baker Street Willesden Junction Wealdstone Oxford Circus Lambeth North 

BFS
Waterloo Charing Cross Paddington Oxford Circus Willesden Junction Baker Street Wealdstone Lambeth North

Також було проаналізовано найшвидші маршрути від ст Baker Street до інших станцій.