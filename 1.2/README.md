## README

## Why dictionary for a recipe 
I chose a dictionary to store each recipe because it keeps every attribute as a clear key-value pair, making fields like name, cooking_time, and ingredients easy to read and retrieve. Keys give the structure flexibility: I can add new attributes without reshaping existing data. This clarity and adaptability help when editing recipes now and when the Recipe app grows.

## Why list for all_recipes
I used a list to hold all recipes because a list naturally keeps entries in sequence and supports quick iteration. It lets me append new recipes, remove outdated ones, and loop over the collection for printing or searching without extra overhead. This makes scaling the Recipe app straightforward while keeping code simple and readable.
