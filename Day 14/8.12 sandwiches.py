def want_sandwich(*items):
    print("We have following sandwiches ready to be served: ")
    for item in items:
        print(item)
    
want_sandwich("tomato", "grilled toast", "cheese sandwich")