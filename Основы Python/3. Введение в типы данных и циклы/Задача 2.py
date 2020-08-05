cook_book = [
  ['salad',
      [
        ['potatoes', 100, 'gr.'],
        ['carrot', 50, 'gr.'],
        ['cucumbers', 50, 'gr.'],
        ['peas', 30, 'gr.'],
        ['mayonnaise', 70, 'ml.'],
      ]
  ],
  ['pizza',  
      [
        ['cheese', 50, 'gr.'],
        ['tomatoes', 50, 'gr.'],
        ['dough', 100, 'gr.'],
        ['bacon', 30, 'gr.'],
        ['sausage', 30, 'gr.'],
        ['mushrooms', 20, 'gr.'],
      ],
  ],
  ['fruit dessert',
      [
        ['persimmon', 60, 'gr.'],
        ['kiwi', 60, 'gr.'],
        ['curd', 60, 'gr.'],
        ['sugar', 10, 'gr.'],
        ['honey', 50, 'ml.'],  
      ]
  ]
]
person = 5

for recipe in cook_book:
  print(recipe[0])
  for ingrs in recipe[1]:
    print("{}, {} {}".format(ingrs[0], ingrs[1] * person, ingrs[2]))
  print()