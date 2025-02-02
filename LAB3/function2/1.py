def moviefunc(mov):
    if mov["imdb"]>5.5:
        print(mov["name"])



movie=[
    {
        "name": "We Two",
        "imdb": 7.2,
        "category": "Romance"
    }
]

for m in movie:
    moviefunc(m)